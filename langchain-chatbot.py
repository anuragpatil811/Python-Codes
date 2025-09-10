import streamlit as st
import os
import requests
import json
from typing import List, Dict

# Initialize session state for conversation history
if "hf_messages" not in st.session_state:
    st.session_state.hf_messages = []
if "conversation_context" not in st.session_state:
    st.session_state.conversation_context = ""

class HuggingFaceAPI:
    """Simple Hugging Face API client for chat models"""
    
    def __init__(self, api_key: str, model_name: str = "microsoft/DialoGPT-medium"):
        self.api_key = api_key
        self.model_name = model_name
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.headers = {"Authorization": f"Bearer {api_key}"}
    
    def query(self, payload: Dict) -> Dict:
        """Send request to Hugging Face API"""
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"API request failed with status {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}
    
    def generate_response(self, user_input: str, context: str = "") -> str:
        """Generate response using the model"""
        # Prepare input with conversation context
        if context:
            full_input = f"{context}\nHuman: {user_input}\nAssistant:"
        else:
            full_input = f"Human: {user_input}\nAssistant:"
        
        payload = {
            "inputs": full_input,
            "parameters": {
                "max_new_tokens": 150,
                "temperature": 0.7,
                "do_sample": True,
                "top_p": 0.95,
                "repetition_penalty": 1.1,
                "return_full_text": False
            }
        }
        
        result = self.query(payload)
        
        if "error" in result:
            return f"Error: {result['error']}"
        
        if isinstance(result, list) and len(result) > 0:
            generated_text = result[0].get("generated_text", "")
        elif isinstance(result, dict):
            generated_text = result.get("generated_text", "")
        else:
            return "Error: Unexpected response format"
        
        # Clean up the response
        if generated_text:
            # Remove the input part if it's included
            if "Assistant:" in generated_text:
                generated_text = generated_text.split("Assistant:")[-1].strip()
            # Remove Human: parts if they appear
            if "Human:" in generated_text:
                generated_text = generated_text.split("Human:")[0].strip()
        
        return generated_text or "I'm sorry, I couldn't generate a response. Please try again."

class ConversationMemory:
    """Simple conversation memory management"""
    
    def __init__(self, max_turns: int = 5):
        self.max_turns = max_turns
    
    def get_context(self, messages: List[Dict]) -> str:
        """Build conversation context from recent messages"""
        if not messages:
            return ""
        
        # Get last few exchanges
        recent_messages = messages[-self.max_turns*2:] if len(messages) > self.max_turns*2 else messages
        
        context_parts = []
        for msg in recent_messages:
            if msg["role"] == "user":
                context_parts.append(f"Human: {msg['content']}")
            else:
                context_parts.append(f"Assistant: {msg['content']}")
        
        return "\n".join(context_parts)

def initialize_huggingface_client(api_key: str, model_name: str):
    """Initialize Hugging Face API client"""
    try:
        client = HuggingFaceAPI(api_key, model_name)
        return client
    except Exception as e:
        st.error(f"Failed to initialize Hugging Face client: {str(e)}")
        return None

def get_ai_response(client: HuggingFaceAPI, user_input: str, conversation_memory: ConversationMemory) -> str:
    """Get response from Hugging Face API with conversation context"""
    try:
        context = conversation_memory.get_context(st.session_state.hf_messages)
        response = client.generate_response(user_input, context)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Set page configuration
    st.set_page_config(
        page_title="LangChain HuggingFace Chatbot",
        page_icon="🤗",
        layout="wide"
    )
    
    # Main title
    st.title("🤗 Hugging Face API Chatbot")
    st.markdown("Chat with an AI assistant powered by Hugging Face models")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Hugging Face API Token",
            type="password",
            value=os.getenv("HUGGINGFACE_API_TOKEN", ""),
            help="Enter your Hugging Face API token to start chatting"
        )
        
        # Model selection
        model_options = [
            "microsoft/DialoGPT-medium",
            "microsoft/DialoGPT-large",
            "facebook/blenderbot-400M-distill",
            "facebook/blenderbot-1B-distill",
            "google/flan-t5-base",
            "google/flan-t5-large"
        ]
        
        selected_model = st.selectbox(
            "Select Model",
            model_options,
            index=0,
            help="Choose the Hugging Face model for conversation"
        )
        
        # Clear conversation button
        if st.button("Clear Conversation", type="secondary"):
            st.session_state.hf_messages = []
            st.session_state.conversation_context = ""
            st.rerun()
        
        # Display conversation count
        if st.session_state.hf_messages:
            st.info(f"Messages in conversation: {len(st.session_state.hf_messages)}")
        
        # Instructions
        st.markdown("### How to use:")
        st.markdown("1. Enter your Hugging Face API token")
        st.markdown("2. Select a model from the dropdown")
        st.markdown("3. Type your message in the chat input")
        st.markdown("4. Press Enter to send")
        st.markdown("5. Use 'Clear Conversation' to start fresh")
        
        # Model info
        st.markdown("### Model Information:")
        st.markdown(f"**Current Model:** {selected_model}")
        if "DialoGPT" in selected_model:
            st.markdown("DialoGPT: Conversational AI trained on Reddit data")
        elif "blenderbot" in selected_model:
            st.markdown("BlenderBot: Open-domain chatbot from Facebook")
        elif "flan-t5" in selected_model:
            st.markdown("FLAN-T5: Instruction-tuned text-to-text model")
    
    # Check if API key is provided
    if not api_key:
        st.warning("Please enter your Hugging Face API token in the sidebar to start chatting.")
        st.info("You can get your API token from [Hugging Face](https://huggingface.co/settings/tokens)")
        return
    
    # Initialize Hugging Face client
    hf_client = initialize_huggingface_client(api_key, selected_model)
    if not hf_client:
        return
    
    # Initialize conversation memory
    memory = ConversationMemory(max_turns=5)
    
    # Display chat messages
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.hf_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to talk about?"):
        # Add user message to session state
        st.session_state.hf_messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Get response from Hugging Face API
                response = get_ai_response(hf_client, prompt, memory)
                
                # Display response
                st.markdown(response)
        
        # Add assistant response to session state
        st.session_state.hf_messages.append({"role": "assistant", "content": response})
        
        # Rerun to update the chat display
        st.rerun()

if __name__ == "__main__":
    main()
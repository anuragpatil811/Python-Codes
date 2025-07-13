import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
image_path = "/mnt/data/pexels-pixabay-302820.jpg"
image = Image.open(image_path)

# Define a transformation (resize and convert to tensor)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Apply transformation
input_image = transform(image).unsqueeze(0)  # Add batch dimension

# Define a simple CNN model
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 8, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc = nn.Linear(16 * 56 * 56, 2)  # Fully connected layer for classification

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 56 * 56)  # Flatten for FC layer
        x = self.fc(x)
        return x

# Instantiate the model
model = SimpleCNN()

# Pass the image through the CNN (extracting features)
with torch.no_grad():
    output = model(input_image)

print("CNN Output Shape:", output.shape)

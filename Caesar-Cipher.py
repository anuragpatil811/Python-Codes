def caesar(text, shift, char):
    result = " "
    for i in range(len(text)):
        if char.isupper():
            result += chr((ord(char) + shift - 65)% 26 + 65)
        elif char.islower():
            result += char((ord(char) + shift - 97)% 26 + 97)
        else:
            result += char
    return result
text = input("Enter a string:")
shift  = int(input("Enter frequency:"))
encrypted_message = caesar(text, shift)
print("Encrypted text: ", encrypted_message)

import clipboard

def text_to_binary(text):
    """Convert text to a binary string using UTF-8 encoding."""
    return ''.join(format(byte, '08b') for byte in text.encode('utf-8'))

def shift_binary(binary, shift):
    """Shift the binary string by the given shift amount."""
    return binary[-shift:] + binary[:-shift]

def encrypt(text, shift):
    binary_text = text_to_binary(text)
    shifted_binary = shift_binary(binary_text, shift)
    return shifted_binary
plain_text = input("PlainText: ")
print(text_to_binary(plain_text))
shift_value = int(input("Key: ")) % 7 + 1

encrypted_binary = encrypt(plain_text, shift_value)
clipboard.copy(encrypted_binary)
print(f"Encrypted: {encrypted_binary}")
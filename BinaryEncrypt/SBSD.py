import os
from PIL import Image

def binary_to_message(binary_data):
    """Convert binary data to a string message using UTF-8 decoding."""
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message_bytes = bytearray([int(byte, 2) for byte in all_bytes])
    message = message_bytes.decode('utf-8', errors='ignore')
    return message

def extract_message(image_path):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    image = Image.open(image_path)
    binary_data = ''
    pixels = list(image.getdata())

    for pixel in pixels:
        for i in range(3):
            binary_data += str(pixel[i] & 1)

    delimiter = '1111111111111110'
    binary_message = binary_data.split(delimiter)[0]
    message = binary_to_message(binary_message)
    return message

def binary_to_text(binary_data):
    """Convert binary string to text using UTF-8 decoding."""
    byte_list = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    byte_array = bytearray(int(byte, 2) for byte in byte_list)
    return byte_array.decode('utf-8', errors='ignore')

def reverse_shift_binary(binary, shift):
    """Reverse the shift operation on the binary string."""
    return binary[shift:] + binary[:shift]

def decrypt(encrypted_binary, shift):
    shifted_binary = reverse_shift_binary(encrypted_binary, shift)
    binary_text = binary_to_text(shifted_binary)
    return binary_text

filename = input("FileName: ")
hidden_message = extract_message(filename)
encrypted = hidden_message
shift_value = int(input("Key: "))
if shift_value < 1 or shift_value > 7:
    shift_value = shift_value % 7 + 1

decrypted = decrypt(encrypted, shift_value)
print(f"Decrpted(PlainText): {decrypted}")
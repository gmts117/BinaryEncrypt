import clipboard
import os
from PIL import Image

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

def message_to_binary(message):
    """Convert a string message to binary using UTF-8 encoding."""
    binary_message = ''.join(format(byte, '08b') for byte in message.encode('utf-8'))
    return binary_message

def hide_message(image_path, message, output_image_path):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    image = Image.open(image_path)
    binary_message = message_to_binary(message) + '1111111111111110'  # End of message delimiter
    binary_index = 0

    pixels = list(image.getdata())
    new_pixels = []

    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Assuming an RGB image
            if binary_index < len(binary_message):
                new_pixel[i] = (new_pixel[i] & 254) | int(binary_message[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)
    image.save(output_image_path)

plain_text = input("PlainText: ")
shift_value = int(input("Key: "))
if shift_value < 1 or shift_value > 7:
    shift_value = shift_value % 7 + 1
filename = input("FileName: ")
encrypted_binary = encrypt(plain_text, shift_value)
#clipboard.copy(encrypted_binary)
hide_message(filename, encrypted_binary, f'encrypted{filename}')
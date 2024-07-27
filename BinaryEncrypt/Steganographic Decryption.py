from PIL import Image

def binary_to_message(binary_data):
    """Convert binary data to a string message using UTF-8 decoding."""
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message_bytes = bytearray([int(byte, 2) for byte in all_bytes])
    message = message_bytes.decode('utf-8', errors='ignore')
    return message

def extract_message(image_path):
    image = Image.open(image_path)
    binary_data = ''
    pixels = list(image.getdata())

    for pixel in pixels:
        for i in range(3):  # Assuming an RGB image
            binary_data += str(pixel[i] & 1)

    delimiter = '1111111111111110'
    binary_message = binary_data.split(delimiter)[0]
    message = binary_to_message(binary_message)
    return message


hidden_message = extract_message('output_image.png')
print("추출된 메시지:", hidden_message)

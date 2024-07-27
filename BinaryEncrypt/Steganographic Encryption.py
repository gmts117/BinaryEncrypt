from PIL import Image

def message_to_binary(message):
    """Convert a string message to binary using UTF-8 encoding."""
    binary_message = ''.join(format(byte, '08b') for byte in message.encode('utf-8'))
    return binary_message

def hide_message(image_path, message, output_image_path):
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


message = input("숨기고 싶은 문자열: ")
hide_message('피카츄.png', message, 'output_image.png')

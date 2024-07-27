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

encrypted = input("Encrypted: ")
shift_value = int(input("Key: "))

decrypted = decrypt(encrypted, shift_value)
print(f"Decrpted(PlainText): {decrypted}")
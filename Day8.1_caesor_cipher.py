def caesar_cipher_encode(plaintext, shift):
    """
    Encodes the plaintext using Caesar Cipher with a given shift.
    
    :param plaintext: The string to encode.
    :param shift: The number of positions to shift each letter in the alphabet.
    :return: The encoded string (ciphertext).
    """
    ciphertext = []
    
    for char in plaintext:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and ensure it stays within alphabet bounds
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext.append(shifted_char)
        else:
            # Non-alphabetical characters are not changed
            ciphertext.append(char)
    
    return ''.join(ciphertext)


def caesar_cipher_decode(ciphertext, shift):
    """
    Decodes the ciphertext using Caesar Cipher with a given shift.
    
    :param ciphertext: The string to decode.
    :param shift: The number of positions to shift each letter in the alphabet.
    :return: The decoded string (plaintext).
    """
    plaintext = []
    
    for char in ciphertext:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Reverse the shift for decoding
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext.append(shifted_char)
        else:
            # Non-alphabetical characters are not changed
            plaintext.append(char)
    
    return ''.join(plaintext)


def main():
    while True:
        # Ask the user what they want to do
        action = input("Do you want to (e)ncode or (d)ecode a message? (e/d): ").lower()
        
        if action == 'e':
            plaintext = input("Enter the message you want to encode: ")
            shift_value = int(input("Enter the shift value: "))
            encoded_text = caesar_cipher_encode(plaintext, shift_value)
            print(f"Encoded message: {encoded_text}")
        elif action == 'd':
            ciphertext = input("Enter the message you want to decode: ")
            shift_value = int(input("Enter the shift value: "))
            decoded_text = caesar_cipher_decode(ciphertext, shift_value)
            print(f"Decoded message: {decoded_text}")
        else:
            print("Invalid option! Please choose 'e' to encode or 'd' to decode.")

        # Ask if the user wants to continue
        continue_choice = input("Do you want to continue? (y/n): ").lower()
        if continue_choice != 'y':
            print("Goodbye!")
            break

# Run the main function to start the program
if __name__ == "__main__":
    main()

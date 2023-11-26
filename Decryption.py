import cv2
import numpy as np

def decode_text(encrypted_image_path, output_text_path):
    # Read the encrypted image
    encrypted_image = cv2.imread(encrypted_image_path)

    # Get the image height and width
    height, width = encrypted_image.shape[:2]

    # Extract the binary text from the image
    binary_text = ""
    for row in encrypted_image:
        for pixel in row:
            binary_text += str(pixel[0] & 1)

    # Convert the binary text to a list of integers
    binary_text_list = [int(binary_text[i:i+8], 2) for i in range(0, len(binary_text), 8)]

    # Convert the list of integers to ASCII characters
    text = "".join([chr(char) for char in binary_text_list])

    # Save the decrypted text
    with open(output_text_path, 'w') as f:
        f.write(text)
    '''print("The decrypted file has been successfully created. Kindly check the entered location.\n")'''

# Example usage
encrypted_image_path = input("Enter the encrypted image path: \n")
output_text_path = input("Enter the output text path and name to be saved after decryption: \n")

decode_text(encrypted_image_path, output_text_path)

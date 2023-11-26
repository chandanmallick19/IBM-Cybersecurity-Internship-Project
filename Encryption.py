import cv2
import numpy as np

def encode_text(image_path, text_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the text to binary
    binary_text = "".join([bin(ord(char))[2:] for char in open(text_path, 'r').read()])

    # Get the image height and width
    height, width = image.shape[:2]

    # Check if the image is large enough to hold the text
    if len(binary_text) > (width * height * 3):
        raise ValueError("Image is not large enough to hold the text")

    # Convert the binary text to a list of integers
    binary_text_list = [int(binary_text[i:i+8], 2) for i in range(0, len(binary_text), 8)]

    # Embed the binary text into the image
    i = 0
    for row in image:
        for pixel in row:
            if i < len(binary_text_list):
                pixel[0] = pixel[0] & ~1 | binary_text_list[i] & 1
                i += 1

    # Save the encrypted image
    cv2.imwrite(output_path, image)
    print("The encrypted file has been successfully created. Kindly check the entered location.\n")

# Example usage
image_path = input("Enter the original image path: \n")
text_path = input("Enter the text file path which is to be encrypted: \n")
output_path = input("Enter the encrypted image path and name to be saved after encryption: \n")

encode_text(image_path, text_path, output_path)

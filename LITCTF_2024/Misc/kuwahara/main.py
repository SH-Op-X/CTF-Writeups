"""
Problem Statement:

Here, you have an encryption method based on the Kuwahara Algorithm.
You're also given some images and a message that was encoded using this method.
Your task is to decode the message and find the flag.
"""

import numpy as np
import cv2
from encoder import encode, decode

def kuwahara(original_image, window_size):
    """
    Kuwahara Algorithm. This function applies the Kuwahara algorithm to an image.
    More specifically, it runs the average based filter on the image,
    going over each pixel, putting 4 windows of window_size x window_size each
    having a different offset from the pixel, and then calculating the average
    and standard deviation of the pixel values in the window.
    
    Args:
        original_image (ndarray): The original image to apply the Kuwahara algorithm to.
        window_size (int): The size of the window used for calculating the local statistics.

    Returns:
        tuple: A tuple containing the following elements:
            - averages (ndarray): An array of shape (4, H, W, C)
                                containing the average values for each subregion.
            - stddevs (ndarray): An array of shape (4, H, W)
                                containing the standard deviations for each subregion.
    """
    # Your code here
    return None, None

def kuwahara_encryption(original_image, message, window_size=5):
    """
    Applies the Kuwahara algorithm to an original image and encrypts a message within it.

    Parameters:
    - original_image (ndarray): The original image to be processed.
    - message (str): The message to be encrypted within the image.
    - window_size (int): The size of the window used in the Kuwahara algorithm. Default is 5.

    Returns:
    - ndarray: The filtered image with the encrypted message.
    """
    averages, stddevs = kuwahara(original_image, window_size)

    # Might not give them these two, might give them...
    indices = np.argmin(stddevs, axis=0)
    sorted_indices = np.argsort(stddevs, axis=0)

    # Start at (window_size, window_size) to avoid the border, where
    # the Kuwahara Algorithm might not get enough pixels.
    start_x = start_y = window_size
    for m in message:
        indices[start_x][start_y] = sorted_indices[m][start_x][start_y]
        start_y += 1
        if start_y == original_image.shape[1] - window_size:
            start_y = window_size
            start_x += 1

    # Second favorite function when writing this, take_along_axis. Epic.
    filtered = np.take_along_axis(averages, indices[None,...,None], 0).reshape(original_image.shape)
    return filtered.astype(original_image.dtype)

def kuwahara_decryption(original_image, enc_image, window_size=5):
    """
    Decodes an encoded image using the Kuwahara algorithm.

    Parameters:
    original_image (ndarray): The original image used for encoding.
    enc_image (ndarray): The encoded image to be decoded.
    window_size (int, optional): The size of the window used
                                for the Kuwahara algorithm. Default is 5.

    Returns:
    list: The original message from the encoded image.
    """
    return [] # Your code here

# Below code is what I did to the image:
"""
# ENCRYPTION:

# Load the noisy image
input_image = cv2.imread('img/noisy_image.jpg')
flag = [enc + 1 for enc in encode("FLAG", 3)] # FLAG encoded with base 3, plus 1 to ensure offsets are always found.

encoded_image = kuwahara_encryption(input_image, flag)
cv2.imwrite('img/encoded_image.jpg', encoded_image)
"""

# DECRYPTION:
input_image = cv2.imread('img/noisy_image.jpg')
encoded_image = cv2.imread('img/encoded_image.jpg')

decoded_indices = kuwahara_decryption(input_image, encoded_image)

final_message = decode([dec - 1 for dec in decoded_indices], 3)
print("Flag: ", final_message)

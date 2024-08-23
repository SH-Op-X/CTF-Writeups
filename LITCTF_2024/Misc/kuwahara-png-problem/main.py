"""
Problem Statement:

Here, you have an encryption method based on the Kuwahara Algorithm.
You're also given some images and a message that was encoded using this method.
Your task is to decode the message and find the flag.
"""

import numpy as np
from cv2 import cvtColor, COLOR_BGR2GRAY, sepFilter2D, imread, imwrite
from encoder import encode, decode

def kuwahara(original_image, window_size):
    """
    Kuwahara Algorithm. This function applies the Kuwahara algorithm to an image.
    More specifically, it runs the average based filter on the image,
    going over each pixel, putting 4 windows of window_size x window_size each
    having the original pixel as a corner, and then calculating the
    standard deviation of these regions (in grayscale). Then, set the color
    of the pixel to the color average of the region with the lowest standard deviation.
    
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
    # convert to float32 if necessary for further math computation
    image = original_image.astype(np.float32, copy=False)
    radius = (window_size - 1) // 2
    # preallocate these arrays
    avgs = np.empty((4, *image.shape), dtype=image.dtype)
    stddevs = np.empty((4, *image.shape[:2]), dtype=image.dtype)

    if image.ndim == 3:
        image_2d = cvtColor(original_image, COLOR_BGR2GRAY).astype(image.dtype, copy=False)
        avgs_2d = np.empty((4, *image.shape[:2]), dtype=image.dtype)
    elif image.ndim == 2:
        image_2d = image
        avgs_2d = avgs

    # Create a pixel-by-pixel square of the image
    squared_img = image_2d ** 2

    kxy = np.ones(radius + 1, dtype=image.dtype) / (radius + 1)  # kernelX and kernelY (same)

    # the pixel position for all kernel quadrants
    shift = [(0, 0), (0, radius), (radius, 0), (radius, radius)]

    # Calculation of averages and variances on subwindows
    for k in range(4):
        kx = ky = kxy
        sepFilter2D(image, -1, kx, ky, avgs[k], shift[k])
        if image.ndim == 3:  # else, this is already done...
            sepFilter2D(image_2d, -1, kx, ky, avgs_2d[k], shift[k])
        sepFilter2D(squared_img, -1, kx, ky, stddevs[k], shift[k])
        stddevs[k] = stddevs[k] - avgs_2d[k] ** 2  # compute the final variance on subwindow

    # Choice of index with minimum variance
    indices = np.argmin(stddevs, axis=0)

    # Building the filtered image
    if image.ndim == 2:
        filtered = np.take_along_axis(avgs, indices[None, ...], 0).reshape(image.shape)
    else:  # then avgs.ndim == 4
        filtered = np.take_along_axis(avgs, indices[None, ..., None], 0).reshape(image.shape)

    return avgs, stddevs


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
    averages, stddevs = kuwahara(original_image, window_size)

    # Might not give them these two, might give them...
    indices = np.argmin(stddevs, axis=0)
    sorted_indices = np.argsort(stddevs, axis=0)

    # Start at (window_size, window_size) to avoid the border, where
    # the Kuwahara Algorithm might not get enough pixels.
    start_x = start_y = window_size

    enc_image = enc_image.reshape(1, enc_image.shape[0], enc_image.shape[1], enc_image.shape[2])
    # Second favorite function when writing this, take_along_axis. Epic.
    filtered = np.take_along_axis(averages, indices[None, ..., None], 0).astype(original_image.dtype)

    message = [enc + 1 for enc in encode("FLAG", 3)]
    for m in message:
        indices[start_x][start_y] = sorted_indices[m][start_x][start_y]
        start_y += 1
        if start_y == original_image.shape[1] - window_size:
            start_y = window_size
            start_x += 1

    return filtered.astype(original_image.dtype)

# Below code is what I did to the image:
# """
# ENCRYPTION:

# Load the noisy image
# input_image = imread('img/noisy_image.png')
# flag = [enc + 1 for enc in encode("FLAG", 3)] # FLAG encoded with base 3, plus 1 to ensure offsets are always found.
#
# encoded_image = kuwahara_encryption(input_image, flag)
# imwrite('img/encoded_image1.png', encoded_image)
# """

# DECRYPTION:
input_image = imread('img/noisy_image.png')
encoded_image = imread('img/encoded_image1.png')

decoded_indices = kuwahara_decryption(input_image, encoded_image)

final_message = decode([dec - 1 for dec in decoded_indices], 3)
print("Flag: ", final_message)

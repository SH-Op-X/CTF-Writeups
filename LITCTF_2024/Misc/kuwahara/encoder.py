"""
This module contains functions to encode a message into a single number.
You shouldn't need to modify this file to solve the CTF. 
If you're interested in how the encoding works, you can read the code.
"""

from math import ceil, log
from string import ascii_lowercase, ascii_uppercase, digits
from random import randint

CHARACTERS = " _{}" + f"{ascii_lowercase}{ascii_uppercase}{digits}"
BASE = 10

def generate_table(base=BASE, characters=CHARACTERS):
    """
    Generate an encoder and decoder table for a given base and set of characters.

    Parameters:
    - base (int): The base used for encoding.
    - characters (str): The set of characters to be encoded.

    Returns:
    - encoder (dict): A dictionary mapping characters to their encoded values.
    - decoder (dict): A dictionary mapping encoded values to their characters.
    """
    encoder = {}
    decoder = {}
    k = ceil(log(len(characters) / (base - 1), base)) + 1

    for i, ch in enumerate(characters):
        encoder[ch] = base ** k + i
        decoder[base ** k + i] = ch

    return encoder, decoder

def number_to_base(num, base=BASE):
    """
    Converts a decimal number to a list of digits in a given base.

    Parameters:
    - n (int): The decimal number to convert.
    - b (int): The base to convert the number to. Default is 4.

    Returns:
    - list: A list of digits representing the decimal number in the given base.
    """
    if num == 0:
        return [0]
    num_digits = []
    while num:
        num_digits.append(int(num % base))
        num //= base
    return num_digits[::-1]

def convert_from(num, base=BASE):
    """
    Converts a number from a given base to decimal.

    Parameters:
    n (list): A list of digits representing the number in the given base.
    b (int): The base of the number. Default is 4.

    Returns:
    int: The decimal representation of the number.

    Example:
    >>> convert_from([1, 0, 1, 1], 2)
    11
    """
    s = 0
    for i, d in enumerate(num[::-1]):
        s += base**i * d
    return s

def encode(message, base=BASE, characters=CHARACTERS):
    """
    Encodes a given message using a specified base and character set.

    Args:
        message (str): The message to be encoded.
        b (int, optional): The base to be used for encoding. Defaults to BASE.
        characters (str, optional): The character set to be used for encoding.
                                    Defaults to CHARACTERS.

    Returns:
        list: A list of integers representing the encoded message.

    Raises:
        ValueError: If the message contains characters not present in the character set.
    """
    encoder, _ = generate_table(base, characters)
    if not set(message).issubset(set(characters)):
        raise ValueError('`message` cannot contain any other characters.')
    nums = map(lambda x: encoder[x], message)
    seq = []
    for num in nums:
        seq += number_to_base(num, base)
    return seq

def decode(encoded, base=BASE, characters=CHARACTERS):
    """
    Decodes a given list of integers using a specified base and character set.

    Args:
        encoded (list): A list of integers representing the encoded message.
        b (int, optional): The base to be used for decoding. Defaults to BASE.
        characters (str, optional): The character set to be used for decoding.
                                    Defaults to CHARACTERS.

    Returns:
        str: The decoded message.

    Raises:
        ValueError: If the encoded message contains integers not present in the encoder table.
    """
    _, decoder = generate_table(base, characters)
    seq = ""
    k = ceil(log(len(characters)/(base - 1), base)) + 1
    for i in range(0, len(encoded), k+1):
        num = encoded[i:i+k+1]
        conv = convert_from(num, base)
        seq += decoder[conv]
    return seq

if __name__ == "__main__":
    # Random tests
    for n in range(1, 1000):
        b = randint(2, 100)
        assert convert_from(number_to_base(n, b), b) == n
        assert decode(encode(str(n), b), b) == str(n)
    # Base tests
    assert decode(encode('hello world')) == 'hello world'
    assert decode(encode("""picoCTF{HELLO}""")) == """picoCTF{HELLO}"""

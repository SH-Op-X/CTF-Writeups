custom_b64_chars = "TUVWXYZabcdefghijABCDEF456789GHIJKLMNOPQRSklmnopqrstuvwxyz0123+/"
char_to_index = {char: idx for idx, char in enumerate(custom_b64_chars)}


def decode_custom_base64(encoded_str):
    encoded_str = encoded_str.rstrip('=')
    bit_stream = []
    for char in encoded_str:
        if char in char_to_index:
            bit_stream.append(char_to_index[char])
        else:
            raise ValueError(f"Invalid character: {char}")
    decoded_bytes = []
    for i in range(0, len(bit_stream), 4):
        chunk = bit_stream[i:i + 4]
        if len(chunk) < 4:
            chunk += [0] * (4 - len(chunk))
        byte1 = (chunk[0] << 2) | (chunk[1] & 3)
        byte2 = ((chunk[1] >> 2) << 4) | (chunk[2] & 0xf)
        byte3 = ((chunk[2] >> 4) << 6) | chunk[3]
        decoded_bytes.extend([byte1^1, byte2^1, byte3^1])
    padding_length = encoded_str.count('=')
    if padding_length:
        decoded_bytes = decoded_bytes[:-padding_length]
    return bytes(decoded_bytes)


encoded_str = b"RPVIRN40R9PU67ue6RUH88Rgs65Bp8td8VQm4SPAT8Kj97QgVG=="
encoded_str1 = ""
for i in encoded_str:
    if i in range(ord("A"), ord("M")+1):
        encoded_str1 += chr(i+13)
    elif i in range(ord("M")+1, ord("Z")+1):
        encoded_str1 += chr(i-13)
    elif i in range(ord("a"), ord("m")+1):
        encoded_str1 += chr(i+13)
    elif i in range(ord("m")+1, ord("z")+1):
        encoded_str1 += chr(i-13)
    else:
        encoded_str1 += chr(i)
decoded_data = decode_custom_base64(encoded_str1)
print(decoded_data)
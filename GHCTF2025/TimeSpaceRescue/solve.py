def xor5(a):
    a = list(a)
    for i in range(0, len(a), 2):
        a[i] ^= 5
        a[i + 1] ^= 5
        a[i], a[i + 1] = a[i + 1], a[i]
    return bytes(a)

def xorf(p):
    p = list(p)
    for i in range(0, len(p), 16):
        for j in range(8):
            p[i + j] ^= 15
            p[i + 15-j] ^= 15
            p[i + j], p[i + 15-j] = p[i + 15-j], p[i + j]
    return bytes(p)


import hashlib
from Crypto.Cipher import AES

# Function to calculate MD5 hash
def calculate_md5(data):
    return hashlib.md5(data).digest()

# Function to decrypt AES-128 using a given key and ciphertext
def aes_decrypt(key, ct):
    key = xor5(key)
    ct = xor5(ct)
    cipher = AES.new(key, AES.MODE_ECB)
    plain = cipher.decrypt(ct)
    plain = xorf(plain)
    return plain

# Function to simulate C code's AES decryption
def decrypt_ct(ct):
    # Iterate over each month in 2024
    for month in range(12):
        days_in_month = get_days_in_month_2024(month)
        # Iterate over each day in the month
        for day in range(1, days_in_month + 1):
            # Create the time data for the current day, month, and year (2024)
            time_data = bytearray(12)
            time_data[0:4] = day.to_bytes(4, byteorder='little')
            time_data[4:8] = month.to_bytes(4, byteorder='little')
            time_data[8:12] = (2024 - 1900).to_bytes(4, byteorder='little')

            # Calculate the MD5 hash of the time data
            md5_hash = calculate_md5(time_data)

            # Generate AES key by XORing MD5 hash with 0x14 byte-by-byte
            aes_key = bytes([md5_hash[i] ^ 5 for i in range(16)])

            # Decrypt the ciphertext with the generated AES key
            decrypted = aes_decrypt(aes_key, ct)
            if is_printable(decrypted):
                print(f"Date: 2024-{month+1:02d}-{day:02d}")
                print(decrypted)


# Helper function to get the number of days in a month for 2024
def get_days_in_month_2024(month):
    # Months with 31 days
    if month in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    # Months with 30 days
    elif month in [3, 5, 8, 10]:
        return 30
    # February 2024 has 29 days (since 2024 is a leap year)
    else:
        return 29

def is_printable(data):
    return all(32 <= byte <= 126 for byte in data)

# Main execution
if __name__ == "__main__":
    # Given ciphertext
    ct = bytes([
        0xCD, 0x16, 0xDB, 0xB5, 0xD1, 0x02, 0xA4, 0x82,
        0x8E, 0x59, 0x73, 0x9E, 0x96, 0x26, 0x56, 0xF2,
        0x16, 0x8E, 0x46, 0xF2, 0x55, 0x7B, 0x92, 0x31,
        0x30, 0xDC, 0xAA, 0x8A, 0xF3, 0x1C, 0xA0, 0xAA
    ])

    decrypt_ct(ct)

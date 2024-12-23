from Crypto.Cipher import AES

with open("aes_enc", "rb") as f:
    data = f.read()

dec_result = [b""] * 961
dec_result[565] = b"9fc82e15d9de6ef2"
visited = [0] * 961

def decrypt(ciphertext, key):
    aes = AES.new(key, mode=AES.MODE_ECB)
    ciphertext = list(ciphertext)
    for i in range(len(ciphertext)):
        ciphertext[i] ^= key[i&0xf] ^ (i%32)
    new_result = []
    for i in range(0, len(ciphertext), 32):
        result = aes.decrypt(bytes(ciphertext[i:i+32]))
        try:
            key = result.split(b'"')[1]
            index = int(result.split(b'_')[2].decode())
            dec_result[index] = key
            new_result.append((index, key))
        except:
            print(result)
    return new_result


def bfs(result):
    if b"" not in dec_result:
        return
    new_result = []
    for i in range(len(result)):
        index = result[i][0]
        key = result[i][1]
        if visited[index] == 1:
            continue
        if index != 0:
            new_result += decrypt(data[-(index * 128 + 128):-(index * 128)], key)
        else:
            new_result += decrypt(data[-(index * 128 + 128):], key)
        visited[index] = 1
    if len(new_result) == 0:
        return
    bfs(new_result)


bfs([(565, b"9fc82e15d9de6ef2")])
print(dec_result)
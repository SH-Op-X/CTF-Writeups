from scipy.io import wavfile

samplerate, data = wavfile.read('public.wav')
flag = ""
for i in range(0, len(data), 44):
    if data[i] == 32767:
        flag += "1"
    elif data[i] == -32767:
        flag += "0"
# print(flag, len(flag)/7)

# flag = "".join(["1" if flag[i:i+2] == "10" else "0" for i in range(0, len(flag), 2)])
# print(flag, len(flag)/8)

flag = "".join(["0" if flag[i:i+2] == "10" else "1" for i in range(0, len(flag), 2)])
print("".join([chr(int(flag[i:i+8], 2)) for i in range(0, len(flag), 8)]))
# print("".join(map(lambda x: chr(int(x, 2)), [flag[i:i+8] for i in range(0, len(flag), 8)])))
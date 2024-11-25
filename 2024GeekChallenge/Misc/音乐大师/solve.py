import wave

f = wave.open("secret.wav", "r")
frame = f.readframes(f.getnframes())
f1 = wave.open("00000758.wav", "r")
frame1 = f1.readframes(f.getnframes())
print(len(frame)==len(frame1), len(frame), len(frame1))
diff = []
for i in range(len(frame1)):
    diff.append(frame[i]^frame1[i])
j = -1
while diff[j] == 0:
    j -= 1
print(j)
print(diff[:j])
print("".join(map(chr,diff[:j])))
# print(list(map(lambda x: x&0xff, diff[:j])))
# print(frame[len(frame1):])

# import scipy.io.wavfile as wavfile

# samplerate, data = wavfile.read('combine.wav')
# print(samplerate, data)
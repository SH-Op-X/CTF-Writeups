with open("Dusk_witnesses_devout_believers.gif", "rb") as f:
    data = f.read()
new_data = b""
s = "qwertyuiopasdfgh"
print(len(s))
for i in range(0, len(data)):
    new_data += (data[i]^ord(s[i%len(s)])).to_bytes(1,'big')
with open("out.gif", "wb") as f1:
    f1.write(new_data)
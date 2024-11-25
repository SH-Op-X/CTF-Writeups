s = "0A161230300C2D0A2B303D2428233005242C2D26182206233E097F133A"
s = list(bytes.fromhex(s))
key = "GEEK"
for i in range(len(s)):
	s[i] ^= ord(key[i%4])
for i in range(len(s)):
	if chr(s[i]).islower():
		s[i] = chr((s[i] - 97 - 20) % 26 + 97)
	elif chr(s[i]).isupper():
		s[i] = chr((s[i] - 65 - 20) % 26 + 65)
	elif chr(s[i]).isdigit():
		s[i] = chr((s[i] - 48 - 20) % 10 + 48)
	else:
		s[i] = chr(s[i])
print("".join(s))


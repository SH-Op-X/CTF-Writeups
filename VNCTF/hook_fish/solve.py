s = "jjjliijijjjjjijiiiiijijiijjiijijjjiiiiijjjjliiijijjjjljjiilijijiiiiiljiijjiiliiiiiiiiiiiljiijijiliiiijjijijjijijijijiilijiijiiiiiijiljijiilijijiiiijjljjjljiliiijjjijiiiljijjijiiiiiiijjliiiljjijiiiliiiiiiljjiijiijiijijijjiijjiijjjijjjljiliiijijiiiijjliijiijiiliiliiiiiiljiijjiiliiijjjliiijjljjiijiiiijiijjiijijjjiiliiliiijiijijijiijijiiijjjiijjijiiiljiijiijilji"
ij_dict = {"iiijj": "a",
    "jjjii": 'b',
"jijij": 'c',
"jjijj": 'd',
"jjjjj": 'e',
"ijjjj": 'f',
"jjjji": 'g',
"iijii": 'h',
"ijiji": 'i',
"iiiji": 'j',
"jjjij": 'k',
"jijji": 'l',
"ijiij": 'm',
"iijji": 'n',
"ijjij": 'o',
"jiiji": 'p',
"ijijj": 'q',
"jijii": 'r',
"iiiii": 's',
"jjiij": 't',
"ijjji": 'u',
"jiiij": 'v',
"iiiij": 'w',
"iijij": 'x',
"jjiji": 'y',
"jijjj": 'z',
"iijjl": '1',
"iiilj": '2',
"iliii": '3',
"jiili": '4',
"jilji": '5',
"iliji": '6',
"jjjlj": '7',
"ijljj": '8',
"iljji": '9',
"jjjli": '0'}
c = ""
for i in range(0, len(s), 5):
    c += ij_dict[s[i:i+5]]
print(c)
c = list(c.encode())
for i in range(len(c)):
    if c[i] > 55:
        c[i] -= (i % 10 + 55)
    else:
        c[i] += (49 - i % 4)
for i in range(0, len(c), 2):
    c[i], c[i+1] = c[i+1], c[i]
new_c = bytes.fromhex(bytes(c).decode())
for i in range(len(new_c)):
    print(chr(new_c[i]-68), end="")
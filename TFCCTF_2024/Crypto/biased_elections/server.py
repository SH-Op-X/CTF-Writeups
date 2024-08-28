from ecdsa import ellipticcurve
from ecdsa.ecdsa import curve_256, generator_256, Public_key, Private_key
import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes,bytes_to_long

FLAG = b'TFCCTF{REDACTED}'
G = generator_256
order = G.order()
rand = random.randint(1,order-1)
pubkey = Public_key(G, rand*G)
privkey = Private_key(pubkey, rand)



messages = [
    "Ensure the ballots are ready for the biased count.",
    "The first batch of votes is in. Proceed as planned.",
    "Secure the communications. We can't risk exposure.",
    "Start the rigging process at midnight tonight.",
    "All systems are go. Confirm the final preparations.",
    "Intercepted some chatter. Maintain radio silence.",
    "Verification complete. Everything is on track.",
    "Monitor the vote counts closely. Report any issues.",
    "We've gained access. Execute the next step."
]

def the_random():
    def very_random(length):
        return ''.join(chr((l(a, b, m) % 94) + 33) for _ in range(length))
    
    def l(a, b, m):
        nonlocal x
        result = (a * x + b) % m
        x = result
        return result
    
    a = 6364136223846793005
    b = 1
    m = 2 ** 64
    x = random.getrandbits(64)

    r = very_random(128)
    
    g = very_random(256)
    h = very_random(256)
    j = ''.join(chr((ord(k) ^ ord(l)) % 256) for k, l in zip(g, h))
    k = hashlib.sha256(r.encode() + j.encode()).hexdigest()
    n = ''.join(chr((ord(o) ^ ord(p)) % 256) for o, p in zip(j, k))
    o = hashlib.md5(n.encode() + k.encode()).hexdigest()
    p = hashlib.sha1(o.encode() + k.encode()).hexdigest()
    q = int(p[:40], 16)
    
    aes_key = very_random(16).encode('utf-8')
    aes_iv = very_random(16).encode('utf-8')
    aes_cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    aes_data = pad((p[:32] + o[:32]).encode('utf-8'), AES.block_size)
    aes_encrypted = aes_cipher.encrypt(aes_data)
    z = int(hashlib.sha256(aes_encrypted).hexdigest()[:40], 16)

    result = q ^ (z >> 5)
    return result & ((1 << random.randint(170,200)) - 1)

def sign_message(message):
    hsh = hashlib.sha256(message.encode()).digest()
    nonce = the_random()
    sig = privkey.sign(bytes_to_long(hsh), nonce)
    return {"hash": bytes_to_long(hsh), "r": hex(sig.r), "s": hex(sig.s)}

max_used = 10
used = 0
print('What do you want to do?')
print('1. Listen in on conversation')
print('2. Submit the info you found')
print('3. Get pubkey')
while True:
    data = input()

    if data == '1':
        if used > max_used:
            print('Intruder spotted, deleting secrets.')
            exit()

        message = messages[random.randint(0,len(messages)-1)]
        print(sign_message(message))
        used+=1

    if data == '2':
        key = int(input('Key? '))

        if key == rand:
            print('Thanks bro here is a flag for your effort')
            print(FLAG)

    if data == '3':
        print(f'Public key: {int(pubkey.point.x())} {int(pubkey.point.y())}')
from hashlib import sha1
from Crypto.Util.number import bytes_to_long
from ecdsa.ecdsa import Public_key, Private_key, Signature, generator_192
from datetime import datetime
from random import randrange


banner = """                                                
    //   / /     //   ) )     //    ) )     //   ) )     // | | 
   //____       //           //    / /     ((           //__| | 
  / ____       //           //    / /        \\         / ___  | 
 //           //           //    / /           ) )    //    | | 
//____/ /    ((____/ /    //____/ /     ((___ / /    //     | |  

Welcome to the SCUCTF 2024 challenge!
you have THREE choices:
- sign_time to get a signature
- verify to verify the signature
- I kown the secret to get the flag
You only have TWO chances per connection. Best wish for you!
"""

g = generator_192
n: int = g.order()
hint = b'**************'
flag = b'**************'
secret = randrange(1, n-1)
class Challenge():
    def __init__(self):
        self.secret =  secret
        self.pubkey = Public_key(g, g * self.secret)
        self.privkey = Private_key(self.pubkey, self.secret)

    def sign_time(self):
        now: datetime = datetime.now()
        m: int = int(now.strftime("%m"))
        n: int = int(now.strftime("%S"))
        current: str = f"{m}:{n}"
        msg: str = f"The time is {current}"
        hsh: bytes = sha1(msg.encode()).digest()
        sig: Signature = self.privkey.sign(bytes_to_long(hsh), randrange(100, 100+n))
        return {"time": msg, "r": hex(sig.r), "s": hex(sig.s)}
    

    def verify(self):
        msg: str = input("Enter the message: ")
        r: str = input("Enter r in hexadecimal form: ")
        s: str = input("Enter s in hexadecimal form: ")
        hsh: bytes = sha1(msg.encode()).digest()
        sig_r: int = int(r, 16)
        sig_s: int = int(s, 16)
        sig: Signature = Signature(sig_r, sig_s)
        return self.pubkey.verifies(bytes_to_long(hsh), sig)

    def challenge(self):
        print(banner)
        for _ in range(2):
            option: str = input("Enter your option: ")
            if option == 'sign_time':
                print(self.sign_time())
            elif option == 'verify':
                if self.verify():
                    print(f"The hint is: {hint}")
                    exit(0)
                else:
                    print("Invalid signature!")
            elif option == 'I kown the secret':
                if input("Enter the secret: ") == hex(secret):
                    print(f"The flag is: {flag}")
                    exit(0)
            else:
                print("Invalid option!")
        exit(0)


if __name__ == "__main__":
    c: Challenge = Challenge()
    c.challenge()

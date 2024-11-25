import socketserver
import signal
from Crypto.Cipher import AES


KEY = b'...'
FLAG = b'SYC{...}'

def encrypt(key, plaintext):
    plaintext = padding(plaintext)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)

def padding(m):
    if (len(m) % 16 != 0):
        m = m + b'F' * (16 - (len(m) % 16))
    return m
class Serve(socketserver.BaseRequestHandler):

    ctry = 0
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass
        
    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        return self._recvall()

    def handle(self):
        try:
            go = 1
            signal.alarm(3000)
            self.send(b'Welcome to the AES_ECB Cryptography System')
            self.send(b'You can send your plaintext and get ciphertext')
            self.send(b'[+] ciphertext = plaintext + FLAG')
            self.send(b'Start?(yes/no)')
            while go:
                c = self.recv()
                if c == b'yes':
                    plain = self.recv()
                    cipher = encrypt(KEY,plain+FLAG)
                    self.send(b'Your cipher:'+ cipher.hex().encode())
                else:
                    go = 0
                    self.send(b'GoodBye!')

        except TimeoutError:
            self.send(b'[!] Ohhehe, Timeout!')

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST,PORT = '0.0.0.0',12321
    server = ForkedServer((HOST,PORT),Serve)
    server.allow_reuse_address = True
    print(HOST, PORT)
    server.serve_forever()
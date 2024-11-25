from hashlib import sha256
import socketserver
import os
import signal
import string
import random

flag = "SYC{...}"

class Task(socketserver.BaseRequestHandler):

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

    def proof_of_work(self):
        random.seed(os.urandom(8))
        proof = ''.join(
            [random.choice(string.ascii_letters+string.digits) for _ in range(20)])
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
        x = self.recv(prompt=b'[+] Plz tell me XXXX: ')
        if len(x) != 4 or sha256(x+proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True

    def handle(self):
        signal.alarm(60)
        try:
            if not self.proof_of_work():
                self.send(b'[!] Wrong!')
                self.send(b'[*] Maybe you need a little force, right?')
                return
            else:
                self.send(b'[*] HEY, MY NEW FRIENDDD, YOUUUUUU FIND THE RIGHT WAAAAAAY!')
                self.send(b'[*] Or even more complex?')
                self.send(b'[*] Maybe these details are not important. See below :D')

            signal.alarm(400)
            self.send(b'[+] ')
            while self.ctry < 35:
                data = self.recv().decode()
                f = self.oraicle(data)
                self.send(f)
                self.ctry += 1

        except TimeoutError:
            self.send(b'[!] Ohhehe, Timeout!')

    def oraicle(self,a):

        if a.isdigit() and int(a)<33 and int(a)>0:
            a = int(a)-1
            return b'[+] ' + flag[a].encode()

        return  b'[!] Invalid Member!'


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST,PORT = '0.0.0.0',12321
    server = ForkedServer((HOST,PORT),Task)
    server.allow_reuse_address = True
    print(HOST, PORT)
    server.serve_forever()
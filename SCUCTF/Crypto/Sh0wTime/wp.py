from hashlib import sha1
from Crypto.Util.number import inverse, bytes_to_long
from ecdsa.ecdsa import Public_key, Private_key, Signature, generator_192


def recover_private_key(r, s, k, h, n):
    """
    从 ECDSA 签名参数恢复私钥
    :param r: 签名参数 r
    :param s: 签名参数 s
    :param k: 签名使用的随机数
    :param h: 消息哈希值（整数形式）
    :param n: 椭圆曲线的阶
    :return: 恢复的私钥 d
    """
    r_inv = inverse(r, n)  # 计算 r 的模逆
    d = (s * k - h) * r_inv % n  # 恢复私钥
    return d

# 示例：
r = 0x19cea4d3a4e153433a58e47afdbba5d9b456c2680b8941c1  # 签名参数 r
s = 0xff33ad480b3764d1661082f93c690c8da825eb43255df578  # 签名参数 s
k = 0x13579BDF2468ACE  # 签名随机数
h = 0xdeadbeef  # 消息的哈希值（整数形式）
g = generator_192
n: int = g.order()

d = recover_private_key(r, s, k, h, n)
print(f"Recovered private key: {hex(d)}")
hsh = bytes_to_long(sha1("The time is 11:2".encode()).digest())
sig = d.sign(hsh, 100)
print(hex(sig.r) == r)
import gmpy2, libnum, codecs, hashlib, itertools
from functools import reduce

from Crypto.Util.number import long_to_bytes


def exgcd(a, b):
    if b == 0: return 1, 0
    x, y = exgcd(b, a % b)
    return y, x - a // b * y


def uni(P, Q):
    r1, m1 = P
    r2, m2 = Q

    d = gmpy2.gcd(m1, m2)
    assert (r2 - r1) % d == 0

    l1, l2 = exgcd(m1 // d, m2 // d)

    return (r1 + (r2 - r1) // d * l1 * m1) % gmpy2.lcm(m1, m2), gmpy2.lcm(m1, m2)


def CRT(eq):
    return reduce(uni, eq)


if __name__ == "__main__":
    ms = [207867980504656835313307696396607264603, 245036212212570610987366430554968489325, 270836744824069537438646110613439698666, 319275775495422875474878625752594133023, 254268823435329877199449670714528712873, 213093607196415232366564484229844568444, 246921085368773491003187313772615702950]
    cs = [150031581047390726903711035932621949276, 21260202376534810598778595491323328519, 144049733622518360270048059408969512643, 236920143187836025924037873968303507493, 99781504248790469459151935530031893836, 69236016568483424294966410179787943383, 20613188366058016717435734248097940419]
    m, mod = CRT(zip(cs, ms))
    print(m, mod)
    # print(hashlib.sha256(1000).hexdigest())
    for i in itertools.count(0):
        s = hashlib.sha256(long_to_bytes(m + i * mod)).hexdigest()
        if "6a651" == s[:5]:
            print(f"SYC{{{s}}}")
            print(long_to_bytes(m + i * mod))
# 第三届黄河流域网络安全技能挑战赛WP

京麒杯是打不动的只好来看看小比赛-悲，Re题目整体难度不大，第一个ak了所有逆向

## Reverse

### qgd

> 最终flag格式：flag{part1flag/part2flag}
>
> 48 89 4C 24 08 55 57 48 81 EC 28 01 00 00 48 8D 6C 24 20 48 8D 0D 34 08 01 00 E8 96 FB FF FF 48 83 BD 20 01 00 00 00 75 05 E9 BF 00 00 00 48 8B 8D 20 01 00 00 E8 7D F9 FF FF 48 89 45 08 48 C7 45 28 00 00 00 00 EB 0B 48 8B 45 28 48 FF C0 48 89 45 28 48 8B 45 08 48 39 45 28 0F 83 8C 00 00 00 48 8B 45 28 48 FF C0 33 D2 B9 02 00 00 00 48 F7 F1 48 8B C2 48 83 F8 01 75 2A 48 8B 45 28 48 8B 8D 20 01 00 00 48 03 C8 48 8B C1 0F BE 00 83 F0 31 48 8B 4D 28 48 8B 95 20 01 00 00 48 03 D1 48 8B CA 88 01 48 8B 45 28 48 FF C0 33 D2 B9 02 00 00 00 48 F7 F1 48 8B C2 48 85 C0 75 2A 48 8B 45 28 48 8B 8D 20 01 00 00 48 03 C8 48 8B C1 0F BE 00 83 F0 58 48 8B 4D 28 48 8B 95 20 01 00 00 48 03 D1 48 8B CA 88 01 
>
>
> encrypted part1 flag:[88 ,47, 80 ,54 ,95 ,57, 90 ,54 ,94, 47]

第一部分很明显需要把上面十六进制字节写入文件然后ida反编译，发现是个奇偶位异或

第二部分在pyinstaller打包的exe中，解包拿到WO0o.pyc和secret.pyc

WO0o是主函数，发现调用了secret里的decrypt获得解密字符串然后做比较，因此直接打印就好

~~~python
from secret import decrypt
key = bytes.fromhex('EC3700DFCD4F364EC54B19C5E7E26DEF6A25087C4FCDF4F8507A40A9019E3B48BD70129D0141A5B8F089F280F4BE6CCD')
ciphertext = b'\xd4z\'0L\x10\xca\x0b\x0b\xaa\x15\xbeK0"\xbf\xb2\xc6\x05'
cipher = decrypt(ciphertext, key)
a = bytes(input('flag呢'), encoding='utf-8')
if a == cipher:
    print('没错没错')
else:
    print('不对不对')
~~~

解密脚本如下

~~~python
def key_schedule(key: bytes) -> list:
    S = list(range(128))
    v6 = 0
    for j in range(128):
        v6 = (S[j] + key[j % len(key)] + v6) % 128
        v6 = (v6 ^ 55) % 128
        S[j], S[v6] = (S[v6], S[j])
    return S

def next_byte(state: dict) -> int:
    S = state['S']
    state['i'] = (state['i'] + 1) % 128
    state['j'] = (state['j'] + S[state['i']]) % 128
    S[state['i']], S[state['j']] = (S[state['j']], S[state['i']])
    v2 = S[(S[state['i']] + S[state['j']]) % 128]
    return (16 * v2 | v2 >> 4) & 255

def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    state = {'S': key_schedule(key), 'i': 0, 'j': 0}
    plaintext = bytearray()
    for byte in ciphertext:
        plaintext.append(byte ^ next_byte(state))
    return bytes(plaintext)

key = bytes.fromhex('EC3700DFCD4F364EC54B19C5E7E26DEF6A25087C4FCDF4F8507A40A9019E3B48BD70129D0141A5B8F089F280F4BE6CCD')
ciphertext = b'\xd4z\'0L\x10\xca\x0b\x0b\xaa\x15\xbeK0"\xbf\xb2\xc6\x05'
flag2 = decrypt(ciphertext, key).decode()

b = bytes.fromhex("48 89 4C 24 08 55 57 48 81 EC 28 01 00 00 48 8D 6C 24 20 48 8D 0D 34 08 01 00 E8 96 FB FF FF 48 83 BD 20 01 00 00 00 75 05 E9 BF 00 00 00 48 8B 8D 20 01 00 00 E8 7D F9 FF FF 48 89 45 08 48 C7 45 28 00 00 00 00 EB 0B 48 8B 45 28 48 FF C0 48 89 45 28 48 8B 45 08 48 39 45 28 0F 83 8C 00 00 00 48 8B 45 28 48 FF C0 33 D2 B9 02 00 00 00 48 F7 F1 48 8B C2 48 83 F8 01 75 2A 48 8B 45 28 48 8B 8D 20 01 00 00 48 03 C8 48 8B C1 0F BE 00 83 F0 31 48 8B 4D 28 48 8B 95 20 01 00 00 48 03 D1 48 8B CA 88 01 48 8B 45 28 48 FF C0 33 D2 B9 02 00 00 00 48 F7 F1 48 8B C2 48 85 C0 75 2A 48 8B 45 28 48 8B 8D 20 01 00 00 48 03 C8 48 8B C1 0F BE 00 83 F0 58 48 8B 4D 28 48 8B 95 20 01 00 00 48 03 D1 48 8B CA 88 01".replace(" ", ""))
with open("out", "wb") as f:
    f.write(b)

flag1 = ""
encrypted = [88,47,80,54,95,57,90,54,94,47]
for i in range(len(encrypted)):
    if i%2:
        flag1 += chr(encrypted[i]^0x58)
    else:
        flag1 += chr(encrypted[i]^0x31)
print(f"flag{{{flag1+flag2}}}")
~~~

`flag{iwannaknowwhat_DO_you_mean#@!}`

### Victory Melody

很简单小型虚拟机，可以直接导出opcode查看

~~~c++
int __fastcall sub_140011890(unsigned int *a1, __int64 a2, __int64 a3)
{
  j___CheckForDebuggerJustMyCode(&unk_140022014, a2, a3);
  while ( 1 )
  {
    switch ( *((_BYTE *)a1 + a1[2] + 268) )
    {
      case 0x10:
        *a1 = *((char *)a1 + a1[2] + 269);
        a1[2] += 2;
        break;
      case 0x11:
        a1[1] = *((char *)a1 + a1[2] + 269);
        a1[2] += 2;
        break;
      case 0x20:
        *((_BYTE *)a1 + *((char *)a1 + a1[2] + 269) + 12) = *((_BYTE *)a1 + a1[2] + 270);
        a1[2] += 3;
        break;
      case 0x30:
        *((_BYTE *)a1 + *a1 + 12) ^= *((_BYTE *)a1 + 4);
        ++a1[2];
        break;
      case 0x40:
        sub_14001109B(&unk_14001ACA4, a1 + 3);	// %7s
        ++a1[2];
        break;
      case 0x50:
        return j_memcmp(a1 + 3, (char *)a1 + *((char *)a1 + a1[2] + 269) + 12, *((char *)a1 + a1[2] + 270));
      default:
        continue;
    }
  }
}
~~~

发现输入7位字符，根据case值对vm做了个划分，然后动调发现7个字符均异或了0x21，直接就能出了

~~~python
vm = [0x20, 0x10, 0x5B,
      0x20, 0x11, 0x58,
      0x20, 0x12, 0x56,
      0x20, 0x13, 0x6E,
      0x20, 0x14, 0x11,
      0x20, 0x15, 0x4E,
      0x20, 0x16, 0x00,
      0x40,
      0x11, 0x21,
      0x10, 0x00,
      0x30,
      0x10, 0x01,
      0x30,
      0x10, 0x02,
      0x30,
      0x10, 0x03,
      0x30,
      0x10, 0x04,
      0x30,
      0x10, 0x05,
      0x30,
      0x10, 0x06,
      0x30,
      0x10, 0x07,
      0x30,
      0x50,
      0x10, 0x07]
for i in range(0, 21, 3):
    print(chr(vm[i+2]^0x21), end="")
~~~

然后md5后包上flag{}

### R

rust写的很难分析，上午没看懂加密方式，隐约感觉像是流密码，但是发现输入不同异或的值也不同，下午出题人上了提示说是魔改了rc4有位移，直接一个个函数找就能找到魔改地方

主函数如下，很明显看出v12是比较值即加密完的数据，v25是我们输入加密完的结果，v4是密钥，加密函数是sub_140003C80

~~~c++
// Hidden C++ exception states: #wind=4
__int64 sub_1400040E0()
{//...
  v29 = -2LL;
  sub_1400017C0(v17, &off_140021CC0);
  sub_14000A950(v17);
  sub_140002A10(v18);
  v20 = sub_140009F60();
  v19[0] = sub_140009F90(&v20, v18);
  v19[1] = v0;
  sub_140001B80(v19);
  v1 = sub_1400036A0(v18);
  v15 = sub_140002080(v1, v2);
  v16 = v3;
  v4 = (_BYTE *)sub_140005C00(8LL, 1LL);
  *v4 = 108;
  v4[1] = 110;
  v4[2] = 116;
  v4[3] = 102;
  v4[4] = 118;
  v4[5] = 112;
  v4[6] = 117;
  v4[7] = 115;
  sub_140006450(v21, v4, 8LL);
  jumpbuf_sp = _except_get_jumpbuf_sp(v21);
  v22[0] = sub_140006470(0LL, jumpbuf_sp);
  v22[1] = v5;
  while ( 1 )
  {
    v23 = sub_140005440(v22);
    v24 = v6;
    if ( !v23 )
      break;
    v13 = v24;
    v10 = (_BYTE *)sub_140006780(v21, v24, &off_140021D10);
    *v10 ^= v13;
  }
  v7 = sub_1400065E0(v21);
  sub_140003C80((unsigned int)v25, v15, v16, v7, v8);
  v12 = (_BYTE *)sub_140005C00(19LL, 1LL);
  *v12 = 41;
  v12[1] = 5;
  v12[2] = 19;
  v12[3] = 12;
  v12[4] = -25;
  v12[5] = -91;
  v12[6] = -46;
  v12[7] = -94;
  v12[8] = -92;
  v12[9] = 58;
  v12[10] = 58;
  v12[11] = 90;
  v12[12] = -69;
  v12[13] = 35;
  v12[14] = -100;
  v12[15] = -28;
  v12[16] = -41;
  v12[17] = 2;
  v12[18] = -65;
  sub_140006450(v26, v12, 19LL);
  v11 = sub_140005870(v25, v26);
  if ( (v11 & 1) != 0 )
  {
    sub_1400017C0(v27, &off_140021D00);
    sub_14000A950(v27);
  }
  else
  {
    sub_1400017C0(v28, &off_140021CE0);
    sub_14000A950(v28);
  }
  sub_140001AB0(v26);
  sub_140001AB0(v25);
  sub_140001AB0(v21);
  return sub_140001A70(v18);
}
~~~

跟入sub_140003C80，发现while循环存在rc4特征，对输入的密钥做了处理，直接动态调试到while外，v23就是根据密钥生成的S盒（每次都一样）

~~~c++
// Hidden C++ exception states: #wind=4
__int64 *__fastcall sub_140003C80(__int64 *a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int64 a5)
{//...
  v38 = -2LL;
  v20 = a2;
  v21 = a1;
  v22 = a1;
  LOBYTE(a1) = 0;
  LOBYTE(a2) = -1;
  v5 = sub_140005120(a1, a2);
  v34 = v5;
  v35 = BYTE2(v5);
  v25 = BYTE2(v5);
  v24 = v5;
  v37 = BYTE2(v5);
  v36 = v5;
  sub_140005620(v23, (BYTE2(v5) << 16) | (unsigned int)(unsigned __int16)v5);
  v26 = 0;
  v27[0] = sub_140006470(0LL, 256LL);
  v27[1] = v6;
  while ( 1 )
  {
    v28 = sub_140005440(v27);
    v29 = v7;
    if ( !v28 )
      break;
    v17 = v29;
    if ( !a5 )
      sub_140020930(&off_140021B70);
    v15 = *(_BYTE *)(a4 + v29 % a5) ^ 0x66;
    v16 = v26;
    v11 = *(unsigned __int8 *)sub_1400066C0(v23, v29, &off_140021B88);
    v14 = v11 + v16;
    if ( __CFADD__(v11, v16) )
      sub_1400208B0(&off_140021BA0);
    if ( __CFADD__(v15, v14) )
      sub_1400208B0(&off_140021BB8);
    v26 = (unsigned __int8)(v15 + v14);
    v12 = sub_140006680(v23);
    sub_1400057D0(v12, v13, v17, v26, (__int64)&off_140021BD0);
  }
  v30 = 0;
  v31 = 0;
  v8 = sub_1400057C0(v20, a3);
  v33[0] = &v30;
  v33[1] = &v31;
  v33[2] = v23;
  sub_140002200(v32, v8, v9, v33);
  sub_140005680(v21, v32);
  sub_140001AB0((__int64)v23);
  return v22;
}
~~~

动调发现sub_140005680的第一个参数就是输出，里面必然有rc4和PRGA操作，直接进去一个个找（动调也可以，一直关注第一个参数a1什么时候变为最终输出）

最终找到如下

~~~c++
char __fastcall sub_140003F40(unsigned __int16 **a1, char *a2)
{//...
  v13 = *a2;
  v2 = **a1;
  if ( __CFADD__(v2, 1) )
    sub_1400208B0(&off_140021BE8);
  **a1 = (unsigned __int8)(v2 + 1);
  v11 = *a1[1];
  v3 = *(unsigned __int8 *)sub_1400066C0(a1[2], **a1, &off_140021C00);
  if ( __CFADD__(v3, v11) )
    sub_1400208B0(&off_140021C18);
  *a1[1] = (unsigned __int8)(v3 + v11);
  v4 = sub_140006680(a1[2]);
  sub_1400057D0(v4, v5, **a1, *a1[1], (__int64)&off_140021C30);
  v9 = a1[2];
  v10 = *(unsigned __int8 *)sub_1400066C0(v9, **a1, &off_140021C48);
  v6 = *(unsigned __int8 *)sub_1400066C0(a1[2], *a1[1], &off_140021C60);
  if ( __CFADD__(v6, v10) )
    sub_1400208B0(&off_140021C78);
  v7 = (_BYTE *)sub_1400066C0(v9, (unsigned __int8)(v6 + v10), &off_140021C90);
  return ((((*v7 >> 4) | (16 * *v7)) + 1) ^ v13) + 1;
}
~~~

很明显这里v7是PRGA的返回的值，然后做了一定处理在和输入异或再加一，逆向就很简单了

~~~python
def PRGA(S):
    """ Pseudo-Random Generation Algorithm (PRGA) 伪随机数生成算法"""
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(text):
    """ RC4 encryption/decryption """
    S = [0x0A, 0x14, 0x8C, 0x2C, 0x1E, 0x9A, 0x43, 0xB9, 0x6F, 0x38, 0x39, 0x68, 0x3F, 0x12, 0x36, 0x56, 0x70, 0x31, 0xE4, 0x3C, 0xCB, 0x60, 0x19, 0x4E, 0x10, 0x85, 0xE3, 0xCC, 0xC4, 0x5A, 0x6D, 0x9E, 0x66, 0x7B, 0xE8, 0xF5, 0x74, 0xA9, 0xAA, 0xF1, 0x2B, 0x5D, 0x78, 0xEC, 0x5F, 0x50, 0x05, 0x9D, 0xE7, 0x8A, 0x53, 0x89, 0x4D, 0x21, 0x3D, 0x8F, 0xB0, 0x1C, 0x52, 0xF3, 0x04, 0x35, 0x57, 0xB2, 0xFC, 0x46, 0x33, 0xDE, 0xF6, 0x0E, 0x5B, 0xFD, 0x29, 0x54, 0x51, 0x24, 0x82, 0xA8, 0xC5, 0xCD, 0x93, 0x7F, 0xAC, 0x1F, 0xA1, 0xB1, 0xD5, 0x61, 0xA0, 0x26, 0x6C, 0x67, 0xF2, 0xDC, 0xBB, 0xD6, 0xFF, 0xDD, 0x8B, 0x4C, 0x92, 0x71, 0xC8, 0x99, 0xD2, 0xB7, 0xBF, 0xA5, 0x16, 0x76, 0x87, 0xA2, 0x97, 0x41, 0xD0, 0x9C, 0x63, 0xC0, 0x03, 0x5E, 0x2A, 0x2D, 0xA3, 0x0C, 0xA6, 0x22, 0xAF, 0xD4, 0x64, 0x84, 0xB5, 0xE9, 0x90, 0x79, 0x6B, 0xE5, 0xFA, 0xB3, 0x23, 0x96, 0x59, 0x08, 0x17, 0xE6, 0xFB, 0x91, 0xAD, 0x6E, 0xF8, 0x58, 0x06, 0x9F, 0xCF, 0xCA, 0x5C, 0x0D, 0x9B, 0xD3, 0x95, 0x73, 0xB6, 0x1B, 0x98, 0xE0, 0x37, 0x94, 0x55, 0x7A, 0xE2, 0x2F, 0x72, 0x11, 0x86, 0x15, 0x83, 0x34, 0xC3, 0xAE, 0x49, 0x8D, 0xD9, 0x0F, 0xE1, 0xCE, 0xC2, 0xED, 0x25, 0x88, 0xC1, 0xD1, 0x81, 0xD8, 0x01, 0x2E, 0xEA, 0x20, 0x00, 0xBD, 0xEE, 0xC7, 0xB4, 0xDB, 0xA4, 0x0B, 0xF4, 0xAB, 0x7D, 0xEB, 0x3B, 0x02, 0xC6, 0xEF, 0xFE, 0x27, 0x09, 0x32, 0xF7, 0x47, 0x30, 0x44, 0x4F, 0x13, 0x77, 0x07, 0x18, 0x65, 0x7C, 0xBC, 0x40, 0xF0, 0x28, 0xD7, 0x4B, 0x3E, 0x1D, 0xB8, 0x42, 0xDF, 0x48, 0x3A, 0x69, 0xF9, 0x8E, 0x75, 0xDA, 0x4A, 0x45, 0xBE, 0x1A, 0x80, 0xBA, 0x6A, 0xA7, 0xC9, 0x62, 0x7E]
    keystream = PRGA(S)
    res = []
    for char in text:
        tmp = next(keystream)
        tmp = (tmp << 4) | (tmp >> 4)
        tmp += 1
        tmp &= 0xff
        res.append(((char-1) ^ tmp))
    return bytes(res)


text = [0x29, 0x05, 0x13, 0x0C, 0xE7, 0xA5, 0xD2, 0xA2, 0xA4, 0x3A, 0x3A, 0x5A, 0xBB, 0x23, 0x9C, 0xE4, 0xD7, 0x02, 0xBF]
print(f"flag{{{RC4(text).decode()}}}")
~~~

`flag{Y0uKn0wRu5tV@ryW@1l}`

### go for it

算法相比Rust好分析多了

~~~c++
// main.main
void __fastcall main_main()
{//...
  p_string = (string *)runtime_newobject(&RTYPE_string);
  v75 = p_string;
  p_string->ptr = 0LL;
  v78[0] = &RTYPE__ptr_string;
  v78[1] = p_string;
  v2 = qword_567068;
  fmt_Fscanf(
    (unsigned int)go_itab__ptr_os_File_comma__ptr_io_Reader,
    qword_567068,
    (unsigned int)"%s",
    2,
    (unsigned int)v78,
    1,
    1,
    v3,
    v4);
  if ( v2 || v75->len != 32 )
    goto LABEL_4;
  v70 = v0;
  v71 = v0;
  ptr = (unsigned __int64)v75->ptr;
  v10 = runtime_stringtoslicebyte(
          (unsigned int)&v69,
          v75->ptr,
          v75->len,
          (unsigned int)&v71,
          (unsigned int)&v70,
          v5,
          v6,
          v7,
          v8);
  v73 = v10;
  v66 = ptr;
  v67 = v11;
  v16 = 0LL;
  while ( (__int64)ptr > v16 )
  {
    v17 = v16;
    while ( v16 < (__int64)(v17 + 4) )
    {
      if ( ptr <= v16 )
        runtime_panicIndex(v16, ptr, ptr);
      v43 = *(unsigned __int8 *)(v16 + v10);
      if ( ptr <= v16 + 2 )
        runtime_panicIndex(v16 + 2, ptr, ptr);
      v44 = v43 ^ *(unsigned __int8 *)(v16 + v10 + 2);
      *(_BYTE *)(v10 + v16) = v43 ^ *(_BYTE *)(v16 + v10 + 2);
      if ( ptr <= v16 + 1 )
        runtime_panicIndex(v16 + 1, ptr, ptr);
      LODWORD(cap) = v44 ^ *(unsigned __int8 *)(v16 + v10 + 2);
      v42 = cap ^ *(unsigned __int8 *)(v16 + v10 + 1);
      *(_BYTE *)(v16 + v10 + 1) ^= (unsigned __int8)v44 ^ *(_BYTE *)(v16 + v10 + 2);
      v12 = v42 ^ *(unsigned __int8 *)(v16 + v10 + 2);
      *(_BYTE *)(v16 + v10 + 2) ^= v42;
      v16 += 3LL;
    }
    v79 = 0;
    v80 = 0LL;
    v81 = v0;
    v18 = 0LL;
    v19 = (_QWORD *)math_big__ptr_Int_SetInt64(
                      (unsigned int)&v79,
                      0,
                      v11,
                      (int)v17 + 4,
                      v17,
                      v12,
                      cap,
                      v14,
                      v15,
                      v51,
                      v55);
    v20 = v17;
    v21 = v17 + 8;
    if ( v67 < v17 + 8 )
      runtime_panicSliceAcap(v19, 0LL, v17 + 8);
    if ( v17 > v21 )
      goto LABEL_47;
    v72 = v19;
    v22 = (v17 & ((__int64)(v17 - v67) >> 63)) + v73;
    v23 = v19[2];
    v24 = math_big_nat_setBytes(
            v19[1],
            v23,
            v19[3],
            v22,
            8,
            (int)v67 - (int)v17,
            (int)v67 - (int)v17,
            v73,
            v19[1],
            v52,
            v56,
            v58,
            v60,
            v62,
            v64);
    v25 = v72;
    v72[2] = v23;
    v25[3] = v26;
    if ( dword_5BBB30 )
    {
      LODWORD(v22) = (_DWORD)v25 + 8;
      runtime_gcWriteBarrier(v25 + 1);
    }
    else
    {
      v25[1] = v24;
    }
    *(_BYTE *)v25 = 0;
    if ( v25[2] )
      v27 = *(_QWORD *)v25[1];
    else
      v27 = 0LL;
    for ( i = 0LL; i < 64; ++i )
    {
      if ( v27 < 0 )
        v27 = (2 * v27) ^ 0x2EF20D07161E85F7LL;
      else
        v27 *= 2LL;
    }
    v65 = v27;
    p_bytes_Buffer = (bytes_Buffer *)runtime_newobject(&RTYPE_bytes_Buffer);
    v34 = runtime_convT64(v65, v23, v29, v22, 8, v30, v31, v32, v33, v53);
    v18 = p_bytes_Buffer;
    v38 = encoding_binary_Write(
            (unsigned int)go_itab__ptr_bytes_Buffer_comma__ptr_io_Writer,
            (_DWORD)p_bytes_Buffer,
            (unsigned int)go_itab__ptr_binary_littleEndian_comma__ptr_binary_ByteOrder,
            (unsigned int)&unk_5BBAD8,
            (unsigned int)&RTYPE_int64,
            v34,
            v35,
            v36,
            v37,
            v54,
            v57,
            v59,
            v61,
            v63,
            v64);
    if ( v38 )
    {
      runtime_gopanic(
        *(_QWORD *)(v38 + 8),
        (_DWORD)v18,
        v39,
        (unsigned int)&unk_5BBAD8,
        (unsigned int)&RTYPE_int64,
        v12,
        cap,
        v14,
        v15,
        v51,
        v55);
LABEL_47:
      runtime_panicSliceB(v20, v18, v21);
    }
    v40 = p_bytes_Buffer;
    for ( j = 0LL; j < 8; ++j )
    {
      for ( k = 0LL; k < 8; ++k )
      {
        len = v40->buf.len;
        cap = v40->buf.cap;
        off = v40->off;
        if ( off > len )
          runtime_panicSliceB(v40->off, v18, v40->buf.len);
        v48 = len - off;
        v14 = (__int64)(off - cap) >> 63;
        v15 = v14 & v40->off;
        if ( k >= v48 )
          runtime_panicIndex(k, v18, v48);
        v18 = (bytes_Buffer *)k;
        v12 = -128;
        LOBYTE(v12) = 0x80u >> j;
        if ( ((0x80u >> j) & __ROL1__(v40->buf.ptr[v15 + k], 5)) != 0 )
        {
          v49 = j + v17;
          if ( j + v17 >= 0x20 )
            runtime_panicIndex(j + v17, k, 32LL);
          v12 = *((unsigned __int8 *)&v70 + v49);
          v50 = -128;
          LOBYTE(v50) = 0x80u >> k;
          LODWORD(cap) = v12 | v50;
          *((_BYTE *)&v70 + v49) = cap;
        }
      }
    }
    v10 = v73;
    ptr = v66;
    v16 = v17 + 8;
    LODWORD(v11) = v67;
  }
  v68[0] = 0x8ADD5C04E5934C8LL;
  v68[1] = 0x199AC0E6DA4C2BC9LL;
  v68[2] = 0xFF83F5E87D5510B5LL;
  v68[3] = 0x58447D6AD4E38B74LL;
  if ( (unsigned __int8)runtime_memequal(&v70, v68, 32LL) )
  {
    v77[0] = &RTYPE_string;
    v77[1] = &off_4DE248;
    fmt_Fprintln(
      (unsigned int)go_itab__ptr_os_File_comma__ptr_io_Writer,
      qword_567070,
      (unsigned int)v77,
      1,
      1,
      v5,
      v6,
      v7,
      v8,
      v51,
      v55,
      v58,
      v60,
      v62);
  }
  else
  {
LABEL_4:
    v76[0] = &RTYPE_string;
    v76[1] = &off_4DE258;
    fmt_Fprintln(
      (unsigned int)go_itab__ptr_os_File_comma__ptr_io_Writer,
      qword_567070,
      (unsigned int)v76,
      1,
      1,
      v5,
      v6,
      v7,
      v8,
      v51,
      v55,
      v58,
      v60,
      v62);
  }
}
~~~

* 首先输入长度32的字符串
* 然后每8位字符一组（v17+8）前6个字符每3个字符做一轮异或处理，还原比较复杂需要认真分析
* 然后处理完的8字节转为int数做了64轮crc64加密（(2 * v27) ^ 0x2EF20D07161E85F7LL）
* 双层8*8循环先把每个字符循环左移5位，然后转置读取比特，读出新的8字节
* runtime_memequal比较4组8字节，即32字节

按步骤逆向即可，注意端序，多调试检查输入输出就好

~~~python
from Crypto.Util.number import bytes_to_long

def transpose_bytes8x8(block):
    # 先把 block 解开成 8×8 位矩阵 bits[row][col]
    bits = [[(block[row] >> (7 - col)) & 1 for col in range(8)]
            for row in range(8)]

    # 转置后按行重组，每行 8 个 bit 合成一个字节
    transposed = []
    for new_row in range(8):
        byte = 0
        for new_col in range(8):
            byte = (byte << 1) | bits[new_col][new_row]
        transposed.append(byte)

    return bytes(transposed)


s = ["08ADD5C04E5934C8", "199AC0E6DA4C2BC9", "FF83F5E87D5510B5", "58447D6AD4E38B74"]
for i in range(len(s)):
    s[i] = transpose_bytes8x8(bytes.fromhex(s[i])[::-1])
ss = []
for i in s:
    ss += list(i)
for i in range(len(ss)):
    ss[i] = (ss[i] << 3) | (ss[i] >> 5)
    ss[i] &= 0xff
s = [bytes_to_long(bytes(ss[i:i+8][::-1])) for i in range(0, len(ss), 8)]
new_s = []
for v in s:
    for i in range(64):
        bit = v & 1
        if bit:
            v ^= 0x2EF20D07161E85F7
        v >>= 1
        if bit:
            v |= 0x8000000000000000
    new_s.append(v)
s = []
for i in new_s:
    tmp = list(i.to_bytes(8, byteorder='big'))
    flag = [0] * 8
    for i in range(0, 6, 3):
        flag[i+2] = tmp[i+2] ^ tmp[i+1]
        flag[i] = tmp[i] ^ flag[i+2]
        flag[i+1] = tmp[i+1] ^ flag[i]
    flag[6] = tmp[6]
    flag[7] = tmp[7]
    print("".join(map(chr, flag)), end="")
~~~

`flag{5e28e27a835c4958b2d6dd186b21727a}`

## Misc

只做了一道，学点新知识

有一种二维码叫data matrix，https://zxing.org/w/decode.jspx可以解密

解密出来再base85得到UV!W_X_YZ,U,Y∈[0,9], V,W,X,Z∈[A,z]

这个是提示要用掩码来爆破zip
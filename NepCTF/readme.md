# NepCTF 2024

比赛题目都去哪了，怎么网上都没找到，印象里貌似很多0解题目？完整保留的只有3道（只会2道）

## ezAndroid

> 网盘链接：https://pan.baidu.com/s/1geynaaZGnoojLjrpGPQC-g?pwd=hero 提取码：hero 非常ez的安卓题。确保flag内容为32位后请包裹NepCTF{}提交。 雷电9.0版本模拟器测试可运行。

jeb查关键字符串直接定位apk里的`ProxyActivity`，java层没有加密代码都在lib里，传入的是32位字符串

先导入JNI相关结构体（parce c header-jni.h-Y键 `JNIEnv *`），再定位关键函数如下

~~~c
_OWORD *__fastcall sub_8B4(JNIEnv *a1, __int64 a2, __int64 a3)
{
  v23 = *(_QWORD *)(_ReadStatusReg(ARM64_SYSREG(3, 3, 13, 0, 2)) + 40);
  result = (_OWORD *)((__int64 (__fastcall *)(JNIEnv *, __int64, _QWORD))(*a1)->GetStringUTFChars)(a1, a3, 0LL);
  if ( result )
  {
    v22 = 0LL;
    *(_OWORD *)v20 = 0u;
    v21 = 0u;
    v4 = result[1];
    *(_OWORD *)v20 = *result;
    v21 = v4;
    v5 = 0;
    v6 = __strlen_chk(v20, 0x28u) - 1;
    if ( v6 >= 0 )
    {
      do
      {
        v18 = (unsigned int)v6;
        if ( v20[v6] == 49 )	// 等于"1"
        {
          v19 = __strlen_chk(v20, 0x28u);
          v5 = (unsigned int)(exp2((double)(unsigned __int64)(v19 + ~v18)) + (double)v5);
        }
        v6 = v18 - 1;
      }
      while ( (int)v18 - 1 >= 0 );	// 二进制串转十进制int数字
    }
    srand(0x53355354u);
    v7 = rand() % 7;
    v8 = v5;
    if ( v7 )
    {
      v9 = 0;
      v10 = 0;
      v11 = -v7;
      do
      {
        v12 = v11 + v9;
        v13 = rand();
        v14 = v13 + 31;
        if ( v13 >= 0 )
          v14 = v13;
        v15 = v13 - (v14 & 0xE0);               // v13%32
        if ( (v9 & 1) != 0 )                    // 奇数
        {
          if ( (v15 & 1) != 0 )
            v17 = v10 << v15;
          else
            v17 = v10 >> v15;
          v8 = v17 ^ v10;
          v7 = v17 ^ v10;
          if ( v12 == -1 )
            return (_OWORD *)(v7 == 0xE4BE1307);
        }
        else                                    // 偶数
        {
          if ( (v15 & 1) != 0 )
            v16 = v8 << v15;
          else
            v16 = v8 >> v15;
          v10 = v16 ^ v8;
          v7 = v16 ^ v8;
          if ( v12 == -1 )
            return (_OWORD *)(v7 == 0xE4BE1307);
        }
        ++v9;
      }
      while ( v11 + v9 );
    }
    return (_OWORD *)(v7 == 0xE4BE1307);
  }
  return result;
}
~~~

随机数生成，必须在linux上跑，毕竟安卓linux

~~~c++
#include <iostream>

int main() {
    srand(0x53355354u);
    int a = rand()%7;
    printf("%d, ", a);
    for (int i = 0; i < a; i++)
        printf("%d, ", rand()%32);
}
~~~

得到`6, 12, 28, 11, 12, 14, 14, `，所以进入循环的有6个

最开始试图逆向位运算发现太复杂了，就用z3，结果试了半天才发现这里BitVec必须设置为`64位`才可以出来结果，貌似因为左移溢出的原因

~~~python
from z3 import *

rand_list = [12, 28, 11, 12, 14, 14]
s = Solver()
v = BitVec('v', 64)
for i in range(len(rand_list)):
    if rand_list[i] % 2:
        v = (v << rand_list[i] & 0xffffffff) ^ v
    else:
        v = (v >> rand_list[i] & 0xffffffff) ^ v
s.add(v==0xE4BE1307)
if s.check() == sat:
    ans = s.model()
    print(bin(ans[ans[0]].as_long())[2:].zfill(32))	# 01100101011101100110111101101100
~~~

出题人的代码很神奇，脑子太笨没搞懂为啥是这样

~~~c
#include
void left(unsigned char* enc, unsigned int num) {           //左移解密          
    for (int i = 31 - num; i >= 0; i--) {          
        if (enc[i] != enc[i + num]) {          
            enc[i] = '1';          
        }          
        else {          
            enc[i] = '0';          
        }          
    }          
}          
void right(unsigned char* enc, unsigned int num) {          //右移解密          
    for (int i = num; i < 32; i++) {          
        if (enc[i] != enc[i - num]) {          
            enc[i] = '1';          
        }          
        else {          
            enc[i] = '0';          
        }          
    }          
}          
void  decrypt() {          
    unsigned int cnt[] = { 12, 28,11,12,14,14 };              //随机数          
    unsigned char enc[] = "11100100101111100001001100000111";    //result          
    //printf("0x%x\n", Otto(enc));          
    for (int i = 5; i >= 0; i--) {          
        if ((cnt[i] % 2) == 0) {          
            right(enc, cnt[i]);          
        }          
        else {          
            left(enc, cnt[i]);          
        }          
    }          
         
    printf("%s", enc);          
}          
int main()          
{          
    decrypt();          
}
~~~

##  0ezAndroid

> 点得够多的小朋友，会有flag作为奖励，flag请用NepCTF{}代替flag{}包裹提交。
>
> 娱乐题，玩的开心:)

纯加密算法分析，需要注意rc4改编的，init循环不止一次

~~~python
import struct
from ctypes import c_uint32


def tea_encrypt(r, v, key, delta):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    # delta = 0x9e3779b9  # -0x61C88647
    total = c_uint32(0)
    for i in range(r):
        total.value += delta
        v0.value += ((v1.value << 4) + key[0]) ^ (v1.value + total.value) ^ ((v1.value >> 5) + key[1])
        v1.value += ((v0.value << 4) + key[2]) ^ (v0.value + total.value) ^ ((v0.value >> 5) + key[3])
    return v0.value, v1.value


def tea_decrypt(r, v, key, delta):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    # delta = 0x9e3779b9
    total = c_uint32(delta * r)
    for i in range(r):
        v1.value -= ((v0.value << 4) + key[2]) ^ (v0.value + total.value) ^ ((v0.value >> 5) + key[3])
        v0.value -= ((v1.value << 4) + key[0]) ^ (v1.value + total.value) ^ ((v1.value >> 5) + key[1])
        total.value -= delta
    return v0.value, v1.value


def PRGA(S):
    """ Pseudo-Rom Generation Algorithm (PRGA) 伪随机数生成算法"""
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, text):
    """ RC4 encryption/decryption """
    S = list(range(256))
    j = 0
    for k in range(10000000):
        for i in range(256):	# s box init
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]
        new_S = S.copy()
        keystream = PRGA(new_S)
        res = []
        for i in range(len(text)):
            char = text[i]
            res.append(char ^ next(keystream))
        if bytes(res).find(b'%PDF-1.4') != -1:
            print(bytes(res), k)
            open("out", "wb").write(bytes(res))
            break


if __name__ == "__main__":
    k = [49, 50, 51, 52]
    v = [602450884, 98211040, 0x7A2D2F0D, 0x77FC29FF]
    delta = 287454020
    for i in range(0, len(v), 2):
        v[i:i+2] = tea_encrypt(32, v[i:i+2], k, delta)
    print(list(map(hex, v)))
    key = b"".join([int.to_bytes(i, 4, byteorder="little") for i in v])
    print(key)  # b'bangboo!Knows!!!'
    text = [...]	# so文件里找导出的
    RC4(key, text)
~~~

写入文件里的内容里是pdf格式+js代码，提取出来代码跑一下即可得到flag

~~~js
function _0x293d(_0xf34e71, _0x3b0a75) {
	var _0x152c52 = _0x152c();
	return (
		(_0x293d = function (_0x293d07, _0x1cf734) {
			_0x293d07 = _0x293d07 - 0x17d;
			var _0x295575 = _0x152c52[_0x293d07];
			return _0x295575;
		}),
		_0x293d(_0xf34e71, _0x3b0a75)
	);
}
function _0x152c() {
	var _0x2afd46 = [
		"length",
		"1290091TnwESj",
		"log",
		"24gcWwOg",
		"238vgiywR",
		"1110zIrcMD",
		"6570PnprMP",
		"2724jzgoXj",
		"32622ruecCw",
		"1iEaPEv",
		"559224qyymQW",
		"fromCharCode",
		"170qYoxBW",
		"91746kJRbmM",
		"1285816cOGCJT",
	];
	_0x152c = function () {
		return _0x2afd46;
	};
	return _0x152c();
}
var _0x1bd3c0 = _0x293d;
(function (_0x46e90f, _0x45bba7) {
	var _0x4be0b6 = _0x293d,
		_0x2c1162 = _0x46e90f();
	while (!![]) {
		try {
			var _0xd857f7 =
				(parseInt(_0x4be0b6(0x17f)) / 0x1) *
					(parseInt(_0x4be0b6(0x180)) / 0x2) +
				-parseInt(_0x4be0b6(0x183)) / 0x3 +
				(parseInt(_0x4be0b6(0x17d)) / 0x4) *
					(parseInt(_0x4be0b6(0x182)) / 0x5) +
				(parseInt(_0x4be0b6(0x17e)) / 0x6) *
					(parseInt(_0x4be0b6(0x189)) / 0x7) +
				-parseInt(_0x4be0b6(0x184)) / 0x8 +
				(parseInt(_0x4be0b6(0x18b)) / 0x9) *
					(parseInt(_0x4be0b6(0x18a)) / 0xa) +
				(parseInt(_0x4be0b6(0x186)) / 0xb) *
					(-parseInt(_0x4be0b6(0x188)) / 0xc);
			if (_0xd857f7 === _0x45bba7) break;
			else _0x2c1162["push"](_0x2c1162["shift"]());
		} catch (_0x203077) {
			_0x2c1162["push"](_0x2c1162["shift"]());
		}
	}
})(_0x152c, 0x22dbf);
var cipher = [
	0x69, 0x7c, 0x70, 0x75, 0x68, 0x71, 0x7b, 0x73, 0x79, 0x76, 0x7c, 0x7f,
	0x75, 0x72, 0x78, 0x70, 0x7a, 0x45, 0x4f, 0xe, 0x4d, 0x41, 0x4b, 0x43, 0x42,
	0x46, 0x4c, 0x44, 0x4e, 0x42, 0xc, 0x40, 0x4a, 0x55, 0x5f, 0x13, 0x4e,
];
flag = "";
for (i = 0x0; i < cipher[_0x1bd3c0(0x185)]; i++) {
	flag += String[_0x1bd3c0(0x181)](cipher[i] ^ (i + 0xf));
}
console[_0x1bd3c0(0x187)](flag);	// flag{enenneenneneen,neneenenen!neen!}
~~~

##  easyobf

> xia0ji233写了一个非非非非非非非非非常简单的混淆器，有一天他想看看自己的混淆器实力如何，于是有了这道题...

不会做呢，这到底考啥的，没找到wp

唯一有点信息的：https://github.com/Yutori-Natsu/Yutori-Natsu.github.io/blob/aaf6b1b8b67f31536eb7cf88ae8fd053ed67a0b1/source/_posts/frida-%E5%AE%89%E5%8D%93%E9%80%86%E5%90%91%E5%88%9D%E6%8E%A2-0824-NepCTF2024-%E9%83%A8%E5%88%86%E9%A2%98%E7%9B%AE%E5%A4%8D%E7%8E%B0.md

## A service

> 浮游城建造后，罗恩开发了多种android机器人被用于日常维护、保护工作。 不过由于人们粗鲁的对待方式机器人们产生了不满意，MK99更是成为了懒虫。 现在罗恩想要升级MK99，但是MK99给自己服务上了锁，你能帮罗恩解开锁吗？

找不到附件了

## Qriver4.0

> http://nepfrp.lemonprefect.cn:3606/d/Topic/Qriver4.0.rar?sign=b05te98lDhjn-WXMD5ps3NyX4Fbh-bwGGOaSL3UzPUo=:0
>
> Windows 10 x64
>
> PS：手动加载sys文件后运行exe
>
> 更新题目描述：手动加载sys文件后运行exe

找不到附件了

## DCTris Secret

> Find a secret cheat code in the game.
>
> Flag格式 NepCTF{一组按键序列}，按键序列仅有"A B X Y"按键和"上下左右"
>
> "上下左右"用"U D L R"表示
>
> Example：NepCTF{UUDDLRLRBAXXYY}，不代表实际长度
>
> 附件同 misc DCTris Evolved

这什么鬼？

## Super Neuro : Escape from Flame!

> Neuro一觉醒来变成面包了desu~
>
> Neuro被困在烘焙屋了! 身后是烤面包机散发出来的滚滚烈火/浓烟 玩家要在时间限制内控制Neuro及时通过障碍 否则会被屁股的火焰追上导致失败!!! （其实没做 x）
>
> - 如果可能的话，最好玩一下教学关
> - 正常上 1024 就能得到 Flag

找不到附件了


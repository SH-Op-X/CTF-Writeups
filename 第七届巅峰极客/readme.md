# 第七届巅峰极客

比赛是真垃圾，出9道web，30道安全选择题还有多选，其他方向就出一道题，不知道出题人咋想的

## Reverse

### BabyRe

- [x] solved

这题主函数代码存在不少混淆，有些地方执行不到，所以采用动态调试的方法确认加密比较流程（输入了flag{aaa}）

进来调试发现直接跳转else里的一个while循环，`pbInput`每次接收3个输入的字符，使用sha256加密存到v14

~~~c
while ( 1 )
{
    sub_7FF65AFE1FF0(v101, pbInput, v10, v6);
    BCryptOpenAlgorithmProvider(&phAlgorithm, L"SHA256", 0i64, 0);
    BCryptCreateHash(phAlgorithm, &phHash, 0i64, 0, 0i64, 0, 0);
    v11 = (UCHAR *)pbInput;
    if ( v95 > 0xF )
      v11 = pbInput[0];
    BCryptHashData(phHash, v11, cbInput[0], 0);
    BCryptFinishHash(phHash, &pbOutput, 0x20u, 0);
    BCryptDestroyHash(phHash);
    BCryptCloseAlgorithmProvider(phAlgorithm, 0);
    v12 = v95;
    v13 = v95 > 0xF;						// v95=15，恒不成立v13=0
    v14 = &v107;                            // sha256加密后的位置
    v15 = 2i64;
    v16 = 2i64;
    v17 = *(_QWORD *)cbInput;
    v18 = pbInput[0];
    do
    {//...
    } while ()
	//...
}
~~~

do-while循环里主要是一对判断v13，其中v13恒为0，即只执行一个方向

~~~c
do
{
    v19 = pbInput;
    if ( v12 > 0xF )
    	v19 = (PUCHAR *)v18;
    *(v14 - 1) ^= *((_BYTE *)v19 + (v15 - 2) % v17);
	v20 = (v15 - 1) % v17;
    *v14 ^= *((_BYTE *)pbInput + v20);
    v14[1] ^= *((_BYTE *)pbInput + v15 % v17);
    v14[2] ^= *((_BYTE *)pbInput + (v15 + 1) % v17);
    v14[3] ^= *((_BYTE *)pbInput + (v15 + 2) % v17);
    v14[4] ^= *((_BYTE *)pbInput + (v15 + 3) % v17);
    v14[5] ^= *((_BYTE *)pbInput + (v15 + 4) % v17);
    v14[6] ^= *((_BYTE *)pbInput + (v15 + 5) % v17);
    v14[7] ^= *((_BYTE *)pbInput + (v15 + 6) % v17);
    v14[8] ^= *((_BYTE *)pbInput + (v15 + 7) % v17);
    v14[9] ^= *((_BYTE *)pbInput + (v15 + 8) % v17);
    v14[10] ^= *((_BYTE *)pbInput + (v15 + 9) % v17);
    v14[11] ^= *((_BYTE *)pbInput + (v15 + 10) % v17);
    v14[12] ^= *((_BYTE *)pbInput + (v15 + 11) % v17);
    v21 = *((_BYTE *)pbInput + (v15 + 12) % v17);
    v22 = pbInput;
    v14[13] ^= v21;
    v14[14] ^= *((_BYTE *)v22 + (v15 + 13) % v17);
    v15 += 16i64;
    v14 += 16;
    --v16;
}
while ( v16 );
~~~

找v14内存地址查看可知，是sha256的结果和每次取的三个字符（`fla`）分别异或

得到的结果开头是0xA5, 0x7C, 0x97, ...，

再去找整个代码里唯一比较值的位置，发现和unk_7FF65AFE90C0比较1280字节

~~~c
if ( (void *)(Buf1[1] - Buf1[0]) != (void *)1280
	|| (v75 = memcmp(Buf1[0], &unk_7FF65AFE90C0, 0x500ui64), v76 = "right,flag is your input!", v75) )
{
	v76 = "Error.";
}
~~~

提取unk_7FF65AFE90C0，意外发现上面整段sha256异或完的结果都在这个unk数组中

继续调试可以发现循环完回到sha256加密处时，要加密的字符变为`lag`，和第一次比整体向后移动了一位，sha256完再异或完，结果同样在unk数组中找到（但是顺序乱了）。由此可知，unk存储的是flag每三位加密完的结果，理论上可以每三个字符爆破

在最开始while循环开始前有一处地方对输入进行了字符范围判断：`-`的ascii值45，`}`的ascii值125，范围可以限制在`48~123`+125+45

~~~c
while ( 1 )
{
    v8 = v101;
    if ( v103 > 0xF )
    	v8 = (void **)v101[0];
    v9 = *((_BYTE *)v8 + v7);
    if ( (unsigned __int8)(v9 - 48) > 9u && (unsigned __int8)(v9 - 97) > 0x1Au && v9 != 45 && v9 != 125 )
   		break;
    ++v4;
    ++v7;
    if ( v4 >= v6 )
    	goto LABEL_10;
}
v23 = sub_7FF65AFE24D0(std::cout, "Error.", v7);
std::ostream::operator<<(v23, sub_7FF65AFE2880);
~~~

由此写脚本爆破

~~~python
from itertools import product
import hashlib

s = [0xEB, 0x74, 0x46, 0x4F, 0x79, 0x24, 0xC5, 0x62, 0x10, 0xCB, 0xFF, 0xC5, 0xA2, 0x39, 0xBE, 0x03, 0x99, 0xED, 0x2C, 0x8F, 0xB9, 0x54, 0x2B, 0xA7, 0xC5, 0x8A, 0x7E, 0x56, 0x0F, 0x35, 0x2C, 0xA0, 0x3E, 0xE5, 0xE0, 0x0A, 0x6E, 0xA9, 0x38, 0xCF, 0x85, 0xF8, 0x82, 0xC7, 0x99, 0xD7, 0x8B, 0xC6, 0x82, 0x22, 0x54, 0x28, 0xF4, 0xE5, 0x56, 0xD0, 0x47, 0xF1, 0x5E, 0x57, 0x66, 0x85, 0x5C, 0x04, 0x66, 0x0D, 0xC7, 0x21, 0x81, 0x95, 0x4C, 0xF9, 0x97, 0x6E, 0x57, 0x05, 0xCB, 0xAA, 0x48, 0x3D, 0x2A, 0xAB, 0x5A, 0x69, 0x28, 0x3D, 0x68, 0xE4, 0xF7, 0x4C, 0x23, 0xCF, 0xA8, 0xC2, 0x26, 0xD0, 0xF9, 0x41, 0xE7, 0xF4, 0xFF, 0x99, 0x60, 0xF1, 0xDA, 0x67, 0x7E, 0x9D, 0xBF, 0x98, 0x14, 0xB5, 0xB3, 0xE2, 0xD7, 0x99, 0x07, 0x4A, 0xC0, 0x12, 0x0F, 0x21, 0x2F, 0x3A, 0x52, 0xC3, 0x7F, 0xE3, 0x35, 0xD5, 0x6D, 0xB4, 0xBD, 0x21, 0x46, 0x00, 0x04, 0x9F, 0x7F, 0x95, 0x0C, 0x01, 0xFA, 0xBD, 0x86, 0x25, 0x06, 0x56, 0x07, 0x30, 0x4F, 0x17, 0xAE, 0xF3, 0xC0, 0xF0, 0x17, 0x7F, 0x9B, 0x3E, 0xBD, 0xE5, 0x66, 0x33, 0x46, 0x60, 0x6C, 0xB3, 0x07, 0xF1, 0x64, 0x5F, 0x00, 0x6D, 0xB0, 0x88, 0xF3, 0x4F, 0x7D, 0x44, 0xBE, 0x95, 0x43, 0xA1, 0x39, 0x3B, 0x29, 0x50, 0x6D, 0x1D, 0x31, 0x81, 0x44, 0x60, 0xFE, 0x7B, 0xAC, 0x48, 0xBD, 0xBB, 0x8E, 0x35, 0x41, 0x28, 0xE7, 0x53, 0x5C, 0xE7, 0x3B, 0x16, 0x18, 0xC5, 0x94, 0xD9, 0xD1, 0xB9, 0xBF, 0x71, 0x48, 0xA7, 0xD7, 0x70, 0x77, 0xE9, 0xA7, 0xFF, 0xA0, 0xBE, 0x1C, 0xFA, 0x98, 0x00, 0xFE, 0x33, 0x64, 0xF9, 0xE7, 0x30, 0x45, 0x57, 0x97, 0x40, 0x45, 0xE0, 0xC9, 0x50, 0xB8, 0xF3, 0x44, 0x44, 0x32, 0xC1, 0x6A, 0xB7, 0xDD, 0xEE, 0x37, 0x1F, 0x60, 0x26, 0xFA, 0x2D, 0x6F, 0xC1, 0x43, 0x59, 0x8A, 0x9E, 0xE9, 0xE1, 0x27, 0x36, 0xEA, 0xBD, 0x51, 0x5B, 0xAE, 0x24, 0xBB, 0x03, 0xE4, 0xC0, 0x62, 0xDD, 0xC2, 0x63, 0xF4, 0xA1, 0x8C, 0x3E, 0x5C, 0x10, 0xA4, 0xCC, 0x88, 0xE1, 0x9B, 0x04, 0x59, 0x2B, 0x86, 0x4A, 0xC8, 0x83, 0xD8, 0xB9, 0x94, 0xEE, 0xB2, 0xC4, 0x64, 0x96, 0xB3, 0x41, 0x6B, 0x00, 0x0C, 0x9A, 0x34, 0x4A, 0x4F, 0x3C, 0xF2, 0xC3, 0x0D, 0xA6, 0xDD, 0x57, 0xB7, 0xD3, 0x70, 0x1C, 0xDC, 0xB9, 0x41, 0x8E, 0xAE, 0x8A, 0x04, 0x70, 0xC2, 0xAD, 0x26, 0x68, 0xEC, 0xF0, 0xE3, 0xAE, 0x6B, 0x6A, 0x29, 0xF6, 0xAE, 0x3C, 0x23, 0xE3, 0x0F, 0x42, 0x57, 0x1D, 0xFC, 0x50, 0x71, 0x71, 0xD1, 0x73, 0xF9, 0x28, 0x71, 0x8E, 0x2A, 0x5D, 0x18, 0xC4, 0x3F, 0x7A, 0x5B, 0x20, 0xE1, 0x25, 0xA6, 0x42, 0x1E, 0xFB, 0xEF, 0xA5, 0x03, 0x4B, 0xF4, 0x4B, 0x5E, 0x66, 0xEF, 0x90, 0x12, 0x4E, 0xE2, 0xCF, 0xFD, 0x9A, 0xAC, 0xE7, 0xC4, 0x93, 0x56, 0xA6, 0x4A, 0xDF, 0xFB, 0xA0, 0xD4, 0x4D, 0x29, 0xB1, 0x25, 0xAB, 0x8E, 0x98, 0x38, 0x6E, 0xD9, 0x11, 0x29, 0xB0, 0x19, 0x7A, 0xE9, 0xA6, 0x42, 0xC1, 0x73, 0x57, 0x8E, 0xFD, 0x47, 0x84, 0xD1, 0xEE, 0x08, 0x7C, 0xE7, 0x65, 0xA7, 0x14, 0x64, 0x0F, 0x9A, 0xA8, 0x67, 0xA4, 0xAD, 0x87, 0x92, 0x29, 0xF1, 0x71, 0x20, 0x37, 0xD5, 0x22, 0xB5, 0x22, 0x6B, 0x2D, 0xC7, 0x44, 0x0E, 0xFC, 0xB7, 0x53, 0xEC, 0x8A, 0x52, 0xC2, 0x9C, 0xF1, 0xFB, 0x9B, 0xD8, 0x5F, 0xA6, 0x5F, 0xDA, 0x70, 0xB1, 0x26, 0x1E, 0x14, 0x3F, 0x94, 0x06, 0xD0, 0x0D, 0x90, 0xAA, 0x0F, 0x55, 0x31, 0x06, 0x52, 0xF3, 0xF9, 0x08, 0xD7, 0xC1, 0xE5, 0xA8, 0x41, 0xF7, 0x7E, 0xBD, 0x30, 0x14, 0xFC, 0xA2, 0x3C, 0xB2, 0x23, 0xF8, 0x91, 0x5D, 0x77, 0x30, 0xAF, 0xC7, 0x27, 0x6F, 0x1C, 0x0F, 0xC7, 0xEA, 0x33, 0xA3, 0x08, 0x35, 0x53, 0xD2, 0x68, 0x4D, 0x96, 0x4E, 0xC7, 0xE4, 0xA9, 0x20, 0x5D, 0xEE, 0x6F, 0xCF, 0xEA, 0xDA, 0x8B, 0x58, 0x9C, 0xF4, 0x83, 0x26, 0xAF, 0x2D, 0xEB, 0xF5, 0x6D, 0xB4, 0x2A, 0x4D, 0xFD, 0xF7, 0x4B, 0xF9, 0xCB, 0x0A, 0x34, 0xBF, 0xD9, 0x7B, 0x90, 0xB8, 0x3E, 0x17, 0xE3, 0x1F, 0xE0, 0xA4, 0x8B, 0x54, 0xC9, 0x4A, 0xC4, 0x17, 0x5B, 0x46, 0x30, 0x2D, 0x5E, 0x8B, 0x38, 0xD7, 0xCB, 0x42, 0xE6, 0x18, 0xAE, 0xC9, 0x19, 0x7D, 0x43, 0xB1, 0xB3, 0x68, 0x91, 0xA1, 0x8C, 0xDC, 0x5C, 0xA5, 0x7F, 0x20, 0x28, 0x41, 0x87, 0xFE, 0x69, 0x88, 0xD8, 0x60, 0xED, 0x46, 0x07, 0x6F, 0x77, 0x9B, 0x08, 0x8D, 0x2F, 0xA7, 0x8A, 0x79, 0x8A, 0x55, 0xDC, 0xC6, 0xE6, 0x57, 0xE8, 0xB1, 0x01, 0xA2, 0x3B, 0x9F, 0x8A, 0xDE, 0x02, 0xF6, 0x96, 0xD9, 0x05, 0xF6, 0x3C, 0x62, 0x6C, 0x3E, 0x07, 0xFD, 0x06, 0x00, 0x2B, 0x20, 0x30, 0xB2, 0x0F, 0xAF, 0xF0, 0x26, 0x25, 0xD9, 0xB8, 0x75, 0xA4, 0xB7, 0x4D, 0xD4, 0x21, 0xCC, 0xB5, 0x41, 0x1C, 0xC3, 0x09, 0xEB, 0xE7, 0xCC, 0x75, 0xBE, 0xD4, 0x08, 0xF9, 0xF4, 0x86, 0xE6, 0xCF, 0xFF, 0x4F, 0x14, 0xAC, 0x36, 0xDF, 0xFB, 0x64, 0x3C, 0x27, 0x21, 0xA3, 0xAD, 0x4C, 0xA9, 0x54, 0x15, 0xD5, 0x9C, 0xF3, 0xC3, 0xEE, 0x85, 0xFF, 0x75, 0xF2, 0xBC, 0x6F, 0xFD, 0x1F, 0xC0, 0x94, 0x99, 0x54, 0x4B, 0x72, 0x18, 0xF5, 0x93, 0x7E, 0x8B, 0x73, 0xC7, 0x76, 0x4D, 0xEB, 0xC8, 0x40, 0x26, 0x6B, 0x14, 0xF3, 0xD0, 0x49, 0xAE, 0x95, 0x11, 0xAB, 0x13, 0x5C, 0xC7, 0x64, 0xC5, 0xC6, 0xF1, 0x0C, 0x87, 0xC0, 0x87, 0xBC, 0x8D, 0x31, 0x81, 0xD7, 0x47, 0x06, 0x30, 0xD4, 0xA9, 0x83, 0xFE, 0x40, 0x1F, 0x46, 0xC9, 0x9F, 0x4A, 0x52, 0xD8, 0x1E, 0x8D, 0x41, 0x46, 0x21, 0x1B, 0xFA, 0x28, 0xAE, 0x52, 0xC9, 0xD0, 0xE3, 0x97, 0x4A, 0xFB, 0x2D, 0x83, 0x0F, 0x44, 0x31, 0x36, 0xF4, 0x46, 0x4D, 0xDF, 0xEF, 0xA3, 0x06, 0x88, 0xBE, 0x27, 0xA8, 0xA0, 0x15, 0x8A, 0x85, 0xB8, 0x04, 0x0C, 0x2C, 0x04, 0x59, 0x8F, 0x21, 0x11, 0x75, 0x1D, 0x29, 0x6F, 0x86, 0x2F, 0xFE, 0xBC, 0x2F, 0xB5, 0x0D, 0x65, 0x30, 0xFE, 0x6C, 0x09, 0xD7, 0x0F, 0x54, 0x66, 0x4E, 0xD2, 0xF2, 0xC4, 0x43, 0x65, 0xD6, 0x47, 0xB3,
     0xE6, 0xD5, 0xBB, 0x45, 0x70, 0x7C, 0x8B, 0x18, 0xC8, 0xA2, 0x48, 0xB1, 0x53, 0x30, 0x96, 0x05, 0xB3, 0x4E, 0xD9, 0xCE, 0xF4, 0x21, 0x72, 0x11, 0x4F, 0x52, 0xAE, 0x47, 0xE8, 0x06, 0x31, 0x31, 0xEF, 0xB2, 0xF1, 0xAD, 0x55, 0x86, 0x8D, 0x64, 0x87, 0x22, 0x11, 0x1B, 0x00, 0xCF, 0xE2, 0x13, 0x24, 0x63, 0xF9, 0x65, 0x9A, 0xA1, 0xF8, 0x29, 0x8E, 0xD2, 0xFB, 0xD1, 0x23, 0x90, 0x71, 0xDC, 0x3A, 0xCF, 0x63, 0x66, 0x1C, 0x77, 0xA5, 0xAC, 0xBB, 0x54, 0x41, 0x0F, 0xF3, 0xF7, 0xCF, 0xA1, 0x70, 0x10, 0x40, 0xBD, 0x2D, 0x2C, 0x8F, 0x72, 0x1A, 0x37, 0xE3, 0x10, 0xA8, 0x46, 0x05, 0x84, 0x5E, 0x72, 0x02, 0xDB, 0x02, 0x1B, 0x23, 0x46, 0xA1, 0xBB, 0x92, 0x0A, 0xE8, 0x0D, 0xD0, 0x06, 0x6F, 0x05, 0xA0, 0x52, 0x4B, 0xC8, 0x03, 0x39, 0xED, 0x99, 0x32, 0x54, 0x28, 0x83, 0x47, 0x3F, 0xEF, 0xCA, 0x18, 0xC1, 0xC8, 0xB8, 0xC9, 0xB0, 0xE3, 0x1B, 0x71, 0x69, 0xBA, 0xC1, 0xF1, 0xB9, 0x69, 0x7B, 0x27, 0x99, 0xBD, 0xB8, 0x69, 0x00, 0x6C, 0x16, 0xC4, 0x9B, 0x77, 0x52, 0x5A, 0xB7, 0x54, 0x6F, 0xE3, 0x34, 0x5E, 0x5F, 0x01, 0xA5, 0xE2, 0x48, 0xFB, 0x96, 0x6B, 0x75, 0x92, 0xD2, 0xA0, 0xDA, 0x0B, 0xED, 0x3E, 0x27, 0xF6, 0xC7, 0x89, 0x64, 0x7F, 0xDE, 0x73, 0xF5, 0x92, 0x58, 0xFF, 0xC6, 0xA6, 0x38, 0x75, 0x86, 0x61, 0x12, 0x6F, 0xC0, 0x3D, 0x24, 0x22, 0x6D, 0xA7, 0x29, 0x5E, 0xBD, 0xF5, 0x0C, 0x52, 0xD9, 0x66, 0x31, 0xB5, 0x80, 0x4D, 0x02, 0xCD, 0xF2, 0xDC, 0x89, 0xFA, 0x60, 0x63, 0xCA, 0x2D, 0x00, 0x95, 0x32, 0x00, 0xBE, 0xD4, 0xBF, 0x73, 0x4C, 0xED, 0xBA, 0x0C, 0x56, 0xA1, 0x85, 0xC4, 0x6C, 0xB6, 0x0A, 0xBC, 0xDD, 0x8C, 0x61, 0x1E, 0x42, 0x03, 0xB4, 0xE0, 0xF2, 0x17, 0xFA, 0x14, 0x38, 0x9F, 0xB1, 0xA4, 0x9C, 0x03, 0x18, 0x0C, 0xC6, 0x16, 0xC7, 0x30, 0xFA, 0x48, 0xB1, 0xB9, 0x6E, 0xB1, 0x7D, 0x7B, 0x3B, 0xDF, 0xD9, 0xB6, 0xA7, 0xD6, 0x46,
     0xA5, 0x7C, 0x97, 0x6D, 0xD5, 0x92, 0xA3, 0xF0, 0x22, 0xA1, 0x53, 0x99, 0xA1, 0xC3, 0x71, 0x40, 0xE1, 0x89, 0x7B, 0x23, 0x19, 0x18, 0xDC, 0x2F, 0x22, 0x57, 0xDD, 0x2C, 0xC3, 0x3F, 0xAD, 0xEF, 0x99, 0x93, 0x9C, 0xE9, 0xEB, 0x67, 0x66, 0x74, 0x45, 0x8E, 0xD4, 0x87, 0x98, 0x4E, 0x9F, 0x8D, 0x2C, 0x7D, 0xF2, 0x3D, 0x80, 0x93, 0x94, 0x0F, 0xEA, 0xB5, 0x86, 0xD0, 0xE6, 0x74, 0xB6, 0xB2,
     0x41, 0x61, 0x25, 0xDE, 0xD9, 0xC2, 0x38, 0x6A, 0x24, 0x7F, 0x1D, 0x87, 0xBA, 0xD1, 0xCA, 0xB6, 0x40, 0x57, 0x9E, 0xAE, 0x30, 0x50, 0xFF, 0xD0, 0xA8, 0xAE, 0xDF, 0x52, 0x25, 0x4A, 0xA5, 0xE9, 0x18, 0x6F, 0x06, 0x0C, 0x97, 0x15, 0x0E, 0xC2, 0x66, 0x26, 0xCC, 0x84, 0x51, 0xC4, 0x75, 0x69, 0x76, 0x4B, 0x28, 0x16, 0x67, 0xA5, 0x44, 0x28, 0xE0, 0x96, 0xA2, 0x0A, 0x5D, 0x81, 0xEB, 0x4D]
s = [s[i*32:i*32+32] for i in range(len(s)//32)]
c = list(range(48, 124))+[125, 45]
for i in product(c, c, c):
    sha256 = hashlib.sha256()
    sha256.update("".join(map(chr, i)).encode())
    result = sha256.hexdigest()
    result = [int(result[2*i:2*i+2], 16) for i in range(32)]
    for j in range(len(result)):
        result[j] ^= i[j%3]
    try:
        idx = s.index(result)
        s[idx] = "".join(map(chr, i))
    except:
        continue
print(s)
# s = ['-48', '-79', '-80', '-bf', '0bd', '177', '194', '29f', '37-', '39a', '4-7', '48f', '4a3', '7-4', '729', '772', '793', '80b', '8a}', '8fb', '937', '94a', '9a4', '9f8', 'a-8', 'a39', 'a4-', 'ag{', 'b-b', 'bd1', 'bfe', 'd17', 'ea-', 'f8a', 'fb-', 'fea', 'fla', 'g{1', 'lag', '{19']
flag = "fla"
while True:
    i = 0
    while i < len(s):
        if flag[-2:] == s[i][:2]:
            flag += s[i][2]
            break
        i += 1
    if i == len(s):
        break
print(flag)
# "flag{194a39a4-7937-48fb-bfea-80bd17729f8a}"
~~~

## Misc

### 简历

> 本题灵感来源于真实*产样本，flag为c2 ip的md5值。例如ip为127.0.0.1，flag则为flag{f528764d624db129b32c21fbca0cb8d6}

- [ ] solved

给了个exe，一股逆向的味，但不知道怎么找ip，virustotal搜到的ip全md5了一遍也不对

刚才谷歌了下文件名，结果意外发现别的检测病毒平台也上传了这个文件，并检出了好多ip还有一个美国的域名，不知道是不是答案，没法验证了，只能等wp https://any.run/report/e55d3c0a23ae2b25cac5a389147466920f8c82e0f79e6127001a349bfa73f6be/c04d226a-328e-433c-af9e-a7e12f9a7de9

## Crypto

### backdoorplus

> 密码学也有后门吗

- [ ] solved

考察ecdsa，还是不会，回头学点密码学基础知识
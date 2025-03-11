#include<stdio.h>

int main() {
    unsigned int s = 0;
    unsigned long long i;
    for (i = 0; i < 0xffffffff; i++) {
        s = 0x811C9DC5;
        for (int j = 0; j < 4; j++) {
            unsigned char v = i >> (j * 8);
            if (v % 2) 
                s ^= v;
            else
                s *= 16777619;
            s = (s >> 25) | (s << 7);
            s -= v;
        }
        if (s == 0x45E938F6) {
            printf("password: %ld\n", i);
            break;
        }
    }
    unsigned char cmp[32] = {0x54, 0x55, 0x79, 0x9E, 0xA8, 0xE1, 0x1C, 0xDA, 0x04, 0x1D, 0xC1, 0x6E, 0x80, 0x82, 0x0D, 0x8A, 0x4C, 0x65, 0xE1, 0x46, 0x71, 0x31, 0xED, 0xD2, 0x14, 0xC5, 0x39, 0xB5, 0x49, 0xE2, 0x04, 0xA9};
    for (int j = 0; j < 32; j++) {
        cmp[j] -= j;
        cmp[j] = (cmp[j] << 5) | (cmp[j] >> 3);
        cmp[j] ^= j ^ (i >> (((3 - j % 4)) * 8));
        printf("%c", cmp[j]^(8*0xe9)&0xff);
    }
}
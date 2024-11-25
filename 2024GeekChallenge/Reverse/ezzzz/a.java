public class a {
    public static String encrypt(String arg7) {
        int v0 = arg7.length();
        int[] v1 = new int[v0];
        int v2 = 0;
        int v3;
        for(v3 = 0; v3 < v0; ++v3) {
            v1[v3] = arg7.charAt(v3);
        }

        int[] v3_1 = new int[4];
        int v4;
        for(v4 = 0; v4 < 4; ++v4) {
            v3_1[v4] = "GEEK".charAt(v4);
        }

        int v7;
        for(v7 = 0; v7 < v0; v7 += 2) {
            int v5 = v7 + 1;
            int[] v4_1 = {v1[v7], v1[v5]};
            a.encrypt(v4_1, v3_1);
            v1[v7] = v4_1[0];
            v1[v5] = v4_1[1];
        }

        StringBuilder v7_1 = new StringBuilder();
        while(v2 < v0) {
            v7_1.append(String.format("%08x", ((int)v1[v2])));
            ++v2;
        }

        return v7_1.toString();
    }

    private static void encrypt(int[] arg8, int[] arg9) {
        int v1 = arg8[0];
        int v3 = arg8[1];
        int v4 = 0;
        int v5 = 0;
        while(v4 < 0x20) {
            v1 += (v3 << 4 ^ v3 >> 5) + v3 ^ arg9[v5 & 3] + v5 ^ v5 + v4;
            v5 -= 1640531527;
            v3 += (v1 << 4 ^ v1 >> 5) + v1 ^ arg9[v5 >>> 11 & 3] + v5 ^ v5 + v4;
            ++v4;
        }
        arg8[0] = v1;
        arg8[1] = v3;
    }

    public static String decrypt() {
        int[] v1 = new int[]{0xf1f186b2, 0x5a96c782, 0xe6c63a0b, 0x70b61b5c, 0xed6bf848, 0x89700d6b, 0x09381b5c, 0xcb2f24fa, 0xb1c79e79, 0x6d822d9c, 0xdcc55f76, 0x0f780e75, 0x0d65c4af, 0xb89084a9, 0xe978c382, 0x7a8dd810, 0x91f28df3, 0xa84dbaca, 0xb4d75f75, 0xf19af8e5, 0xb90f80fc, 0xfc10a5c3, 0xd20679fb, 0x2bc734c8, 0xccb31c92, 0x1ac52ad3, 0xe7f922b7, 0x2e24d923, 0xfb4ce9f5, 0x3548a9e5, 0x71ebc25a, 0xdf38862e, 0x10059186, 0x32750946, 0x3dd4d54c, 0x905abc36, 0xc26d5312, 0xd2cd42c0, 0x772d99e5, 0x0cd4c466, 0x5c3178d6, 0x3a7ffe71, 0xada251c0, 0x70568d5a, 0x5798c292, 0x1ec0f7fc, 0x3ae9d841, 0x84607629, 0x30ca6a2d, 0xccef51d2, 0xa1a80854, 0x91b0f82d, 0x686ca347, 0x74c52d0f, 0x0f26449f, 0xc28d362c, 0x86f3311b, 0x8adc4fb1, 0xa4497e34, 0xe0f0915d};
        int v0 = v1.length;
        int v2 = 0;


        int[] v3_1 = new int[4];
        int v4;
        for(v4 = 0; v4 < 4; ++v4) {
            v3_1[v4] = "GEEK".charAt(v4);
        }

        int v7;
        for(v7 = 0; v7 < v0; v7 += 2) {
            int v5 = v7 + 1;
            int[] v4_1 = {v1[v7], v1[v5]};
            a.decrypt(v4_1, v3_1);
            v1[v7] = v4_1[0];
            v1[v5] = v4_1[1];
        }
        StringBuilder v7_1 = new StringBuilder();
        while(v2 < v0) {
            v7_1.append(((char)v1[v2]));
            ++v2;
        }

        return v7_1.toString();
    }

    private static void decrypt(int[] arg8, int[] arg9) {
        int v1 = arg8[0];
        int v3 = arg8[1];
        int v4 = 0x1f;
        int v5 = -957401312;
        while(v4 >= 0) {
            v3 -= (v1 << 4 ^ v1 >> 5) + v1 ^ arg9[v5 >>> 11 & 3] + v5 ^ v5 + v4;
            v5 += 1640531527;
            v1 -= (v3 << 4 ^ v3 >> 5) + v3 ^ arg9[v5 & 3] + v5 ^ v5 + v4;
            --v4;
        }
        arg8[0] = v1;
        arg8[1] = v3;
    }

    public static void main(String[] args) {
        System.out.println(a.encrypt("12"));
        System.out.println(a.decrypt());
    }

}


import java.util.*;

public class Burgers {

    public static char[] bun(char[] s) {
        for (int i = 0; i < 7; i++) {
            s[i] = "LITCTF{".toCharArray()[i];
        }
        s[s.length - 1] = '}';
        return s;
    }

    public static char[] cheese(char[] s) {
        s[13] = '_';
        s[17] = 95;
        s[19] = '_';
        s[26] = (char) (190-s[19]);
        s[29] = '_';
        s[34] = 95;
        s[39] = '_';
        return s;
    }

    public static char[] meat(char[] s) {
        int m = 41;
        char[] meat = {'n', 'w', 'y', 'h', 't', 'f', 'i', 'a', 'i'};
        int[] dif = {4, 2, 2, 2, 1, 2, 1, 3, 3};
        for (int i = 0; i < meat.length; i++) {
            m -= dif[i];
            s[m] = meat[i];
        }
        return s;
    }

    public static char[] pizzaSauce(char[] s) {
        boolean[] isDigit = {false, false, false, true, false, true, false, false, true, false, false, false, false, false};
        char[] sauce = {'b', 'p', 'u', 'b', 'r', 'n', 'r', 'c'};
        int a = 7; int b = 20; int i = 0;
        while (a < b) {
            s[a] = sauce[i];
            s[b] = sauce[i+1];
            a++; b--; i += 2;
            while (isDigit[a-7] || s[a]=='_') a++;
            while (isDigit[b-7] || s[b]=='_') b--;
        }
        return s;
    }

    public static char[] veggies(char[] s) {
        int[] veg1 = {10, 12, 15, 22, 23, 25, 32, 36, 38, 40};
        int[] veg = new int[10];
        veg[0] = 9;
        veg[1] = 5;
        veg[2] = 4;
        veg[4] = 2;
        veg[3] = 2;
        veg[5] = 5;
        veg[6] = 3;
        veg[7] = 4;
        veg[8] = 7;
        veg[9] = 2;
        for (int i = 0; i < 10; i++) {
            s[veg1[i]] = (char) (veg[i] + '0');
        }
        return s;
    }

    public static void main(String[] args) {
        char[] input = new char[42];
        input = bun(input);
        input = cheese(input);
        input = meat(input);
        input = veggies(input);
        input = pizzaSauce(input);
        System.out.println(new String(input));
    }
}

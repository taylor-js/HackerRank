import java.io.*;
import java.util.*;

public class Reverse {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        
        sc.close();
        System.out.println(stringReverse(A));
    }
    public static String stringReverse(String A){
        int i = 0;
        char[] my_chars = A.toCharArray();
        int len = my_chars.length;
        String res = null;
        while (i < len){
            if (my_chars[i] == my_chars[len-1-i]){
                res = "Yes";
            }
            else{
                res = "No";
            }
            i += 1;
        }
        return res;
    }
}


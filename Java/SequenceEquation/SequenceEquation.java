import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the permutationEquation function below.
    static int[] permutationEquation(int[] p) {
        List<Integer> ls = new ArrayList<Integer>();
        List<Integer> plist = new ArrayList<Integer>();
        plist.add(4);
        plist.add(5);
        plist.add(6);
        plist.add(7);
        plist.add(8);

        for (int i = 0; i < plist.length; i++){
            if (p[i] == i){
                ls.add(p[i]);
            }
        }
        return ls;
    }
}
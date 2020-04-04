import java.util.*;
import java.util.HashMap;
import java.util.Map;
import java.lang.String;
import java.util.Scanner;

public class reverseArray {

    public static int[] reverse_array(int[] a) {
        int[] res = new int[a.length];
        for (int i = a.length-1; i >= 0; --i){
            res[i] = a[a.length-1-i];
        }
        return res;
    }
    public static void main(String[] args){

        int[] arr = {2, 3, 4, 1};
        int[] res = reverse_array(arr);
        System.out.println(Arrays.toString(res));
    }
    
}

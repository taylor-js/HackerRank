import java.util.*;
import java.util.Scanner;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Collections;
import java.util.SortedSet;


public class Formatting {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Map<String, Integer> hm = new HashMap<String, Integer>();
        Map<String, Integer> hm = new LinkedHashMap<String, Integer>();

        for (int i = 0; i < 3; ++i) {
            String s1 = sc.next();
            int x = sc.nextInt();
            hm.put(s1, x);
        }

        System.out.println("================================");
        for (Map.Entry<String,Integer> entry : hm.entrySet()){
            String line = String.format("%1$-15s", entry.getKey()) + String.format("%03d", entry.getValue());
            System.out.println(line);
        }
        System.out.println("================================");
        sc.close();
    }
}

// hello 0
// hackerrank 65
// java 10
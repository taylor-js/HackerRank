import java.io.*;
import java.util.*;

public class EndofFile {
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        HashMap<Integer, String> newmap = new HashMap<Integer, String>(); 
        for(int i = 0; i <= n; ++i){
            scan.next();
            String str = scan.nextLine();
            newmap.put(i,str);
        }
        for(int i = 1; i < newmap.size(); ++i){
            System.out.println(i+" "+newmap.get(i));
        }
        scan.close();
    }
}
import java.util.*;
import java.io.*;


class Solution{
    public static void main(String []args){

        Scanner in = new Scanner(System.in);
        List<List<Integer>> outputs = new ArrayList<List<Integer>>();
        int q = in.nextInt();
        for(int k = 0; k < q; ++k) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            outputs.add(Function(a,b,n));
        }
        in.close();

        for (List<Integer> item : outputs) {
            String str = "";
            for (int j = 0; j < item.size(); ++j){
                str += item.get(j).toString() + " ";
            }
            System.out.println(str.trim());
        }
    }
    public static List<Integer> Function(int a, int b, int n){
        List<Integer> array = new ArrayList<>();
        int fb = 0;
        for(int i = 0; i < n; ++i) {
            fb += (int)Math.pow(2,i) * b;
            array.add(a + fb);
        }
        return array;
    }
}

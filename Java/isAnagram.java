import java.util.Scanner;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class isAnagram {
    static boolean anagram(String a, String b) 
	{ 

		HashMap<Character, Integer> map_a = new HashMap<Character, Integer>(); 
		HashMap<Character, Integer> map_b = new HashMap<Character, Integer>(); 

		char arr_a[] = a.toCharArray(); 
		char arr_b[] = b.toCharArray(); 

		for (int i = 0; i < arr_a.length; i++) { 

			if (map_a.get(arr_a[i]) == null) { 

				map_a.put(arr_a[i], 1); 
			} 
			else { 
				Integer c = (int)map_a.get(arr_a[i]);
				map_a.put(arr_a[i], ++c); 
			} 
		} 

		for (int j = 0; j < arr_b.length; j++) { 

			if (map_b.get(arr_b[j]) == null) 
            map_b.put(arr_b[j], 1); 
			else { 

				Integer d = (int)map_b.get(arr_b[j]); 
				map_b.put(arr_b[j], ++d); 
			} 
		} 

		if (map_a.equals(map_b)) 
			return true; 
		else
			return false; 
	}
    
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = anagram(a, b);
        System.out.println((ret) ? "Anagrams" : "Not Anagrams");
    }

}

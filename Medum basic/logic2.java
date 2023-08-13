//input a4k3b2
 //output aeknbd

import java.util.Scanner;

public class logic2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String str=sc.next();
        char[] ch=str.toCharArray();
        for(int i=0;i<ch.length;i++){
            if(Character.isLetter(ch[i])){
                System.out.print(ch[i]);
            }
            else{
                int n=Character.getNumericValue(ch[i]);
                int pos=ch[i-1];
                System.out.print((char)pos);
            }
        }
    }
}

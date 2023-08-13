import java.util.*;

public class logicbased{
    
 public static void main(String[] args) {
    Scanner scs=new Scanner(System.in);
 String str=scs.next();
 
    char[] ch=str.toCharArray();
    
    for(int i=0;i<ch.length;i++){
         if(Character.isLetter(ch[i])){
               System.out.print(ch[i]);
         }
         else{
               int n=Character.getNumericValue(ch[i]);
               for(int j=0;j<n;j++){
                  System.out.print(ch[i-1]);
               }
         }
    }
 
 }
}

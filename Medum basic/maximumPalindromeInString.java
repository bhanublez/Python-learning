import java.util.Scanner;

public class maximumPalindromeInString {
    
    public static void main(String[] args) {
        String scs="nayannamantenet";
        int max=0;
        for(int i=0;i<scs.length();i++){
            for(int j=i+1;j<scs.length();j++){
                String s=scs.substring(i,j);
                if(isPalindrome(s)){
                    if(s.length()>max){
                        max=s.length();
                    }
                }
            }
        }
        

    }

    private static boolean isPalindrome(String s) {
        int i=0;
        int j=s.length()-1;
        while(i<j){
            if(s.charAt(i)!=s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}

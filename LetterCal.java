import java.util.*;

public class LetterCal{
    public static void main(String[]args){
        Scanner s=new Scanner(System.in);
        System.out.println("enter an String");
        String a=s.nextLine();
        int lett=0;
        int digi=0;
        int space=0;
        for(int i=0;i<a.length();i++){
            char ch=a.charAt(i);
            if(Character.isLetter(ch)){
                lett++;
            }
            else if(Character.isDigit(ch)){
                digi++;
            }
            else if(Character.isWhitespace(ch)){
                space++;
            }
        }
        System.out.println("the String You entered is ="+a);
        System.out.println("the number of digits in String ="+digi);
        System.out.println("the number of letters in string ="+lett);
        System.out.println("the number white Spaces is ="+space);
    }
}

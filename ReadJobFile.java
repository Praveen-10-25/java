import java.io.*;

public class ReadJobFile {
    public static void main(String[] args) {
        String filename = "jobfile.txt";

        try {
            BufferedReader a = new BufferedReader(new FileReader(filename));
            String line;
            System.out.println("File content:");
            while ((line = a.readLine()) != null) {
                System.out.println(line);
            }
           a.close();
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);
        
        sprunglibar(n, m);

        bufferedReader.close();
    }
    
    public static void sprunglibar(int n, int m) {
        int[][] best = new int[n+1][m+1];
        String[][] choices = new String[n+1][m+1];
       
        for(int i=0; i<=n; i++)
        {
            for(int j=0; j<=m; j++)
            {
                choices[i][j] = "";
                if(i == j)
                {
                   best[i][j] = 0;
                   continue;
                }
                best[i][j] = Integer.MAX_VALUE;
            }
        }
       
        for(int j = 1; j <= n; j++)
        {
            for(int k = 1; k <= m; k++)
            {
                for(int i = 1; i <= j/2; i++)
                {
                    if((1 + best[i][k] + best[j-i][k]) < best[j][k])
                    {
                        best[j][k] = 1 + best[i][k] + best[j-i][k];
                        choices[j][k] =  "H " + j + "x" + k + " --> " + i + "x" + k + " " + (j-i) + "x" + k + "\n" + choices[i][k] + choices[j-i][k];
                    }
                }
                 
                for(int i = 1; i <= k/2; i++)
                {
                    if(1 + best[j][i] + best[j][k-i] < best[j][k])
                    {
                        best[j][k] = 1 + best[j][i] + best[j][k-i];
                        choices[j][k] =  "V " + j + "x" + k + " --> " + j + "x" + i + " " + j + "x" + (k-i) + "\n" + choices[j][i] + choices[j][k-i];                    
                    }
                }
            }
        }
    
        System.out.println(best[n][m]);
        System.out.println(choices[n][m]);
}

}

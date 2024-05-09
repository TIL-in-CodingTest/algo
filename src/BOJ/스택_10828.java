package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 스택_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();

        int n = Integer.parseInt(br.readLine()); //개수

        for (int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            if (str.equals("push")){
                stack.push(Integer.parseInt(st.nextToken()));
            }
            if (str.equals("pop")){
                if (stack.isEmpty()){
                    sb.append(-1 + "\n");
                } else {
                    sb.append(stack.pop() + "\n");
                }
            }
            if (str.equals("top")){
                if (stack.isEmpty()){
                    sb.append(-1 + "\n");
                } else {
                    sb.append(stack.peek() + "\n");
                }
            }
            if (str.equals("size")){
                sb.append(stack.size() + "\n");
            }
            if (str.equals("empty")){
                if (stack.isEmpty()){
                    sb.append(1 + "\n");
                }
                else {
                    sb.append(0 + "\n");
                }
            }
        }

        //출력
        System.out.println(sb);
    }
}
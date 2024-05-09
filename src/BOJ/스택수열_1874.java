package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 스택수열_1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        // 스택 생성
        Stack<Integer> stack = new Stack<>();

        // n 입력
        int n = Integer.parseInt(br.readLine());

        int start = 1; // 스택에 1부터 저장(문제 : 1부터 N까지의 수를 스택에 넣었다가)
        for (int i=0; i<n; i++){
            int value = Integer.parseInt(br.readLine());
            // 입력한 숫자가 시작 숫자보다 크면
            if (value >= start){
                for (int num = start; num <= value; num ++){
                    stack.push(num);
                    sb.append("+" + "\n");
                }
                start = value +1;
            }
            // stack의 맨 위 숫자과 입력한 숫자가 다르면 (pop해야되는데 다르니까 NO)
            else if (stack.peek() != value){
                System.out.println("NO");
                System.exit(0);
            }
            stack.pop();
            sb.append("-" + "\n");
        }
        System.out.println(sb);
    }
}

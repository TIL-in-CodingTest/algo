package 이코테.binarySearch;

import java.util.Arrays;
import java.util.Scanner;

/**
 * 부품 : N개, 부품 배열 : []
 * 손님 찾는 부품 : M개, 손님 찾는 부품 배열 : []
 */
public class 부품찾기 {
    /**
     * 순차 탐색으로 푼 내 풀이
     */
    public static String search(int n, int[] arr, int target){
        for (int i=0; i<n; i++){
            if (arr[i] == target){
                return "yes";
            }
        }
        return "no";
    }
    public static void search_main (String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        int m = sc.nextInt();
        for (int j=0; j<m; j++){
            System.out.println(search(n, arr, sc.nextInt()));
        }
    }

    /**
     * 이진 탐색으로 푼 책 코드
     */
    public static int binarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = (start + end) / 2;
            // 찾은 경우 중간점 인덱스 반환
            if (arr[mid] == target) return mid;
            // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            else if (arr[mid] > target) end = mid - 1;
            // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else start = mid + 1;
        }
        return -1;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        // N : 가게의 부품 개수
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        // 이진 탐색을 위해 사전에 정렬 수행
        Arrays.sort(arr);

        // M : 손님이 확인 요청한 부품 개수
        int m = sc.nextInt();
        int[] targets = new int[m];
        for (int i=0; i<m; i++){
            targets[i] = sc.nextInt();
        }

        // 손님이 확인 요청한 부품 번호를 하나씩 확인
        for (int i = 0; i < m; i++) {
            // 해당 부품이 존재하는지 확인
            int result = binarySearch(arr, targets[i], 0, n - 1);
            if (result != -1) {
                System.out.print("yes ");
            }
            else {
                System.out.print("no ");
            }
        }
    }
}

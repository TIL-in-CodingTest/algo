package 이코테.binarySearch;
import java.util.Scanner;
/**
 * 이진탐색 시간 복잡도 : O(logN)
 */
public class 이진탐색_반복문 {
    public static int binarySearch(int[] arr, int target, int start, int end){
        while (start <= end){
            int mid = (start + end) / 2;
            // 찾은 경우 중간점 인덱스 반환
            if (arr[mid] == target) return mid;
            // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            else if (arr[mid] > target) end = mid-1;
            // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else start = mid +1;
        }
        return -1;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        // 원소의 개수 : n, 찾고자 하는 값 : target
        int n = sc.nextInt();
        int target = sc.nextInt();

        // 전체 원소 입력받기
        int[] arr = new int[n];
        for (int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        // 이진 탐색 수행 결과 출력
        int result = binarySearch(arr, target, 0, n-1);
        if (result == -1){
            System.out.println("원소가 존재하지 않습니다.");
        }
        else {
            System.out.println(result+1);
        }

    }
}

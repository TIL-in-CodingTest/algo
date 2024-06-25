package BOJ.binarySearch;

import java.util.Arrays;
import java.util.Scanner;

/**
 * 백준 2295 - 골드 4
 * N 개의 자연수들로 이루어진 집합 U
 * 고른 세 수 중에 가장 큰 d 찾기
 */
public class 세수의합 {
    public static boolean binarySearch(int[] arr, int a){
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (a > arr[mid]) {
                left = mid + 1;
            } else if (a < arr[mid]) {
                right = mid - 1;
            } else if (a == arr[mid]) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        int[] ab = new int[arr.length * (arr.length +1) /2];
        int idx = 0;
        for (int i=0; i<arr.length; i++){
            for (int j=i; j< arr.length; j++){
                ab[idx++] = arr[i] + arr[j];
            }
        }
        Arrays.sort(ab);

        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (binarySearch(ab, arr[i] - arr[j])) {
                    result = Math.max(result, arr[i]);
                }
            }
        }
        System.out.println(result);
    }
}

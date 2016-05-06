package com.company;

//Problem description
//Write a function that takes a string as input and reverse only the vowels of a string.
//
//        Example 1:
//        Given s = "hello", return "holle".
//
//        Example 2:
//        Given s = "leetcode", return "leotcede".

public class Question345 {

    public static void main(String[] args) {

        String sample = "aufviedersehn";//eefveidursahn
        String result = reversedString(sample);
        System.out.println("\r\n");
        System.out.println(result);
    }

    private static String reversedString(String originalString){

        char arr[] = originalString.toCharArray();
        StringBuilder builder = new StringBuilder();

        int forwardIndex = 0;
        int backwardIndex = arr.length - 1;

        while(forwardIndex != arr.length) {

            if(isVowel(arr[forwardIndex])) {
                if(isVowel(arr[backwardIndex])) {
                    builder.append(arr[backwardIndex]);
                    System.out.print(arr[backwardIndex]);
                    forwardIndex++;
                }
                backwardIndex--;
            } else {
                System.out.print(arr[forwardIndex]);
                builder.append(arr[forwardIndex]);
                forwardIndex++;
            }
        }
        return builder.toString();
    }

    private static boolean isVowel(char c) {
        return "aeiou".contains(String.valueOf(c).toLowerCase());
    }

}

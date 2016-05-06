package com.company;

/*
    Write a function that takes a string as input and returns the string reversed.

    Example:
    Given s = "hello", return "olleh".

    Subscribe to see which companies asked this question
*/
public class Question344 {

    public static void main(String[] args) {
        String target = "hello";
        System.out.println(reverseString(target)); //should be "olleh"

        target = "welcome";
        System.out.println(reverseString(target)); //should be "emoclew"

        target = "system";
        System.out.println(reverseString(target)); //should be "metsys"
    }

    public static String reverseString(String original){
        int swapCount = original.length() / 2;
        char[] arr = original.toCharArray();
        int backIndex = original.length() - 1;
        for(int i = 0; i < swapCount; i++) {
            swap(arr, i, backIndex);
            backIndex--;
        }

        return printArrayToString(arr);
    }

    private static String printArrayToString(char[] array) {
        StringBuilder builder = new StringBuilder();
        for (char c : array) {
            builder.append(c);
        }
        return builder.toString();
    }

    public static char[] swap(char[] original, int front, int back){
        char temp = original[front];
        original[front] = original[back];
        original[back] = temp;
        return original;
    }

}

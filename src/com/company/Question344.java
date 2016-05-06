package com.company;

/*
    Write a function that takes a string as input and returns the string reversed.

    Example:
    Given s = "hello", return "olleh".

    Subscribe to see which companies asked this question
*/
public class Question344 {

    public String reverseString(String original) {
        int swapCount = original.length() / 2;
        char[] arr = original.toCharArray();
        int backIndex = original.length() - 1;
        for (int i = 0; i < swapCount; i++) {
            swap(arr, i, backIndex);
            backIndex--;
        }

        return printArrayToString(arr);
    }

    private String printArrayToString(char[] array) {
        StringBuilder builder = new StringBuilder();
        for (char c : array) {
            builder.append(c);
        }
        return builder.toString();
    }

    private char[] swap(char[] original, int front, int back) {
        char temp = original[front];
        original[front] = original[back];
        original[back] = temp;
        return original;
    }

}

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:32:33 2018

@author: shaurmanchic
"""
import string
import random


def hello(word):
    """
    1. Define a function, that takes string 
    as argument and prints "Heelo, %arg%!
    """
    print("Hello {}".format(word))


def sum(number_list):
    """
    2.Define a function sum() and a function multiply() that sums and 
    multiplies (respectively) all the numbers in a list of numbers. 
    For example, sum([1, 2, 3, 4]) 
    should return 10, and multiply([1, 2, 3, 4]) should return 24.
    """
    sum = 0
    for number in number_list:
        sum += number
    return sum


def multiply(number_list):
    """
    2.Define a function sum() and a function multiply() that sums and 
    multiplies (respectively) all the numbers in a list of numbers. 
    For example, sum([1, 2, 3, 4]) 
    should return 10, and multiply([1, 2, 3, 4]) should return 24.
    """
    if len(number_list) == 0:
        return 0
    multiply = 1
    for number in number_list:
        multiply *= number
    return multiply


def reverse(word):
    """
    3.Define a function reverse() that computes the reversal of a string. 
    For example, reverse("I am testing") should return 
    the string "gnitset ma I".
    """
    return word[::-1]
    

def is_palindrome(word):
    """
    4. Define a function is_palindrome() that recognizes palindromes 
    (i.e. words that look the same written backwards). 
    For example, is_palindrome("radar") should return True.
    """
    return word == word[::-1]


def histogram(levels):
    """
    5. Define a function histogram() that takes a list of integers and prints 
    a histogram to the screen. For example, histogram([4, 9, 7]) should 
    print the following:
    ****
    *********
    ******
    (usage time.sleep(s) possible for better visualization)
    """
    for height in levels:
        print("*" * height)


def ceasar_cipher(original, key):
    """
    6.Define a function caesar_cipher that takes string and key(number), 
    which returns encrypted string
    """
    uppercase_alphabet = string.ascii_uppercase
    lowercase_alphabet = string.ascii_lowercase
    encrypted = ""
    
    for letter in original:
        if letter in uppercase_alphabet:
            letter = chr(ord(letter) + key)
            if ord(letter) > 90:
                letter = chr(ord(letter) - 26)
            encrypted += letter
            
        elif letter in lowercase_alphabet:
            letter = chr(ord(letter) + key)
            if ord(letter) > 122:
                letter = chr(ord(letter) - 26)
            encrypted += letter
        else:
            encrypted += letter
    
    return encrypted


def diaginal_reverse(matrix):
    """
    7.define a function diaginal_reverse() that takes matrix and returns 
    diagonal-reversed one:
    1 2 3         1 4 7
    4 5 6 returns 2 5 8
    7 8 9         3 6 9
    """
    reversed_matrix = []
    for i in range(0, len(matrix)):
        reversed_matrix.append([])
        for j in matrix:
            reversed_matrix[i].append(j[i])
            
    return reversed_matrix


def game(lo, hi):
    """
    8. Write a function game() number-guessing game, that takes 2 int 
    parameters defining the range. Using random.randint(A, B) generate 
    random int from the range. 
    While user input isn't equal that number, print "Try again!". 
    If user guess the number, congratulate him and exit. (use raw_input())
    """
    answer = ''
    secret_number = random.randint(lo, hi)
    print("Please guess a number between {} and {}!".format(lo, hi))
    while True:
        #all inputs are raw in python 3
        answer = int(input('Your answer: ')) 
        if answer == secret_number:
            print("You've won! Congratulations!")
            break
        else:
            print('Try again!')


def nesting_balance(bracket_string):
    """
    9.Define a function, which takes a string with N opening brackets ("[") 
    and N closing brackets ("]"), in some arbitrary order.
    Determine whether the generated string is balanced; that is, whether 
    it consists entirely of pairs of opening/closing brackets (in that order), 
    none of which mis-nest.
    Examples:
       []        OK   ][        NOT OK
       [][]      OK   ][][      NOT OK
       [[][]]    OK   []][[]    NOT OK
    """
    brackets = '[]'
    bracket_copy = bracket_string
    
    while brackets in bracket_copy:
        bracket_copy = bracket_copy.replace(brackets, '')
    
    print(bracket_copy)
    return not bracket_copy
    

def char_freq(string):
    """
    10. Write a function char_freq() that takes a string and builds a 
    frequency listing of the characters contained in it. Represent the 
    frequency listing as a Python dictionary. Try it with something like 
    char_freq("abbabcbdbabdbdbabababcbcbab").
    """
    char_dict = {}
    for letter in string:
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1
    
    return char_dict


def dec_to_bin(decimal):
    """
    11. Write a function dec_to_bin() that takes decimal integer and outputs 
    its binary representation.
    """
    binary = []
    result = ''
    while decimal > 0:
        binary.append(decimal % 2)
        decimal //=2
    
    for number in binary[::-1]:
        result += str(number)
        
    return  result


def ship_battle_game(size):
    """
    12. Write a ship battle game, which is similar to ex.8, except it takes 
    1 integer as an order of matrix, randomly generates index (x, y) and 
    checks user input (2 integers).
    (tip: use var1, var2 = raw_input("Enter two numbers here: ").split())
    *Visualize the game.
    """
    answers = []
    secret_numbers = random.randint(1, size), random.randint(1, size)
    while True:
        for row in range(1, size + 1):
            for column in range(1, size + 1):
                if (row, column) in answers:
                    print('*', end='')
                else:
                    print('-', end='')
            print('\r')
            
        try:
            answer = list(map(int, input('Enter two numbers here: ').split()))
            if answer in answers:
                print("You've already used this combination!\n")
            if all(digit > 0 and digit <= size for digit in answer):
                if len(answer) == 2:
                    answers.append(tuple(answer))
                else:
                    print("Please make sure that you've entered 2 numbers!\n")
            else:
                print('Input out of bounds!\n')
                continue
        except:
            print('Invalid input!\n')
        if secret_numbers in answers:
            print("You've won! Congratulations!\n")
            break
        else:
            print('Try again!\n')
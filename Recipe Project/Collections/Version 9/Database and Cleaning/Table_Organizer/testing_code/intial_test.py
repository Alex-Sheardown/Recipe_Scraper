
import os
import pandas as pd
import Linkchecker as lc

test_decimal_conversion = False
test_measurement_finder = True


test_cases1 = [
    ("This is ⅒ of a whole.", "this is 0.1 of a whole."),  # Test 1
    ("1 ⅓ cups of sugar", "1.3333333333333333 cups of sugar"),  # Test 2
    ("2 ½ teaspoons of salt", "2.5 teaspoons of salt"),  # Test 3
    ("⅗ of the pie", "0.6 of the pie"),  # Test 4
    ("3 ⅝ hours", "3.625 hours"),  # Test 5
    ("⅙ of a pizza", "0.16666666666666666 of a pizza"),  # Test 6
    ("4 ¾ miles", "4.75 miles"),  # Test 7
    ("⅞ of the cake", "0.875 of the cake"),  # Test 8
    ("⅓ cup of flour", "0.3333333333333333 cup of flour"),  # Test 9
    ("2 ¼ pounds of apples", "2.25 pounds of apples"),  # Test 10
    ("¾ teaspoon of salt", "0.75 teaspoon of salt"),  # Test 11
    ("5 ⅝ meters of fabric", "5.625 meters of fabric"),  # Test 12
    ("⅛ of the pizza", "0.125 of the pizza"),  # Test 13
    ("3 ⅞ hours", "3.875 hours"),  # Test 14
    ("⅕ of a cake", "0.2 of a cake"),  # Test 15
    ("1 ⅝ inches", "1.625 inches"),  # Test 16
    ("⅙ of a pie", "0.16666666666666666 of a pie"),  # Test 17
    ("4 ⅕ tablespoons of sugar", "4.2 tablespoons of sugar"),  # Test 18
    ("⅜ of the cookies", "0.375 of the cookies"),  # Test 19
    ("7 ⅓ ounces of chocolate", "7.333333333333333 ounces of chocolate"),  # Test 20
    ("⅞ of the cake", "0.875 of the cake"),  # Test 21
    ("9 ½ cups of coffee", "9.5 cups of coffee"),  # Test 22
    ("⅗ of a pizza", "0.6 of a pizza"),  # Test 23
    ("12 ⅝ yards of fabric", "12.625 yards of fabric"),  # Test 24
    ("⅝ of a cake", "0.625 of a cake"),  # Test 25
    ("10 ⅓ tablespoons of flour", "10.333333333333334 tablespoons of flour"),  # Test 26
    ("⅓ of a pound of cheese", "0.3333333333333333 of a pound of cheese"),  # Test 27
    ("2 ⅛ cups of milk", "2.125 cups of milk"),  # Test 28
    ("⅞ of a pizza", "0.875 of a pizza"),  # Test 29
    ("3 ⅜ teaspoons of salt", "3.375 teaspoons of salt"),  # Test 30
    ("⅕ of a pie", "0.2 of a pie"),  # Test 31
    ("5 ⅝ pounds of apples", "5.625 pounds of apples"),  # Test 32
    ("⅙ of a gallon of juice", "0.16666666666666666 of a gallon of juice"),  # Test 33
]
test_cases2 = [
    ("⅒ of a whole.", "0.1 of a whole."),  # Test 1
    ("1 ⅓ cups of sugar", "1.3333333333333333 cups of sugar"),  # Test 2
    ("2 ½ teaspoons of salt", "2.5 teaspoons of salt"),  # Test 3
    ("⅗ of the pie", "0.6 of the pie"),  # Test 4
    ("3 ⅝ hours", "3.625 hours"),  # Test 5
    ("⅙ of a pizza", "0.16666666666666666 of a pizza"),  # Test 6
    ("4 ¾ miles", "4.75 miles"),  # Test 7
    ("⅞ of the cake", "0.875 of the cake"),  # Test 8
    ("⅝ of a cake", "0.625 of a cake"),  # Test 9
    ("10 ⅓ tablespoons of flour", "10.333333333333334 tablespoons of flour"),  # Test 10
    ("⅓ of a pound of cheese", "0.3333333333333333 of a pound of cheese"),  # Test 11
    ("2 ⅛ cups of milk", "2.125 cups of milk"),  # Test 12
    ("⅞ of a pizza", "0.875 of a pizza"),  # Test 13
    ("3 ⅜ teaspoons of salt", "3.375 teaspoons of salt"),  # Test 14
    ("⅕ of a pie", "0.2 of a pie"),  # Test 15
    ("5 ⅝ pounds of apples", "5.625 pounds of apples"),  # Test 16
    ("⅙ of a gallon of juice", "0.16666666666666666 of a gallon of juice"),  # Test 17
    ("⅓ ⅖ ⅗ ⅘ ⅙ ⅐ ⅛ ⅑ ⅒", "0.3333333333333333 0.4 0.6 0.8 0.16666666666666666 0.14285714285714285 0.125 0.1111111111111111 0.1"),  # Test 18
    ("1 ⅜ 2 ½ 3 ⅝ 4 ¾ 5 ⅝ 6 ⅞ 7 ⅐ 8 ⅛ 9 ⅑ 10 ⅒", "1.375 2.5 3.625 4.75 5.625 6.875 7.142857142857143 8.125 9.11111111111111 10.1"),  # Test 19
    ("⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛ ⅛", "0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125 0.125"),  # Test 20
]

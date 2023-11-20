
#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

prime = True

number = int(input('Input number to test: '))

counter = 2
while counter < number - 1 and prime == True:
    modulus = number % counter
    if modulus == 0:
        prime = False
    counter = counter + 1

if prime == True:
    print('Your number is PRIME')
else:
    print('Your number is NOT PRIME')

#!/usr/bin/python3.10.10
# -*- encoding: utf-8 -*-
# Copyright (C) 2023/11/20, Inc. All Rights Reserved
# @Author  :   Boyu_Zhang(Bob) 
# @Contact :   boyuzhang215@gmail.com

number = input('Enter number: ')

while True:
    try:
        int(number)
        break
    except:
        number = input('Not an integer, Please enter an integer: ')

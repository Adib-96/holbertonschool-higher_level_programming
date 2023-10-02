#!/usr/bin/python3
import calculator_1 as c
a = 10
b = 5
arr = [c.add, c.sub, c.mul, c.div]
sym = ['+','-','*','/']
for i in range(4):
    print(f'{a} {sym[i]} {b} = {arr[i](a, b)}')

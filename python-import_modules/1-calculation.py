#!/usr/bin/python3
import calculator_1 as c
a = 10
b = 5
arr = [c.add, c.sub, c.mul, c.div]
for i in range(4):
    print(arr[i](a, b))

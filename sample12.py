#Learning Python

import os
import random

def foo(arr):
    sum_arr = []
    sum_arr.append(0)
    sum = 0

    for i in range(0, len(arr) - 1):
        sum += arr[i]
        sum_arr.append(sum)

    val = sum_arr[len(sum_arr) - 1] + arr[len(arr) - 1]
    num = random.randint(1,val)

    ret_val = 0
    for i in range(0,len(sum_arr)):
        if(num > sum_arr[i]):
            ret_val = i

    return ret_val

arr = [98,0,2]

first = 0
second = 0
third = 0

for i in range(0,100):
    x = foo(arr)
    if(x == 0):
        first += 1
    elif(x == 1):
        second += 1
    elif(x == 2):
        third += 1

print(first)
print(second)
print(third)

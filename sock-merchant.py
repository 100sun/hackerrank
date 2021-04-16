#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar): # 9 / 10 20 20 10 10 30 50 10 20
    print(set(ar)) # set([10, 20, 50, 30])
    print([ar.count(i) for i in set(ar)]) # [4, 3, 1, 1]  
    # //: divide with integral result (discard remainder)
    print([ar.count(i)//2 for i in set(ar)]) # [2, 1, 0, 0]
    return sum([ar.count(i)//2 for i in set(ar)])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


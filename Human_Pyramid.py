'''I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project
if I am found in violation of this policy.'''
from time import perf_counter
import sys
cache = {}
def weightOn(r,c):
    w = 0
    keys = (r,c)
    if keys in cache:
            return cache[keys]
    if r == 0 and c == 0:
        return 0
    else:
        if (r-1 >= 0) and (c-1 <= r-1) and (c-1 >= 0):
           w += (weightOn(r-1,c-1) + 200)/ 2
           cache[keys] = w
        if (r-1 >= 0) and (c <= r-1) and (c >= 0):
            w += (weightOn(r-1,c) + 200) / 2
            cache[keys] = w
        return cache[keys]
def pyramid(nrows):
    for r in range(0,nrows):
        for c in range(0,r+1):
            print("{0:.2f}".format(weightOn(r,c)),end = " ")
        print ("\r")



def main(n):
    start = perf_counter()
    pyramid(n)
    print("total time: ", perf_counter() - start)

if __name__=='__main__':
    main(int(sys.argv[1]))


        
        


#encoding:utf8
import os

def f2333():
    i=0;
    for num in xrange(2,10000000):
        if(0==num%2 or 0==num%3):
            i +=1
            print("%s:%s"%(i,num))
            if 2333==i:
            #if 6==i:
                break
                
def main():
    f2333()
    
if '__main__'==__name__:
    main()
    
# -*- coding: utf-8 -*-
def p0(p1):
    for p2 in range(1, p1+1):
        for p3 in range(1, p1+1):
            print "%d*%d=%d"%(p2,p3,p2*p3)

p0(3)
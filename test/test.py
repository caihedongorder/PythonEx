#!/usr/bin/env python
# coding=utf-8

import random
import time

sum = 0

r = random.randint(10,13)
print(r)

t = time.time()

for i in xrange(4000+r):
    for j in xrange(4000):
        sum = sum + i * j

print(sum)

print(time.time()-t)

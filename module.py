#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/ycx/Python/module")

from fun import sum
from fun import Add
print "1、test module...%d" % (sum(1,2))
print "2、test module...%d" % (Add(5,2))

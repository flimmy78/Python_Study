#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_odd(n):
    return (n % 2 == 1)


newlist = filter(is_odd, range(20))
print(newlist)

import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


newlist = filter(is_sqr, range(1, 101))
print(newlist)

import struct
import binascii
#print float(-0xffl)
#print hex(0xFFc6)
# s='\x00\x00\xff\xc6'
# s='\x00\xff\x7f\x47'
#print struct.unpack('i',s)
print struct.unpack('<hh', bytes(b'\x01\x00\x00\x00'))
s = '\x63\x14\x9d\xc3'
print "%.2f" % struct.unpack('f', s)
s = '\xC3\x9D\x14\x63'
# s=bytes().fromhex('C39D1463')
#print s
print "%.2f" % struct.unpack('!f', s)

#s=struct.pack('BBBB',0x63,0x14,0x9d,0xc3)
s=struct.pack('B',0x63)+struct.pack('B',0x14)+struct.pack('B',0x9d)+struct.pack('B',0xc3)
print repr(s)
print struct.unpack('f',s)

buffer = struct.pack("ihb", 1, 2, 3)
print repr(buffer)

s=struct.pack("f",-314.16)
print str(repr(s))
print struct.unpack('f',s)


s=struct.pack("i",300)
print str(repr(s))
print "0x%02x%02x%02x%02x" % (int(ord(s[0])),int(ord(s[1])),int(ord(s[2])),int(ord(s[3])))

s=struct.pack("!i",300)
print str(repr(s))
print "0x%02x%02x%02x%02x" % (int(ord(s[0])),int(ord(s[1])),int(ord(s[2])),int(ord(s[3])))




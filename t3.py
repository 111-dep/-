"""
作者：唐杰松
日期：2022年11月28日
"""
import re
import sys
import getopt

# opts, args = getopt.getopt(sys.argv[1:], "r:m:", ["read_sequence=", "make_reverse="])
# print(opts)
# print(args)
s = open("gtf", "r")
s1 = s.read()
s2= s.readlines()
print(s2)

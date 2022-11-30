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
# s = " 1 atgtttgttt ttcttgtttt attgccacta gtctctagtc"
# s1 = re.sub(r"\d+ (\w{10})| (\w{10})","\\g<1>\\g<2>",s)
# print(s1)
# with open("test.gtf","r") as gtf:
#     lsg = gtf.readlines()
# for i in lsg:
#
#     for j in  re.split(r"\s",i)[3:5]:
#         print(j , end=" ")
# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv, "jfts:m:o:",
#                                    ["seq_fa=", "gtf=", "output=","json", "fasta", "tsv"])
#     except getopt.GetoptError:
#         print("python parse_gtf.py -s<> -g<> -o<> -j -f -t")
#         sys.exit()
#     json, fasta, tsv = "", "", ""
#     for name, value in opts:
#         if name in ("-s", "--seq_fa"):
#             seq_fa = value
#         elif name in ("-g", "--gtf"):
#             gtf = value
#         elif name in ("-o", "--output"):
#             output = value
#         elif name in ("-j", "--json"):
#             json = value
#         elif name in ("-f", "--fasta"):
#             tsv = value
#         elif name in ("-t", "--tsv"):
#             fasta = value
#     return [seq_fa, gtf, output, json, tsv, fasta]
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# def bed_dict(bed_file):
#     a_dict = {}
#     with open(bed_file, "r") as bed_a:
#         alines = bed_a.readlines()
#         for aline in alines:
#             ls_a = aline.strip().split("\t")
#             chr_a = ls_a[0]
#             start_a = ls_a[1]
#             end_a = ls_a[2]
#             if chr_a in a_dict:
#                 a_dict[chr_a] = [start_a, end_a]
#             elif chr_a not in a_dict:
#                 a_dict[chr_a] = [start_a, end_a]
#     return a_dict
#
#
#
#
# if __name__ == '__main__':
#     print(bed_dict("test.bed"))

def check(func):
    def wrapper(*args,**kwargs):
        if type(args) == type(0) :
            return func(*args,**kwargs)
        else:
            print('Type must be number!')
            return None
    return wrapper

@check
def plus(a,b):
    return a+b


di = {1:2,3:6}
if di.get(4) ==None:
    print("aaa")
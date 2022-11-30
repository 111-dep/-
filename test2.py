"""
作者：唐杰松
日期：2022年11月28日
"""
import json
import re
import sys
import getopt

# def main(a,b):
#     getopt.getopt(sys.argv[1:],'ab')
#     return a + b
opts, args = getopt.getopt(["-s", "fa ", "-g", " gtf", "-o", "st", "-j", "j"], "jfts:g:o:",
                           ["seq_fa=", "gtf=", "output=", "json", "fasta", "tsv"])


# for i in opts:
#     print(i)
def index():
    return 1 + 1


def foo(func):
    return func


def outter(func):
    def wrapper():
        pass

    return wrapper


# 不要加括号，加括号是先运行了inndex了，不要加括号！不加括号代表的是传的是函数


# print(sys.argv)
def ls_pos(bed_file):
    a_dict = {}
    with open(bed_file, "r") as bed_a:
        alines = bed_a.readlines()
        for aline in alines:
            ls_a = re.split(r"\s", aline)
            chr_a = ls_a[0]
            start_a = ls_a[1]
            end_a = ls_a[2]
            if chr_a in a_dict:
                a_dict[chr_a].append([start_a, end_a])
            elif chr_a not in a_dict:
                a_dict[chr_a] = []
                a_dict[chr_a].append([start_a, end_a])
    return a_dict
a_dict = ls_pos("test.bed")
b_dict = ls_pos("test1.bed")

for chr in a_dict.keys():
    ls_b = b_dict[chr]
    for pos in a_dict[chr]:
        for i in ls_b:
            if pos[0] < i[0] <pos[1]:

                ls_b.remove(i)
                continue
            elif pos[0] < i[1] <pos[1]:

                ls_b.remove(i)
                continue
ls_over1 = []
for chr in a_dict.keys():
    ls_b = a_dict[chr]
    for pos in b_dict[chr]:
        for i in ls_b:
            if pos[0] < i[0] <pos[1]:
                ls_over1.append(i)
                ls_b.remove(i)
                continue
            elif pos[0] < i[1] <pos[1]:
                ls_over1.append(i)
                ls_b.remove(i)
                continue
print(ls_over1)
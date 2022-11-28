"""
作者：唐杰松
日期：2022年11月28日
"""
import re
import sys
import getopt
def main(a,b):
    getopt.getopt(sys.argv[1:],'ab')
    return a + b

if __name__ == '__main__':
    print(main(sys.argv[2],sys.argv[4]))
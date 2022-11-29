"""
作者：唐杰松
日期：2022年11月29日
"""
import re
import getopt

import sys


class CalculateOverlap:
    # 把bed文件转变成{chrom1：[[],[],[]]}的字典
    @staticmethod
    def bed_to_dict(bed_file):
        bed_dict = {}
        with open(bed_file, "r") as bed_a:
            lines = bed_a.readlines()
            for line in lines:
                ls_temp = re.split(r"\s", line)
                chrom = ls_temp[0]
                start = ls_temp[1]
                end = ls_temp[2]
                if chrom in bed_dict:
                    bed_dict[chrom].append([start, end])
                elif chrom not in bed_dict:
                    bed_dict[chrom] = []
                    bed_dict[chrom].append([start, end])
        return bed_dict

    @staticmethod
    def cal_overlap(bed_dict1, bed_dict2, bed_file1):
        ls_result = []
        for chr in bed_dict1.keys():
            ls_b = bed_dict2[chr]
            for pos_1 in bed_dict1[chr]:
                for pos_2 in ls_b:
                    if pos_2[0] < pos_1[0] < pos_2[1]:
                        ls_result.append(pos_1)
                        ls_b.remove(pos_2)
                        continue
                    elif pos_2[0] < pos_1[1] < pos_2[1]:
                        ls_result.append(pos_1)
                        ls_b.remove(pos_2)
                        continue
                    elif pos_1[0] < pos_2[0] < pos_1[1]:
                        ls_result.append(pos_1)
                        ls_b.remove(pos_2)
                        continue
                    elif pos_1[0] > pos_2[1]:
                        ls_b.remove(pos_2)
                        continue
                    elif pos_1[1] < pos_2[0]:
                        continue

        with open(bed_file1, "r") as f:
            ls_temp = f.readlines()
        res = []
        # 起始位置和基因id做map
        dict_temp = {}
        for line in ls_temp:
            dict_temp[line[1]] = line[3]
        for i in ls_result:
            res.append(dict_temp[i[0]])

        return res


def main(argv):
    try:
        opts = getopt.getopt(argv, "a:b", ["bed-a=", "bed-b="])
    except:
        print("python calculate_overlap.py -a<> -b<>")
        sys.exit()

    for k, v in opts:
        if k in ("-a", "--bed-a"):
            bed_a = v
        elif k in ("-b", "--bed-b"):
            bed_b = v
    return [bed_a, bed_b]


if __name__ == '__main__':
    data = main(sys.argv[1:])
    bed_a = data[0]
    bed_b = data[1]
    dict_a = CalculateOverlap.bed_to_dict(bed_a)
    dict_b = CalculateOverlap.bed_to_dict(bed_b)

    print(CalculateOverlap.cal_overlap(dict_a, dict_b, bed_a))

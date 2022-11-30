"""
作者：唐杰松
日期：2022年11月28日
"""
import re
import json
import sys
import getopt


class GbToJson(object):
    @staticmethod
    def make_json(read_file, make_file):
        gb_dict = {}

        with open(read_file, "r") as f:
            gb_string = f.read()
        with open(make_file, "w") as push:
            for g in re.split(r"//", gb_string):
                g = re.sub(r" +", " ", g)
                g = re.sub(r"\n", "", g)
                g = re.sub(r"\d+ (\w{10})| (\w{10})", "\\g<1>\\g<2>", g)
                g = re.sub(r"(\w{10..}) ", "\\g<1>", g)
                gb_list = re.split(r"(LOCUS)|(DEFINITION)|(ACCESSION)"
                                   r"|(VERSION)(KEYWORDS)|(SOURCE)|(FEATURES)|(gap)|(ORIGIN)"
                                   , g)
                res = list(filter(None, gb_list))
                for i in range(0, len(res), 2):
                    gb_dict[res[i]] = res[i + 1]
                push.write(json.dumps(gb_dict)+"\n")


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "r:m:", ["read_file=", "make_file="])
    except getopt.GetoptError:
        print("python gb_to_json.py -r<> -m<>")
        sys.exit()
    for name, value in opts:
        if name in ("-r", "--read_file"):
            read_file = value
        elif name in ("-m", "--make_file"):
            make_file = value
    return [read_file, make_file]


if __name__ == '__main__':
    data = main(sys.argv[1:])
    read_file = data[0]
    make_file = data[1]
    GbToJson.make_json(read_file,make_file)


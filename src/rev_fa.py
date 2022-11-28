"""
作者：唐杰松
日期：2022年11月28日
"""
import re
import sys
import getopt


class SequenceError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ReverseSequence:
    @staticmethod
    def rev_fa(rd_fa_file, mk_fa_file):
        seq_dict = {"A": "T", "C": "G", "T": "A", "G": "C", "N": "N"}

        with open(rd_fa_file, "r") as file :
            seq_str = file.read().strip("\n")
        with open(mk_fa_file, "w") as push:
            # fasta的正则格式，检测是否为fasta格式
            fa_compile = re.compile(r">\w+\n\w+")
            try:
                if re.match(fa_compile, seq_str) == None:
                    raise SequenceError("请输入正确的fasta序列")
            except SequenceError as e:
                print("{}".format(e))

            for line in seq_str.split("\n"):
                if line.startswith(">"):
                    push.write(line + "\n")
                else:
                    s = ""
                    for i in line:
                        s += seq_dict.get(i.upper(), "-")
                    push.write(s + "\n")



def main(argv):
    try:
        opts, args = getopt.getopt(argv, "r:m:", ["read_sequence=", "make_reverse="])
    except getopt.GetoptError:
        print("python rev_fa.py -r<> -m<>")
        sys.exit()
    for name, value in opts:
        if name in ("-r", "--read_sequence"):
            read_sequence = value
        elif name in ("-m", "--make_reverse"):
            make_reverse = value
    return [read_sequence, make_reverse]


if __name__ == '__main__':
    data = main(sys.argv[1:])
    read_sequence = data[0]
    make_reverse = data[1]
    ReverseSequence().rev_fa(read_sequence, make_reverse)
    # ReverseSequence().rev_fa("aa", "bb")

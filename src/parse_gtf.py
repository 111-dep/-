"""
作者：唐杰松
日期：2022年11月28日
"""
import re
import json
import sys
import getopt


class ParseGtf:
    @staticmethod
    def mk_fa_line(rd_fa_file):
        fa = open(rd_fa_file, "r")
        temp = ""
        for i in fa.readlines():
            # 把序列文件拼成一行,需要字符串切片
            if i[0] != ">":
                temp += i[:-1]
            # 待完善
            else:
                #
                temp = ""
        seq_fa = temp
        return seq_fa

    # 输出精简后的gtf信息

    @staticmethod
    def mk_sim_gtf(rd_gtf_file):
        file = open(rd_gtf_file, "r")
        list_seq = list(file.readlines())
        ls_simplify = []
        for i in list_seq:
            ls_simplify_temp = []
            ls2 = i.replace(";", " ").split()
            ls_simplify_temp.append(ls2[2])
            ls_simplify_temp.append(ls2[3])
            ls_simplify_temp.append(ls2[4])
            ls_simplify_temp.append(ls2[6])
            ls_simplify_temp.append(ls2[9])
            ls_simplify_temp.append(ls2[13])
            ls_simplify.append(ls_simplify_temp)
        return ls_simplify

    # 截取exon和cds序列,并拼接，字典形式呈现
    @staticmethod
    def cut_seq(seq, ls_sim):
        fa_dict = {}
        for ls in ls_sim:
            if ls[0] == "exon" or ls[0] == "CDS":
                fa_dict[
                    "gene_id:" + re.sub(r"\"", "", ls[4]) + " transcript_id:" + re.sub(r"\"", "", ls[5]) + " " + ls[3] +
                    ls[0]] = fa_dict.get(
                    "gene_id:" + re.sub(r"\"", "", ls[4]) + " transcript_id:" + re.sub(r"\"", "", ls[5]) + " " + ls[3] +
                    ls[0], "") + seq[int(ls[1]):int(
                    ls[2]) + 1]

        for j in fa_dict.keys():
            if "-" in j:
                fa_dict[j] = fa_dict[j][::-1]
        return fa_dict

    @staticmethod
    def parse_gtf_json(fa_dict, mk_file):

        with open(mk_file + ".json", "w") as mk:
            dict_gene = {}
            dict_trans = {}
            dict_type = {}
            ls_trans = []
            dict_gene["gene_id"] = ""
            for item in fa_dict:
                ls_temp = re.split(r":| ", item)
                type = re.sub(r"/+|-", "", ls_temp[4])
                if dict_gene["gene_id"] == ls_temp[1] and dict_trans["transcript_id"] == ls_temp[3]:
                    dict_type[type] = fa_dict[item]
                else:
                    dict_type = {}
                    dict_type[type] = fa_dict[item]
                if dict_gene["gene_id"] == ls_temp[1] and dict_gene["gene_id"] != "":
                    dict_trans["transcript_id"] = ls_temp[3]
                    dict_trans["type"] = dict_type
                    ls_trans.append(dict_trans)
                else:
                    # print(dict_gene)
                    ls_trans = []
                    dict_trans = {}
                    dict_type = {}
                    dict_type[type] = fa_dict[item]
                    dict_trans["transcript_id"] = ls_temp[3]
                    dict_trans["type"] = dict_type
                    ls_trans.append(dict_trans)
                    dict_gene["gene_id"] = ls_temp[1]
                    dict_gene["transcript"] = ls_trans
                mk.write(json.dumps(dict_gene)+"\n")

    @staticmethod
    def parse_gtf_fasta(fa_dict, mk_file):
        with open(mk_file + ".fasta", "w") as mk:
            for di in fa_dict:
                mk.write(">" + di.replace("\"", "") + "\n")
                mk.write(fa_dict[di] + "\n")

    @staticmethod
    def parse_gtf_tsv(fa_dict, mk_file):
        with open(mk_file + ".tsv", "w") as mk:
            for di in fa_dict:
                mk.write(di.replace("\"", "") + "\t")
                mk.write(fa_dict[di] + "\n")


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "jfts:g:o:", ["seq_fa=", "gtf=", "output=", "json", "fasta", "tsv"])
    except getopt.GetoptError:
        print("python parse_gtf.py -s<> -g<> -o<> -j -f -t")
        sys.exit()
    js, fasta, tsv = "", "", ""
    for name, value in opts:
        if name in ("-s", "--seq_fa"):
            seq_fa = value
        elif name in ("-g", "--gtf"):
            gtf = value
        elif name in ("-o", "--output"):
            output = value
        elif name in ("-j", "--json"):
            js = "j"
        elif name in ("-t", "--tsv"):
            tsv = "t"
        elif name in ("-f", "--fasta"):
            fasta = "f"
    return [seq_fa, gtf, output, js, tsv, fasta]


if __name__ == '__main__':
    data = main(sys.argv[1:])
     # data = ["../resource/Homo_sapiens.GRCh38.dna.chromosome.MT.fa ", "../resource/Homo_sapiens.GRCh38.99.MT.gtf",
     #        "../test", "json", "", ""]
    seq_fa = data[0]
    gtf = data[1]
    output = data[2]

    seq_line = ParseGtf.mk_fa_line(seq_fa)
    gtf_sim = ParseGtf.mk_sim_gtf(gtf)

    fa_dict = ParseGtf.cut_seq(seq_line, gtf_sim)

    for i in range(3, len(data)):
        if data[i] in ("j", "json"):
            ParseGtf.parse_gtf_json(fa_dict, output)
        elif data[i] in ("t", "tsv"):
            ParseGtf.parse_gtf_tsv(fa_dict, output)
        elif data[i] in ("f", "fasta"):
            ParseGtf.parse_gtf_fasta(fa_dict, output)

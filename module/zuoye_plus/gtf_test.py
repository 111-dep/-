"""
作者：唐杰松
日期：2022年11月24日
"""
import re


# 输出单行序列字符串
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
def cut_seq(seq, ls_sim):
    fa_dict = {}
    for ls in ls_sim:
        if ls[0] == "exon" or ls[0] == "CDS":
            fa_dict["gene_id:" + ls[4] + "_transcript_id:" + ls[5] + "_" + ls[3] + ls[0]] = fa_dict.get(
                "gene_id:" + ls[4] + "_transcript_id:" + ls[5] + "_" + ls[3] + ls[0], "") + seq[
                                                                                            int(ls[1]):int(ls[2]) + 1]

    for j in fa_dict.keys():
        if "-" in j:
            fa_dict[j] = fa_dict[j][::-1]
    return fa_dict


push_file_fa = open("../../result/seq.fa", "w")
push_file_tsv = open("../../result/seq.tsv", "w")
push_file_json = open("../../result/seq.json", "w")

seq_fa = mk_fa_line("../../rd_fa_file")
ls_sim = mk_sim_gtf("rd_gtf_file")
dict_fa = cut_seq(seq_fa, ls_sim)
# 生成fasta文件
for di in dict_fa:
    push_file_fa.write(">" + di.replace("\"", "") + "\n")
    push_file_fa.write(dict_fa[di] + "\n")
# 生成tsv文件
for di in dict_fa:
    push_file_tsv.write(di.replace("\"", "") + "\t")
    push_file_tsv.write(dict_fa[di] + "\n")
# 生成json文件
di_all = {}
for di in dict_fa:
    ls_temp = di.split("\"")
    di_gene = {}
    di_trans = {}
    di_seq = {}
    di_gene[ls_temp[1]] = di_trans
    di_trans["transcript_id"] = ls_temp[3]
    di_trans["seq"] = di_seq
    for i in ls_temp:
        if "exon" in ls_temp[4]:
            di_seq["exon"] = dict_fa[di]
        else:
            di_seq["cds"] = dict_fa[di]
    di_all.update(di_gene)
push_file_json.write(str(di_all).replace("'","\""))

push_file_fa.close()
push_file_tsv.close()
push_file_json.close()

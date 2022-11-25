"""
作者：唐杰松
日期：2022年11月23日
"""
import re
#判断是否有gap
def is_gap(seq):
    if re.search(".*gap.*",seq):
        return False
#去掉gap序列，
def drop_gap(seq,gap_string):
    ls = re.findall("\d+..\d+", gap_string)
    ls1 = []
    for i in ls:
        for j in i.split(".."):
            ls1.append(int(j))

    temp = ""
    flag = 0
    for i in ls1:
        if flag ==0:
            temp += seq[0:i+1]
        elif flag != 0 and flag / 2 == 0:
            pass
        elif flag != len(ls1) - 1 and flag / 2 == 1:
            temp += seq[i:ls1[flag+1]]
        elif flag == len(ls1) -1:
            temp += seq[i:len(seq)-1]
        flag += 1
    return temp
#




# 根据gb文件解析出json文件，即{id：{cds:fa,exon:fa}}
def mk_gb_json(rd_file, mk_file):
    # 创建一个空文件
    json = open(mk_file, "w")
    # 读gb文件
    file = open(rd_file, "r")
    str = file.read()
    str = str.replace("\n", "")
    # 把gap部分字符替换
    # strinfo = re.compile(r"gap(.+?)ORIGIN")
    # str = strinfo.sub('ORIGIN', str)
    l1 = re.findall(r"protein_id=(.+?)//", str)
    count = 0
    n = 1
    json.write("{")
    for j in l1:

        if count < len(l1) - 1:
            for i in j.replace(" ", "").replace("/", "").split("ORIGIN"):
                # 根据n值，写入id或序列

                if n == 1 and not is_gap(i):
                    json.write(i.replace("translation=", ":{\"translation\":"))
                elif n == 1 and is_gap(i):
                    str1 = i.replace("translation=", ":{\"translation\":")
                    json.write(re.sub("gap.*", "", str1))

                elif n == 2:
                    string1 = re.sub(r'[0-9]+', '', i)
                    json.write(",\"origin\":" + "\"" + string1 + "\"},")
                n += 1
                if n > 2:
                    n = 1
        # 针对最后一个序列进行额外的写法，不加","
        else:
            for i in j.replace(" ", "").replace("/", "").split("ORIGIN"):
                if n == 1 :

                    json.write(i.replace("translation=", ":{\"translation\":"))
                else:
                    string1 = re.sub(r'[0-9]+', '', i)
                    json.write(",\"origin\":" + "\"" + string1 + "\"}")
                n += 1
                if n > 2:
                    n = 1
        count += 1
    json.write("}")


# 根据gtf文件解析出json,tsv,fasta三种格式
def mk_json_tsv_fa(rd_gtf_file, rd_fa_file, mk_file):
    # 创建一个空文件
    tsv = open(mk_file + ".tsv", "w")
    json = open(mk_file + ".json", "w")
    fasta = open(mk_file + ".fa", "w")

    file = open(rd_gtf_file, "r")
    # 读fa文件
    fa = open(rd_fa_file, "r")

    list_seq = list(file.readlines())
    l1 = []

    for i in list_seq:
        ls = i.split(";")[0].split("\t")
        # 精简gtf信息
        l1.append([ls[2], ls[3], ls[4], ls[8]])
    temp = ""

    for i in fa.readlines():
        # 把序列文件拼成一行,需要字符串切片
        if i[0] != ">":
            temp += i[:-1]
    # 序列文件
    seq = temp
    di = {}
    for i in l1:
        # 截取序列信息

        # 基因id为键，序列为值
        if di.get(i[0] + ":" + i[3]) != None:
            # 取值，然后拼接
            di[i[0] + ":" + i[3]] = di.get(i[0] + ":" + i[3]) + seq[int(i[1]):int(i[2]) + 1]
        else:
            di[i[0] + ":" + i[3]] = seq[int(i[1]):int(i[2]) + 1]

    for i in di:
        if i[0:3] == "CDS" or i[0:3] == "exo":
            tsv.write(str(i) + "\t" + di.get(i) + "\n")
            # json.write("{\""+str(i)+":"+ di.get(i)+"\"}")
            fasta.write(">" + str(i) + "\n" + di.get(i) + "\n")

    json.write("{")
    len(di)
    count = 0
    for i in di:
        if i[0:3] == "CDS" or i[0:3] == "exo" and count < len(di) - 1:
            json.write("\"" + str(i).replace(":gene_id \"", "_") + ":\"" + di.get(i) + "\",")
        # 解决最后一个逗号问题
        elif i[0:3] == "CDS" or i[0:3] == "exo" and count == len(di) - 1:
            json.write("\"" + str(i).replace(":gene_id \"", "_") + ":\"" + di.get(i) + "\"")
        count += 1
    json.write("}")
    tsv.close()
    json.close()
    fasta.close()


# 计算gc含量
def gc_content(rd_fa_file, mk_gc_content_file):
    test = open(mk_gc_content_file, "w")
    # 读fa文件
    file = open(rd_fa_file, "r")
    list_seq = list(file.readlines())

    temp = ""
    num = 0
    sum = len(list_seq)
    gc = 0
    while num <= sum:
        if num == sum:
            for j in temp[::-1]:
                if j != '\n':
                    if j == "G" or j == "C":
                        gc += 1
            if len(temp) != 0:
                test.write(str(format((gc / len(temp)) * 100, ".2f")) + "%")
            break
        if list_seq[num][0] != ">":
            # 写入内容，合并序列
            temp += list_seq[num]
        else:
            # 倒置，写入
            for j in temp[::-1]:
                if j != '\n':
                    if j == "G" or j == "C":
                        gc += 1
            if len(temp) != 0:
                test.write(str(format((gc / len(temp)) * 100, ".2f")) + "%")
            test.write("\n" + list_seq[num][:-1] + "\t") \
                if num > 0 else \
                test.write(list_seq[num][:-1] + "\t")
            temp = ""
        num += 1
        gc = 0
    test.close()


class Demo:
    seq_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}

    # 输出反向互补序列
    def rev_com(self, rd_fa_file, mk_fa_file):
        push = open(mk_fa_file, "w")
        file = open(rd_fa_file, "r")
        list_temp = file.readlines()
        temp = ""
        n = 0
        for i in list_temp:
            if i[0] != ">":
                temp += i
            else:
                for j in temp[::-1]:
                    if j != "\n":
                        push.write(self.seq_dict[j])
                push.write("\n" + i)
                temp = ""
            n += 1
            if n == len(list_temp) - 1 and i[0] != ">":
                for k in temp[::-1]:
                    if k != "\n":
                        push.write(self.seq_dict[k])

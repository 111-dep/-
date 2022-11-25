"""
作者：唐杰松
日期：2022年11月25日
"""
push = open("../../result/mk_fa_file", "w")
file = open("my_sequences.fa", "r")
s = "ATCGN-"
b = "TAGCN-"
trans_tab = str.maketrans(s, b)
list_seq = file.readlines()
temp = ""
for i in range(0,len(list_seq)):
    if list_seq[i].startswith(">"):
        push.write(temp.translate(trans_tab))
        push.write(list_seq[i])
        temp = ""
    elif i == len(list_seq) - 1:
        push.write(temp.translate(trans_tab))
    else:
        temp += list_seq[i]


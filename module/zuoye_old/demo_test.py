"""
作者：唐杰松
日期：2022年11月23日
"""
from module.zuoye_old import demo

# demo.gc_content("../resource/GC-content.tsv", "../result/gc.tsv")
demo.mk_gb_json("../../resource/SARS-CoV-2_S.gb", "../result/gb.json")
# demo.mk_json_tsv_fa("../resource/Homo_sapiens.GRCh38.99.MT.gtf", "../resource/Homo_sapiens.GRCh38.dna.chromosome.MT.fa", "../result/analysis")
#
# test = demo.Demo()
# test.rev_com("../resource/my_sequences.fa","../result/rev")




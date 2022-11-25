"""
作者：唐杰松
日期：2022年11月23日
"""

import re

dict_all = {}
di_element = {}
di_gene = {}
di_cds = {}
di_gap = {}
di_gaps = {}

file_gb = open("SARS-CoV-2_S.gb", "r")
file_json = open("../../result/json_test.json", "w")
s1 = file_gb.read()
ls_gb = s1.split("//")
for i in ls_gb[:1]:
    ls_temp_one = i.split()
    # 给各个元素赋值
    di_element["TIME"] = ls_temp_one[6]

    di_element["LENGTH"] = ls_temp_one[2]

    definition_temp = i.split("DEFINITION")[1].split("ACCESSION")[0].replace("\n", "")
    definition = re.sub('  +', '', definition_temp)
    di_element["DEFINITION"] = definition

    accession = i.split("ACCESSION")[1].split("VERSION")[0].replace(" ", "")
    di_element["ACCESSION"] = accession

    version = i.split("VERSION")[1].split("KEYWORDS")[0].replace(" ", "")
    di_element["VERSION"] = version

    features = i.split("FEATURES")[1].split("gene")[0].replace(" ", "")
    di_element["FEATURES"] = features



    START_STOP = i.split("FEATURES")[1].split("gene")[1].split()[0]
    di_gene["START_STOP"] = START_STOP

    TYPE = i.split("FEATURES")[1].split("gene")[2].split()[0].replace("\"", "").replace("=", "")
    di_gene["TYPE"] = TYPE

    START_STOP = i.split("FEATURES")[1].split("CDS")[1].split()[0]
    di_cds["START_STOP"] = START_STOP

    TYPE = i.split("FEATURES")[1].split("CDS")[1].split()[1].replace("/gene=\"", "").replace("\"", "")
    di_cds["TYPE"] = TYPE

    codon_start = i.split("codon_start=")[1].split()[0]
    di_cds["codon_start"] = codon_start

    product = i.split("product=")[1].split()[0].replace("\"","")
    di_cds["product"] = product

    protein_id = i.split("protein_id=")[1].split()[0].replace("\"","")
    di_cds["protein_id"] = protein_id

    translation_temp = i.split("translation=")[1].replace("\n","")
    translation= re.sub(r" +","",translation_temp).replace("\"","")
    di_cds["translation"] = translation

    gap_temp = i.split("FEATURES")[1].split("ORIGIN")[0].split("gap")[1:]
    gap_num = 1
    for gap_i in gap_temp:
        START_STOP = gap_i.split()[0]
        di_gaps["name"] = gap_num
        gap_num += 1
        di_gaps["START_STOP"] = START_STOP
        di_gap.update(di_gaps)

    origin_temp = i.split("ORIGIN")[1].replace(" ", "")
    origin = re.sub(r"[0-9]+", "", origin_temp).replace("\n", "")
    di_element["ORIGIN"] = origin

    di_element["gap"] = di_gap
    di_element["gene"] = di_gene
    di_element["cds"] = di_cds
    dict_all[ls_temp_one[1]] = di_element

file_json.write(str(dict_all).replace("'", "\""))

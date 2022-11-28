import re
import json
gb_dict = {}
with open("gb", "r") as f:
    gb_string = f.read()
    gb_string = re.sub(r" +", " ", gb_string)
    gb_string = re.sub(r"\n", " ", gb_string)
    gb_string = re.sub(r"\d{,6} [atcg]{6} |[atcg]{6} ", " ", gb_string)
    gb_list = re.split(r"(LOCUS)|(DEFINITION)|(ACCESSION)"
                       r"|(VERSION)(KEYWORDS)|(SOURCE)|(FEATURES)|(ORIGIN)"
                       , gb_string)
    res = list(filter(None, gb_list))
    for i in range(0,len(res),2):

        if res[i] == "FEATURES":
            gb_fe_dict = {}
            gb_fe_list = re.split(r"(gene)|(CDS)",res[i+1])
            for fi in range(0,len(gb_fe_list),2):
                gb_fe_dict[gb_fe_list[fi]] = gb_fe_list[fi + 1]
            gb_dict["FEATURES"] = gb_fe_dict = {}

        elif i+1 == len(res) -1:
            res[i+1] = re.sub(r"\d| ","" ,res[i+1])
        else:
            gb_dict[res[i]] = res[i + 1]
    gb_json = json.dumps(gb_dict)

    print(gb_json)

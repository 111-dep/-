import re
import json

gb_dict = {}
with open("resource/SARS-CoV-2_S.gb", "r") as f:
    gb_string = f.read()
for g in re.split(r"//",gb_string):
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

    gb_json = json.dumps(gb_dict)

    print(gb_json)

"""
作者：唐杰松
日期：2022年11月28日
"""
import re


class GbJson(object):

    def __init__(self, gb_file_path, json_file_path):
        self.gb_file_path = gb_file_path
        self.json_file_path = json_file_path

    def make_json(self, *args):
        with open("../resource/SARS-CoV-2_S.gb","r") as f:
            gb_string = f.read()
            gb_list = re.split(r"",gb_string)

        pass


def main():
    pass


if __name__ == '__main__':
    main()

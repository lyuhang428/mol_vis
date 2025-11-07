#!/usr/bin/python3
import argparse
from PyPDF2 import PdfReader
import os

def main()->None:
    '''
    CLI tool, extract refs from given paper
    Data washing relies on .get_refs.sh, don't delete it!
    '''

    parser = argparse.ArgumentParser(description="extract refs from paper")
    parser.add_argument('-f', "--file", type=str, required=True, help="paper name")
    parser.add_argument('-n', "--npage", type=int, required=True, help="number of pages of ref")
    parser.add_argument('-o', "--output", type=str, required=True, help="output dest")

    args = parser.parse_args()
    input = args.file
    npage = args.npage
    output = args.output

    reader = PdfReader(input)
    pages = reader.pages[-npage:]

    with open(output, 'w') as file:
        for page in pages:
            file.writelines(page.extract_text())

    os.system(f"./get_refs.sh {output}")

if __name__ == "__main__":
    main()

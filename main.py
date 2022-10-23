from pydoc import Helper
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import numpy as np
from os.path import exists


def salvePDF(path: str, output_file: PdfFileWriter) -> None:
    # Remove o pdf do fim da string e adiciona um _out
    path = path[:-4] + "_Out.pdf"

    with open(path, 'wb') as f:
        output_file.write(f)


def extract_range_of_pages(pages_range: str, pdf_name: str) -> PdfFileWriter:

    extract_page = []
    output_file = PdfFileWriter()
    pages_to_include = set(map(int, pages_range.split(',')))
    file = PdfFileReader(pdf_name, 'rb')

    print(pages_to_include)

    for page in range(file.getNumPages()):

        if (page+1) in pages_range:
            extract_page = file.getPage(page)
            output_file.addPage(extract_page)


def delete_pages(pdf_name: str, pages: str) -> PdfFileWriter:

    pages_to_delete = list(map(int, pages.split(',')))
    file = PdfFileReader(pdf_name, 'rb')
    output_file = PdfFileWriter()

    for i in range(file.getNumPages()):
        if (i+1) not in pages_to_delete:
            p = file.getPage(i)
            output_file.addPage(p)
   ## print("Output File: \n"+ output_file)

    return output_file


def helper():
    print('Usage:main.py [command] <path>')
    print('-d --delete-pages <page>                      Delete pages.')
    print(
        '-e --extract-range-of-pages [<page>,<page>]   Extract page by a range.')

    print('Options:\n')
    print('-h --help     Show this screen.')
    print('--version     Show version.')


def validation_file() -> bool:
    return True


if __name__ == '__main__':

    argv_len = len(sys.argv)

    if argv_len == 1:
        print("[ERROR]: Not enough arguments")
        sys.exit(1)

    command = sys.argv[1]

    if command == '--help' or command == '--h':
        helper()

    if exists(sys.argv[-1]):

        output_file = PdfFileWriter()

        if command == '--delete-pages' or command == '--d':

            if argv_len != 4:
                print("[ERROR]: Not enough arguments")
                sys.exit(1)

            output_file.appendPagesFromReader(delete_pages(sys.argv[-1], sys.argv[2]))

        if command == '--extract-range-of-pages' or command == '--e':
            print('extract-range-of-pages')
            if argv_len != 4:
                print("[ERROR]: Not enough arguments")
                sys.exit(1)
                
            output_file.appendPagesFromReader(extract_range_of_pages(sys.argv[-1], sys.argv[2]))

        salvePDF(sys.argv[-1],output_file)

    else:
        print(f"\n[ERROR]: The file {sys.argv[-1]} does not exist\n")

from pydoc import Helper
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import numpy as np
from os.path import exists

def extract_range_of_pages(pages_range : str, pdf_name : str) -> None: 
    
    extract_page = []
    outputFile = PdfFileWriter()
    pages_to_include = set(map(int, pages_range.split(',')))
    file = PdfFileReader(pdf_name,'rb')

    print(pages_to_include)

    for page in range(file.getNumPages()):

        if (page+1) in pages_range:
            extract_page = file.getPage(page)
            outputFile.addPage(extract_page)
        
    with open('out.pdf', 'wb') as f:
        outputFile.write(f)

def delete_pages(pdf_name : str, pages : str) -> None:

    pages_to_delete = list(map(int, pages.split(',')))
    infile = PdfFileReader(pdf_name, 'rb')
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if (i+1) not in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)


    with open('newfile.pdf', 'wb') as f:
        output.write(f)




def helper():
    print('Usage:main.py [command] <path>')
    print('-d --delete-pages <page>                      Delete pages.')
    print('-e --extract-range-of-pages [<page>,<page>]   Extract page by a range.')

    print('Options:\n')
    print('-h --help     Show this screen.')
    print('--version     Show version.')
    
  
  

if __name__ == '__main__':

    argv_len = len(sys.argv)


    if argv_len == 1:
        print("[ERROR]: Not enough arguments")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == '--help' or command == '--h':
        helper()

    if exists(sys.argv[-1]):

        if command == '--delete-pages' or command == '--d':

            if argv_len != 4:
                print("[ERROR]: Not enough arguments")
                sys.exit(1)

            delete_pages(sys.argv[-1], sys.argv[2])

        if command == '--extract-range-of-pages' or command == '--e':
            print('extract-range-of-pages')
            if argv_len != 4:
                print("[ERROR]: Not enough arguments")
                sys.exit(1)

            extract_range_of_pages(sys.argv[-1],sys.argv[2])
    else:
        print(f"\n[ERROR]: The file {sys.argv[-1]} does not exist\n")
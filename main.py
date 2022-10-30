from PyPDF2 import PdfFileWriter, PdfFileReader
import sys, os

def savePdf(path: str, output_file: PdfFileWriter) -> None:
    # Get the pdf's name and sum up with _out.pdf
    path = path.split('.pdf')[0] + "_out.pdf"

    with open(path, 'wb') as f:
        output_file.write(f)


def extractRangeOfPages(pages_range: str, pdf_name: str) -> PdfFileWriter:
    
    output_file = PdfFileWriter()
    pages_to_include = map(int, pages_range.split(','))
    excluding_duplicated_pages = set(pages_to_include)
    pages = excluding_duplicated_pages
    file = PdfFileReader(pdf_name, 'rb')

    print(pages)

    for page in range(file.getNumPages()):

        if (page + 1) in pages:
            extract_page = file.getPage(page)
            output_file.addPage(extract_page)

    return output_file


def deletePages(pdf_name: str, pages: str) -> PdfFileWriter:

    pages_to_delete = list(map(int, pages.split(',')))
    file = PdfFileReader(pdf_name, 'rb')
    output_file = PdfFileWriter()

    for i in range(file.getNumPages()):
        if (i+1) not in pages_to_delete:
            p = file.getPage(i)
            output_file.addPage(p)

    return output_file


def helper():
    print('Usage: main.py [command] <path>')
    print('-d --delete-pages <page>                      Delete pages.')
    print('-e --extract-range-of-pages [<page>,<page>]   Extract page by a range.')

    print('Options:\n')
    print('-h --help     Show this screen.')
    print('--version     Show version.')


def main():    
    if len(sys.argv) <= 1 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
        helper()
    
    elif os.path.exists(sys.argv[-1]):
        output_file = PdfFileWriter()
        argv_len = len(sys.argv)

        command = sys.argv[1]
        if argv_len != 4:
            print("[ERROR]: Not enough arguments")
        
        else:
            if command == '--delete-pages' or command == '-d':
                output_file.appendPagesFromReader(
                    deletePages(sys.argv[-1], sys.argv[2]))

            elif command == '--extract-range-of-pages' or command == '-e':
                output_file.appendPagesFromReader(
                    extractRangeOfPages(sys.argv[2], sys.argv[-1]))

            savePdf(sys.argv[-1], output_file)

    else:
        print(f"\n[ERROR]: The file {sys.argv[-1]} does not exist\n")
    

if __name__ == '__main__':
    main()
import PyPDF4
from PyPDF4 import PdfFileReader
import argparse


def printMeta(fileName):
    try:
        pdfFile = PdfFileReader(open(fileName, 'rb'))
        docInfo = pdfFile.getDocumentInfo()
        print('Metadata of PDF file: '+ str(fileName))
        for metaItem in docInfo:
            print(metaItem + ' : ' + docInfo[metaItem])   
    except FileNotFoundError:
        print('Enter a valid PDF file name')


def main():
    parser = argparse.ArgumentParser(description = '--file filename')
    parser.add_argument('--file', action='store', dest='file', required = True, help='Enter a PDF file name')
    args = parser.parse_args()
    fileName = args.file
    if fileName == None:
        print('Enter a valid PDF file')
        exit(0)
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()

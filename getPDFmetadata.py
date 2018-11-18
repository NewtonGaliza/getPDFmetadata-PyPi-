import PyPDF2
from PyPDF2 import PdfFileReader
import optparse

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
    parser = optparse.OptionParser('usage %prog' + '-F <PDF File>')
    parser.add_option('-F', dest='fileName', type='string', help='Enter PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()

import PyPDF2

def scrapperPDF(filename):
    """
    doc_string
    """

    pac_data = {}

    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = ''
    for i in range( pdfReader.numPages ):
        print(i)
        pageObj = pdfReader.getPage(i) 
        text += pageObj.extractText() + '\n'
    pdfFileObj.close()

    filename = filename.split('/') [-1]
    filename = 'lab_' + filename.replace('.pdf','').replace('.','')
    pac_data[filename] = text
    
    return pac_data
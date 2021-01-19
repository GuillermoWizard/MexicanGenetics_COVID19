import os
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def replace_text(content, replacements = dict()):
    lines = content.splitlines()
    result = ""
    in_text = False
    for line in lines:
        if line == "BT": in_text = True
        elif line == "ET": in_text = False
        elif in_text:
            cmd = line[-2:]
            if cmd.lower() == 'tj':
                replaced_line = line
                for k, v in replacements.items():
                    #improve this line for case
                    replaced_line = replaced_line.replace(k, v)
                result += replaced_line + "\n"
            else: result += line + "\n"
            continue
        result += line + "\n"
    return result

def process_data(object, replacements):
    data = object.getData()
    decoded_data = data.decode('utf-8')
    replaced_data = replace_text(decoded_data, replacements)
    encoded_data = replaced_data.encode('utf-8')
    if object.decodedSelf is not None:
        object.decodedSelf.setData(encoded_data)
    else: object.setData(encoded_data)

def replace_strings_in_pdf(in_file, out_file='', replacements = dict()):
    in_file = args["input"]
    filename_base = in_file.replace(os.path.splitext(in_file)[1], "")

    pdf = PdfFileReader(in_file)
    writer = PdfFileWriter()
    for page_number in range(0, pdf.getNumPages()):
        page = pdf.getPage(page_number)
        contents = page.getContents()
        if len(contents) > 0:
            for obj in contents:
                streamObj = obj.getObject()
                process_data(streamObj, replacements)
        else: process_data(contents, replacements)
        writer.addPage(page)
    if out_file=='': out_file.replace('.pdf','_replace.pdf')
    with open(out_file, 'wb') as f: writer.write(f)
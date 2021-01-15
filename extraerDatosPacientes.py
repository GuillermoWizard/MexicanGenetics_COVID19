'''
DESCRIPTION
      Extrae y anonimiza la información de las notas de pacientes del H Nutrición
USAGE
       python extraerDatosPacientes.py -p dir -o output.csv
ARGUMENTS
::-p: str, ruta hacia carpeta con datos de pacientes
::--path: str, ruta hacia archivo input .html
::-o: str, nombre de archivo output
::--output: str, nombre de archivo output
'''

import glob
import argparse
from os import walk

import PyPDF2
from bs4 import BeautifulSoup

from scrapperHTML import scrapperHTML
from scrapperPDF import scrapperPDF
from anonimizar import anonimizar

# Parseador de argumentos
parser = argparse.ArgumentParser(description = "Extrae informacion de pacientes")

# Argumento con ruta al archivo de entrada
parser.add_argument(
    "-p", "--path",
    metavar = "ruta/al/archivo.html/de/entrada",
    help = "Ruta al archivo input.html",
    required = True)

# Argumento con ruta al archivo de salida
parser.add_argument(
    "-o", "--output",
    metavar = "ruta/al/archivo.csv/de/salida",
    help = "Ruta al archivo output.csv",
    required = True
    )

args = parser.parse_args()




# navegar el arbol de archivos
_, pacientes, _ = next(walk(args.path))

for pac in pacientes[0:3]:
    pac_path = args.path + '/'+pac
    pac_files = glob.glob(pac_path+'/**', recursive=True)
    pac_files_html = [f for f in pac_files if f[-5:]=='.html']

    for f in pac_files_html:
        try: # si es html valido extraer información de html con tags
            with open(rf"{f}", encoding = "utf-8") as fp:
                soup = BeautifulSoup(fp, "lxml")
            print(f)
            pac_exp, pac_data = scrapperHTML(f)
        except UnicodeDecodeError:
            # si no es html pero es pdf determinar que tipo de laboratorio es y obtener tabla
            f = f.split('/')[-1].replace('.html','.pdf')
            f = pac_path+'/'+f
            with open(f,'rb') as pdfFileObj:
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            print(f)
            pac_exp, pac_data = scrapperPDF(f)
        # anonimizar
        # análisis de texto buscar terminos covid y etc con covidminer
        
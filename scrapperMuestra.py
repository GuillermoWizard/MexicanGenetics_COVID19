'''NAME
       scrapperMuestra.py
VERSION
        0.2
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa preliminar que extrae informacion de html
CATEGORY
        Parseador
USAGE
       python scrapperMuestra.py -p Ruta/hacia/archivo.html -o Nombre/de/archivo.csv
ARGUMENTS
::-p: str, ruta hacia archivo input .html
::--path: str, ruta hacia archivo input .html
::-o: str, nombre de archivo output
::--output: str, nombre de archivo output
'''

from bs4 import BeautifulSoup

import argparse

import csv

# Parseador de argumentos

parser = argparse.ArgumentParser(description = "Extrae informacion de html")

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

# Abre el archivo html

with open(rf"{args.path}", encoding = "utf8") as fp:

    soup = BeautifulSoup(fp, "lxml")



if soup.find(class_ = "js flexbox canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage webworkers no-applicationcache svg inlinesvg smil svgclippaths") not in soup: 

    nombre = ""

    # Parsea nombre, edad, nacimiento, etc. y extrae la informacion correspondiente

    edad = soup.find(class_="##patientIdentificationComponent.ageHN_2675324665956201694 l_form")

    edad = str(edad.next_element)

    nacimiento = soup.find(class_ = "##patientIdentificationComponent.birthHN_1735630509657194021 z-label")

    nacimiento = str(nacimiento.next_element)

    expediente = soup.find(class_ = "##patientIdentificationComponent.nhcHN_950462502649809883 l_form")

    expediente = str(expediente.next_element)

    temporal = soup.find(class_ = "##patientIdentificationComponent.nipHN_1430107845032919595 l_form")

    temporal = str(temporal.next_element)

    sexo = soup.find(class_ = "##patientIdentificationComponent.sexHN_4609232495718251572 l_form")

    sexo = str(sexo.next_element)

    #notas = soup.find(class_ = "##6946985085284717763 reportDataRequired z-textbox z-textbox-disd z-textbox-text-disd")
    
    htmlnotas = ["" for i in range(5)]

    for i in range(5):

        htmlnotas[i] = "Sin notas"

    
    #notas = s
    # Lista de datos a escribir en el archivo .csv
    #listaDeDatos = [["NOMBRE\tSEXO\tEDAD\tNACIMIENTO\tEXPEDIENTE\tTEMPORAL\tNOTAS"],
    #[nombre, sexo, edad, nacimiento, expediente, temporal, notas]]


    listaDeDatos = [["NOMBRE\tSEXO\tEDAD\tNACIMIENTO\tEXPEDIENTE\tTEMPORAL\tNOTAS1\tNOTAS2\tNOTAS3\tNOTAS4\tNOTAS5"],[nombre + "\t" + sexo + "\t" + edad + "\t" + nacimiento + "\t" + expediente + "\t" + temporal  + "\t" + htmlnotas[0]  + "\t" + htmlnotas[1]  + "\t" + htmlnotas[2] + "\t" + htmlnotas[3]  + "\t" + htmlnotas[4]]]


    #Escribiendo en archivo .csvl

    with open(f"{args.output}", "w+") as nuevoArchivo :
    
        escritor = csv.writer(nuevoArchivo)

        escritor.writerows(listaDeDatos)

    nuevoArchivo.close()

    fp.close()



else:

    # Parsea nombre, edad, nacimiento, etc. y extrae la informacion correspondiente

    nombre = soup.find(class_="##patientIdentificationComponent.sNameHN l_form_big namePatient")

    nombre = str(nombre.next_element)

    edad = soup.find(class_="##patientIdentificationComponent.ageHN_2675324665956201694")

    edad = str(edad.next_element)

    nacimiento = soup.find(class_ = "##patientIdentificationComponent.birthHN_3364940428062238283")

    nacimiento = str(nacimiento.next_element)

    expediente = soup.find(class_ = "##patientIdentificationComponent.nhcHN_950462502649809883")

    expediente = str(expediente.next_element)

    temporal = soup.find(class_ = "##patientIdentificationComponent.nipHN_1430107845032919595")

    temporal = str(temporal.next_element)

    sexo = soup.find(class_ = "##patientIdentificationComponent.sexHN_4609232495718251572")

    sexo = str(sexo.next_element)

    #notas = soup.find(class_ = "##6946985085284717763 reportDataRequired z-textbox z-textbox-disd z-textbox-text-disd")

    s = ""
    htmlnotas = ["" for i in range(5)]
    i = 0

    for tag in soup.find_all(class_="##6946985085284717763 reportDataRequired z-textbox z-textbox-disd z-textbox-text-disd"):
        #print (tag.text)
        s += tag.text
        t = tag.text
        s = s.replace('\n', ' ').replace('\r', '')
        t = t.replace('\n', ' ').replace('\r', '')
        htmlnotas[i] = t
        i += 1

    
    #notas = s
    # Lista de datos a escribir en el archivo .csv
    #listaDeDatos = [["NOMBRE\tSEXO\tEDAD\tNACIMIENTO\tEXPEDIENTE\tTEMPORAL\tNOTAS"],
    #[nombre, sexo, edad, nacimiento, expediente, temporal, notas]]


    listaDeDatos = [["NOMBRE\tSEXO\tEDAD\tNACIMIENTO\tEXPEDIENTE\tTEMPORAL\tNOTAS1\tNOTAS2\tNOTAS3\tNOTAS4\tNOTAS5"],[nombre + "\t" + sexo + "\t" + edad + "\t" + nacimiento + "\t" + expediente + "\t" + temporal  + "\t" + htmlnotas[0]  + "\t" + htmlnotas[1]  + "\t" + htmlnotas[2] + "\t" + htmlnotas[3]  + "\t" + htmlnotas[4]]]


    #Escribiendo en archivo .csvl

    with open(f"{args.output}", "w+") as nuevoArchivo :
    
        escritor = csv.writer(nuevoArchivo)

        escritor.writerows(listaDeDatos)

    nuevoArchivo.close()

    fp.close()

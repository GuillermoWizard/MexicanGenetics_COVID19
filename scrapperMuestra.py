'''NAME
       scrapperMuestra.py
VERSION
        0.4
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

from c19mining.covid import MedNotesMiner 

import simplejson as json

import re

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


    listaDeDatos = [["NOMBRE\tSEXO\tEDAD\tNACIMIENTO\tEXPEDIENTE\tTEMPORAL\tDIAGNOSTICO\tCOVID\tSINTOMAS\tCOMORBS\tMUESTREO\tMEDICAMENTOS\tFECH.DEFUNCION\t"],[nombre + "\t" + sexo + "\t" + edad + "\t" + nacimiento + "\t" + expediente + "\t" + temporal + "\t" + "Sin datos" + "Sin datos" + "Sin datos" + "Sin datos" + "Sin datos" + "Sin datos" + "Sin datos"]]


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

    diagnosticoPrincipal = soup.find(class_ = "##1683876444801718701 reportDataRequired z-textbox z-textbox-real-readonly z-textbox-readonly")

    diagnosticoPrincipal = diagnosticoPrincipal.next_element

    fechaDefuncion = soup.find(class_= "bold ##patientIdentificationComponent.deathDateHN_3728526458450632832 z-label")

    fechaDefuncion = str(fechaDefuncion.next_element)

    #notas = soup.find(class_ = "##6946985085284717763 reportDataRequired z-textbox z-textbox-disd z-textbox-text-disd")

    notas = str(soup.find_all(class_ = "##6946985085284717763 reportDataRequired z-textbox z-textbox-disd z-textbox-text-disd"))

    covidSeeker = MedNotesMiner(notas)

    covidSeeker.check_covid19()

    covidSeeker.check_symptoms()

    covidSeeker.check_comorbidities()

    covidSeeker.check_sampling()

    covidSeeker.check_drugs()

    covidInsights = json.dumps(covidSeeker.clues, encoding = "utf8")

    covid =  re.findall(r'"COVID-19": {.*}, "sintomas"', str(covidInsights))

    sintomas =  re.findall(r'"sintomas": {.*}, "comorbilidades"', str(covidInsights))

    comorbilidades = re.findall(r'"comorbilidades": {.*}', str(covidInsights))

    muestreo = re.findall(r'"muestreo": {.*}, "medicamentos"', str(covidInsights))

    medicamentos = re.findall(r'"medicamentos": {.*}', str(covidInsights))



    listaDeDatos = [["NOMBRE\tSEXO\tEDAD\tNACIMIENTO\tEXPEDIENTE\tTEMPORAL\tDIAGNOSTICO\tCOVID\tSINTOMAS\tCOMORBS\tMUESTREO\tMEDICAMENTOS\tFECH.DEFUNCION\t"],[str(nombre) + "\t" + str(sexo) + "\t" + str(edad) + "\t" + str(nacimiento) + "\t" + str(expediente) + "\t" + str(temporal)  + "\t" + str(diagnosticoPrincipal) + "\t" + str(covid) + "\t" + str(sintomas) + "\t" + str(comorbilidades) + "\t" + str(muestreo) + "\t" + str(medicamentos) + "\t" + str(fechaDefuncion) ]]


    #Escribiendo en archivo .csvl

    with open(f"{args.output}", "w+", encoding = "utf8") as nuevoArchivo :
    
        escritor = csv.writer(nuevoArchivo)

        escritor.writerows(listaDeDatos)

    nuevoArchivo.close()

    fp.close()

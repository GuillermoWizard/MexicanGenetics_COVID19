# MexicanGenetics_COVID19

## Pipeline para el análisis de los datos de pacientes covid19

[/] Navegar expedientes (helpers.py)  
[AC] Obtener datos de todos los pacientes (extraerDatosPacientes.py y scrapperHTML.py > datos_pacientes.pk)  
[/] Remover nombres, tratante y fechas de nacimiento de todos los labs pdf (replaceStringsPDF.py)  
[AA] Extraer tablas de pdf (scrapperPDF.py)  
[ME] Anonimizado agresivo sobre notas de html (anonimizado.py)  
[AC] Covidminer sobre notas de html  



## Requerimientos e instalación

Descargar repositorio
```
git clone https://github.com/GuillermoWizard/MexicanGenetics_COVID19.git
```

Anaconda
```
conda create --name MexicanGenetics_COVID19

conda activate MexicanGenetics_COVID19
conda install --file requirements.txt
```

c19mining

Estructura requerida para funcionamiento de c19mining  

├───covidminer-master  
│   ├───scrapperMuestra.py  
│   ├───.github  
│   │         └───workflows  
│   ├───c19mining  
│   │         └───__pycache__  
│   ├───data  
│   │         ├───excels  
│   │         └───test  
│   ├───docs  
│   │         └───imgs  
│   ├───notasPrueba  
│   └───resources  

```
Notas de chat

Alejandro Molina: 
entras por el enlace o directo a github https://github.com/alemol/covidminer
de ahí te agregas en los contributors
clona el repositorio
conviene que en directorio del repo crees un entorno virtual de Python 3.7
también tienes que instalar tesserac y poppler
hay unos comandos en la página de inicio y enlaces para la pag oficial. 
es que para el OCR sí necesitarás esos dos.

Yalbi:
mm intenté hacerlo vía anaconda porque ahí tenía una versión python 37
hice primero lo de 
pip install -r docs/requirements.txt
cuando intenté
brew install tesseract
me mando error e instalé entonces
brew install tesseract-lang
luego no sé si esto tiene español así que intenté el de
brew install tesseract-esp
me dijo esto
tesseract 4.1.1 is already installed and up-to-date
To reinstall 4.1.1, run `brew reinstall tesseract`

Alejandro Molina:
va, es que creo que en orden sería primero lo de brew y luego lo de requirements
intenta lo de conda de nuevo
si todo está OK deberías poder ejecutar un script de demo:
(venv) amolina@Mac:~/repo/covidminer$python demo.py 
te imprime un JSON y una lista de síntomas
haz un directorio "notas" al mismo nivel que el script demo.py
para poner las notas (PDF) y que no estén tan anidadas
pon unas cuantas, para probar y luego ya puedes hacerlo para todas
haces un nuevo script yalbi.py 
y en tres lineas! ahí va:
from c19mining.ocr import TesseOCR
my_ocr = TesseOCR('spa')
texto_nota = my_ocr.get_text_from_pdf('notas/notamed.pdf')
tu variable texto_nota será de tipo str y podrás hacer lo que necesites: escribir un archivo .txt , un csv  un excel...
haz la versión de escribir a un txt y cuando lo tengas para una nota ya lo puedes probar para todo un directorio
tengo una función que explora directorios y te va dando los paths
from c19mining.utils import explore_dir
for (Note_path, MedNote_bname) in explore_dir(jsons_inputdir, yield_extension='pdf'):
    texto_nota = my_ocr.get_text_from_pdf(Note_path)
en 3 líneas!
si te interesa mejorar la biblioteca para que haga algo en especial, adelante bienvenida para sugerir y programar nueva funcionalidad

```




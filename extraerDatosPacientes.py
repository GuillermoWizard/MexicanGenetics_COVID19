import warnings
import pickle

from helpers import *
from scrapperHTML import scrapperHTML

dir_in = 'CovidPacientes'
f_out  = 'data/datos_pacientes.pkl'

pac_files = navegar_expedientes(dir_in, f_format='.html')

datos_pacientes = {}
for ids,files in pac_files.items(): 
    data = {}
    
    for f in files:
        try: 
            d = scrapperHTML(f)
            if len(d['nombre']) >= 50:
                warnings.warn("\n\tWARN: error de procesamiento de archivo, ignorando datos de: " + f)
                d = dict()
        except UnicodeDecodeError: 
            d = dict()
        data.update( d )
        
    datos_pacientes[ids] = data

for pac, data in datos_pacientes.items():
    print(pac, {k:v[0:25] for k,v in data.items()}

with open(f_out, 'wb') as f:
    pickle.dump(datos_pacientes, f)
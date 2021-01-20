import re
from os import path, makedirs
from pickle import load

from helpers import *
import pdf_redactor

dir_in = 'CovidPacientes'
dir_out = 'CovidPacientesLabsAnon'
file_in = 'data/datos_pacientes.pkl'

with open(file_in, 'rb') as f:
    datos_pacientes = load(f)
    
pac_files = navegar_expedientes(dir_in, f_format='.pdf', f_type='lab')

if not path.exists(dir_out):
    makedirs(dir_out)

for pac, pac_data in datos_pacientes.items():
    if len(pac_files[pac]) >=5:
        if not path.exists(dir_out+'/'+pac):
            makedirs(dir_out+'/'+pac)
        for in_file in pac_files[pac]:
            print(in_file, end='\t')
            out_file = in_file.replace(dir_in,dir_out).replace('.pdf','_anon.pdf')

            options = pdf_redactor.RedactorOptions()
            options.input_stream = in_file
            options.output_stream = out_file

            if 'tratante' not in pac_data:
                pac_data['tratante'] = "Dr. REYNERIO FAGUNDO SIERRA"

            replace = [re.compile(pac_data[var]) for var in ['nombre','nacimiento','tratante']]
            options.content_filters = [(var,lambda m:'') for var in replace]
            pdf_redactor.redactor(options)
            print(out_file)
def navegar_expedientes(dir_path, ids=None, f_format=None, f_type=None):
    """
    Recorre el arbol de expedientes y regresa los archivos del tipo específicado en un diccionario {expediente:[archivos]}
    
    Parameters
    ----------
    dir_path: str
        Directory where files are found, we suppose that the first level correspond to the IDs
    ids: list
        List of IDs to explore, if list is empty explores all
    f_format: None, '.html' or '.pdf'
        File format to return, if None returns all files regardless of format
    f_type: None, 'nota' or 'lab'
        Type of file depending on the contents, if None returns all files regardless of type. Only works for pdfs.
        
    Returns
    -------
    dict
        Dictionary where the keys are the IDs and the values a list of the selected file paths of that ID
    """
    
    import glob
    from os import walk

    if ids==None:
        _, ids, _ = next(walk(dir_path))
    
    f_pacientes = {}
    for pac in ids:
        pac_path = dir_path + '/'+pac
        pac_files = glob.glob(pac_path+'/**', recursive=True)
        pac_files.pop(0)
        
        if type(f_format)==str:
            pac_files = [f for f in pac_files if f.endswith(f_format)]
        
        if f_type in ['nota', 'lab']:
            if f_type=='nota':
                search_text = "Fecha de elaboración de la nota:"
            elif f_type=='lab':
                search_text = "PruebaResultadoUnidadValores de Referencia"
            pac_files = [f for f in pac_files if search_text in return_pdf_text(f)]
        
        f_pacientes[pac] = pac_files

    return f_pacientes

def return_pdf_text(file):
    """
    Returns the text of a pdf
    """
    import PyPDF2
    
    text = ''
    try:
        pdfFileObj = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for i in range( pdfReader.numPages ):
            pageObj = pdfReader.getPage(i) 
            text += pageObj.extractText() + '\n'
        pdfFileObj.close()
    except: print('Problem with pdf:', file)
    return text
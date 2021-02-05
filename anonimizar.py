def anonimizar(data_dic):
    
    ###6946985085284717763 reportDataRequired z-textbox z-textbox-disd z-textbox-text-disd <--Etiqueta donde viene quién elaboró (Ojo porque viene en sección "pronóstico")
    
    # Buscar diccionario de datos sensibles por paciente
    # Buscar dic nombres agresivo, se tiene que correr en todos los tipos de notas?
    
    # [A-Z][a-z]+ [A-Z][a-z] <-- posible regex para nombres en formato simple ej. Angel Castillo, problema con Angel De la Cruz
    
    # Buscar regexp telefono
   
# Como limpiar direcciones?
   
## Función que sólo regresa si hay o no una dirección, no la extrae directamente, podría servir 
  #  import nltk 
   # def check_location(text):
    #    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
      #      if hasattr(chunk, "label"):
        #        if chunk.label() == "GPE" or chunk.label() == "GSP":
          #          return "True"
        #return "False"
   
return(data_dic)

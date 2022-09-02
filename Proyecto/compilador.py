import re

REdef="def[\s\t]+[a-zA-z][\w]+\({1}(([\s]+)*[a-zA-z][\w]+(([\=])?([\d]+)*[\']?([a-zA-z]+)*[\']?)*[\,]*([\s]+)*[\w])*\){1}\:{1}"
#it has to be modified for some cases yet
REprint="print\((([\"](\w*\s*)*[\"])|([\'](\w*\s*)*[\'])|(([a-zA-Z][0-9]*)*)|((([\d]+)|(([a-zA-Z][0-9]*)+))([\+]|[\-]|[\*]|[\/])(([\d]+)|(([a-zA-Z][0-9]*)+))))*\)"

def leertexto():
    archivo=open("codigo.txt")
    #Validate if file is readable
    if(archivo.readable()):
        lineas=archivo.readlines()
        deteccion(lineas)
    else:
        print("Error al abrir el archivo.")

def deteccion(lineas):
    
   with  open('generador.txt','w') as filename:
    for i in lineas:
        #finds the expression
        patron=re.search(REdef,i)
        patron1=re.search(REprint,i)
        if(patron):
            filename.write(i)
        if(patron1):
            filename.write(i)
        
       
           
def escritura(linea):
    with open('generador.txt', 'w') as filename:
        filename.write(linea)
    filename.close()
    
def prueba():
    with open("codigo.txt") as filename:
        for i in filename:
            pr=re.search("print\((([\"](\w*\s*)*[\"])|([\'](\w*\s*)*[\'])|(([a-zA-Z][0-9]*)*)|((([\d]+)|(([a-zA-Z][0-9]*)+))([\+]|[\-]|[\*]|[\/])(([\d]+)|(([a-zA-Z][0-9]*)+))))*\)\n",i)
            
                
                
leertexto()
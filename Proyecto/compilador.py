import re
REdef="\A(def[\s]*[\t]*([a-zA-Z][\w]+)[\(]([\s]*[\t]*)(([a-zA-Z][\w]*)|([\d]*)|([a-zA-Z][\d]*))([\s]*|[\t]*)?(([\,]([\s]*)[a-zA-Z][\w]*)|([\,]([\s]*)[\d]+)|([\,]([\s]*)[a-zA-Z][\d]+))*([\s]*[\t]*)[\)]\:)"
REprint="print([\s]*|[\t]*)[\(]([\s]*[\t]*)(([\"]([\s]*[\t]*[\w]*)*[\"])|([\']([\s]*[\t]*[\w]*)*[\'])|([a-zA-Z][\w]*)|([a-zA-Z][\d]*)|([\d]*))([\s]*[\t]*)*([\s]*|[\t]*)?(([\,]([\s]*)[a-zA-Z][\w]*)|([\,]([\s]*)[a-zA-Z][\d]*)|([\,]([\s]*)[\d]*)|([\,]([\s]*)[\"]([\s]*[\t]*[\w]*)*[\"])|([\,]([\s]*)[\']([\s]*[\t]*[\w]*)*[\']))*([\s]*[\t]*)*\)"
REfor="for([\s]+[\t]*)[\w]+([\s]+[\t]*)in([\s]+[\t]*)range([\s]*[\t]*)\(([\s]*[\t]*)[\d]+([\s]*[\t]*)[\,]([\s]*|[\t]*)((len([\s]*[\t]*)\(([\s]*[\t]*)([a-zA-z][\w]*)([\s]*[\t]*)\))|([a-zA-Z][\w]*)|([a-zA-Z][\d]*)|([\d]+))([\s]*[\t]*)\)([\s]*[\t]*)\:"
REarray="([a-zA-z][\w]*)([\s]*[\t]*)(([\.]([\s]*[\t]*)append([\s]*[\t]*)[\(]([\s]*[\t]*)[a-zA-Z][\w]*[\s]*[\)])|(\=([\s]*[\t]*)\[([\s]*[\t]*)(([a-zA-Z][\w]*)|([a-zA-Z][\d]*)|(([\-]?)[\d]+)|([\']([\s]*[\t]*[\w]*[\s]*[\t]*)*[\'])|([\"]([\s]*[\t]*[\w]*[\s]*[\t]*)*[\"]))*([\s]*[\t]*)?(([\,]([\s]*[\t]*)[\"]([\s]*[\t]*[\w]*[\s]*[\t]*)*[\"])|([\,]([\s]*[\t]*)[\']([\s]*[\t]*[\w]*[\s]*[\t]*)*[\'])|([\,]([\s]*[\t]*)[a-zA-Z][\w]*)|([\,]([\s]*[\t]*)[a-zA-Z][\d]*)|([\,]([\s]*[\t]*)[\-]?[\d]+))*([\s]*[\t]*)\]))"
#REint="([a-zA-Z][\w]*)([\s]*[\t]*)[\=]([\s]*[\t]*)(((([a-zA-Z][\w]*)([\s]*[\t]*)[\[]([\s]*[\t]*)(([a-zA-Z][\w]*)|[\d]+)([\s]*[\t]*)[\]]([\s]*[\t]*)([\+]|[\-]|[\*]|[\\])([\s]*[\t]*)([a-zA-Z][\w]*)([\s]*[\t]*)[\[]([\s]*[\t]*)(([a-zA-Z][\w]*)|[\d]+)([\s]*[\t]*)[\]])|(([\d]+)([\s]*[\t]*)([\+]|[\-]|[\*]|[\\])([\s]*[\t]*)([a-zA-Z][\w]*)([\s]*[\t]*)[\[]([\s]*[\t]*)(([a-zA-Z][\w]*)|[\d]+)([\s]*[\t]*)[\]])|(([a-zA-Z][\w]*)([\s]*[\t]*)[\[]([\s]*[\t]*)(([a-zA-Z][\w]*)|[\d]+)([\s]*[\t]*)[\]]([\s]*[\t]*)([\+]|[\-]|[\*]|[\\])([\s]*[\t]*)([\d]+))|(([a-zA-Z][\w]*)([\s]*[\t]*)[\[]([\s]*[\t]*)(([a-zA-Z][\w]*)|([\d]+))([\s]*[\t]*)[\]])|(int([\s]*[\t]*)[\(]([\s]*[\t]*)(([a-zA-Z][\w]*)|([\d]+[\.][\d]+)|(([a-zA-Z][\w]*)([\s]*[\t]*)[\[]([\s]*[\t]*)(([a-zA-Z][\w]*)|[\d]+)([\s]*[\t]*)[\]]([\s]*[\t]*)))([\s]*[\t]*)[\)]([\s]*[\t]*)))|(([\d]+)([\s]*[\t]*)([\+]|[\-]|[\*]|[\\])([\s]*[\t]*)([a-zA-Z][\w]*))|(([\d]+)([\s]*[\t]*)([\+]|[\-]|[\*]|[\\])([\s]*[\t]*)([\d]+))|([\d]+)|(([a-zA-Z][\w]*)([\s]*[\t]*)([\+]|[\-]|[\*]|[\\])([\s]*[\t]*)([\d]+))|([a-zA-Z][\w]*))"
REint="([a-zA-Z][\w]*([\s]*[\t]*)[\=]([\s]*[\t]*)(([a-zA-Z][\w]*([\[]([\s]*[\t]*)(([a-z-A-Z][\w]*)|([\d]+))([\s]*[\t]*)[\]])*)|([\d]+))([\s]*[\t]*)(([\+]|[\-]|[\*]|[\/])([\s]*[\t]*)(([\d]+)|(([a-zA-Z][\w]*([\[]([\s]*[\t]*)(([a-z-A-Z][\w]*)|([\d]+))([\s]*[\t]*)[\]])*)|([\d]+))))?)"
REreturn="return([\s]*|[\t]*)+[\(]*[\"]*(([a-zA-Z0-9]?[\w]?)+([\(]*([\s]*[\t]*)*([\,\+|\-|\*|\/]*)*([\s]*|[\t]*)[\)]*)+([\"]*[\)]*))*;*"
REdef2="\A(([a-zA-Z][\w]*)([\s]*[\t]*)[\(]([\s]*[\t]*)((([\"](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\"])|([\'](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\'])|([a-zA-Z][\w]*)|([\d]+))([\s]*[\t]*)([\,]([\s]*[\t]*)(([\"](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\"])|([\'](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\'])|([a-zA-Z][\w]*)|([\d]+)))*)([\s]*[\t]*)[\)])"
REesp="(([\s]{4})+[\w]+)"
REmain=""

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
            patron2=re.search(REfor,i)
            patron3=re.search(REarray,i)
            patron4=re.search(REint,i)
            patron5=re.search(REreturn,i)
            patron6=re.search(REdef2,i)
            
            if(patron):
                filename.write(i)
            if(patron1):
                filename.write(i)
            if(patron2):
                filename.write(i)
            if(patron3):
                filename.write(i)
            if(patron4):
                filename.write(i)
            if(patron5):
                filename.write(i)
            if(patron6):
                filename.write(i)
    
    encapsulacion()
                        
def escritura(linea):
    with open('generador.txt', 'w') as filename:
        filename.write(linea)
    filename.close()       

#Encapsulacion de funciones y lineas del txt generador
def encapsulacion():
    archivo=open("generador.txt")
    if(archivo.readable()):
        lineas=archivo.readlines()
        print(lineas[1])
    else:
        print("Error al abrir el archivo.")
        
    with open('funciones.txt','w') as filename:
        for i in lineas:
            patron=re.search(REdef,i)
            patron7=re.search(REesp,i)
            if(patron):
                filename.write(i)
            if(patron7):
                filename.write(i)
    
    with open('main.txt','w') as filename:
        for i in lineas:
            patron=re.search(REdef,i)
            patron7=re.search(REesp,i)
            #Aqui se obtiene todo lo relacionado al main
            # if(i!=patron and i!=patron7):
            #     filename.write(i)
            if(patron):
                print()
            else:
                if(patron7):
                    print()
                else:
                    filename.write(i)
                         
leertexto()
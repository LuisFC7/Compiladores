import re
REdef="\A(def[\s]*[\t]*([a-zA-Z][\w]+)[\(]([\s]*[\t]*)(([a-zA-Z][\w]*)|([\d]*)|([a-zA-Z][\d]*))([\s]*|[\t]*)?(([\,]([\s]*)[a-zA-Z][\w]*)|([\,]([\s]*)[\d]+)|([\,]([\s]*)[a-zA-Z][\d]+))*([\s]*[\t]*)[\)]\:)"
REprint="print([\s]*|[\t]*)[\(]([\s]*[\t]*)(([\"]([\s]*[\t]*[\w]*)*[\"])|([\']([\s]*[\t]*[\w]*)*[\'])|([a-zA-Z][\w]*)|([a-zA-Z][\d]*)|([\d]*))([\s]*[\t]*)*([\s]*|[\t]*)?(([\,]([\s]*)[a-zA-Z][\w]*)|([\,]([\s]*)[a-zA-Z][\d]*)|([\,]([\s]*)[\d]*)|([\,]([\s]*)[\"]([\s]*[\t]*[\w]*)*[\"])|([\,]([\s]*)[\']([\s]*[\t]*[\w]*)*[\']))*([\s]*[\t]*)*\)"
REfor="for([\s]+[\t]*)[\w]+([\s]+[\t]*)in([\s]+[\t]*)range([\s]*[\t]*)\(([\s]*[\t]*)[\d]+([\s]*[\t]*)[\,]([\s]*|[\t]*)((len([\s]*[\t]*)\(([\s]*[\t]*)([a-zA-z][\w]*)([\s]*[\t]*)\))|([a-zA-Z][\w]*)|([a-zA-Z][\d]*)|([\d]+))([\s]*[\t]*)\)([\s]*[\t]*)\:"
REarray="([a-zA-z][\w]*)([\s]*[\t]*)(([\.]([\s]*[\t]*)append([\s]*[\t]*)[\(]([\s]*[\t]*)[a-zA-Z][\w]*[\s]*[\)])|(\=([\s]*[\t]*)\[([\s]*[\t]*)(([a-zA-Z][\w]*)|([a-zA-Z][\d]*)|(([\-]?)[\d]+)|([\']([\s]*[\t]*[\w]*[\s]*[\t]*)*[\'])|([\"]([\s]*[\t]*[\w]*[\s]*[\t]*)*[\"]))*([\s]*[\t]*)?(([\,]([\s]*[\t]*)[\"]([\s]*[\t]*[\w]*[\s]*[\t]*)*[\"])|([\,]([\s]*[\t]*)[\']([\s]*[\t]*[\w]*[\s]*[\t]*)*[\'])|([\,]([\s]*[\t]*)[a-zA-Z][\w]*)|([\,]([\s]*[\t]*)[a-zA-Z][\d]*)|([\,]([\s]*[\t]*)[\-]?[\d]+))*([\s]*[\t]*)\]))"
REint="([a-zA-Z][\w]*([\s]*[\t]*)[\=]([\s]*[\t]*)(([a-zA-Z][\w]*([\[]([\s]*[\t]*)(([a-z-A-Z][\w]*)|([\d]+))([\s]*[\t]*)[\]])*)|([\d]+))([\s]*[\t]*)(([\+]|[\-]|[\*]|[\/])([\s]*[\t]*)(([\d]+)|(([a-zA-Z][\w]*([\[]([\s]*[\t]*)(([a-z-A-Z][\w]*)|([\d]+))([\s]*[\t]*)[\]])*)|([\d]+))))?)"
REreturn="return([\s]*|[\t]*)+[\(]*[\"]*(([a-zA-Z0-9]?[\w]?)+([\(]*([\s]*[\t]*)*([\,\+|\-|\*|\/]*)*([\s]*|[\t]*)[\)]*)+([\"]*[\)]*))*;*"
REdef2="\A(([a-zA-Z][\w]*)([\s]*[\t]*)[\(]([\s]*[\t]*)((([\"](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\"])|([\'](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\'])|([a-zA-Z][\w]*)|([\d]+))([\s]*[\t]*)([\,]([\s]*[\t]*)(([\"](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\"])|([\'](([\s]*[\t]*)|([\w]*))*([\:]*)([\s]*[\t]*)[\'])|([a-zA-Z][\w]*)|([\d]+)))*)([\s]*[\t]*)[\)])"
REesp="(([\s]{4})+[\w]+)"
#Expresión para eliminación de espacios
REespmain="\A[\s]+"
#Expresiones para  extracción de contenido semantico
REcont="(\"([\w]*[\s]*[\w]*)*\")"
REinput="\A([\w]+[a-zA-z]+)+\=input[\(][\"]([\w]*[\s]*[\w]*)*[\:]*[\s]*[\"][\)]"
REinputvar="\A([\w]+[a-zA-Z]+)"#Para extraer el nombre de variable
REinputcont="([\"]([\w]*[\s]*[\w]*)*[\:]*[\s]*[\"])"#Para extraer contenido del scanf

cam="\A([\w]+[a-zA-Z]+)+[\s]*[\(][\s]*[\"]([\w]*[\s]*)*[\"][\s]*,([\w]+[a-zA-Z]+)+[\)]"
REpam="[\,]([\w]+[a-zA-Z]+)+"#extrae los parametros
REtry="[\s]{2}"

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
        cont=1
        cont2=1
        error=1
        for i in lineas:
            #finds the expression
            patron=re.search(REdef,i)
            patron1=re.search(REprint,i)
            patron2=re.search(REfor,i)
            patron3=re.search(REarray,i)
            patron4=re.search(REint,i)
            patron5=re.search(REreturn,i)
            patron6=re.search(REdef2,i)
            patron7=re.search(REespmain,i)
            if(patron):
                filename.write(i)
            elif(patron1):
                filename.write(i)
            elif(patron2):
                filename.write(i)
            elif(patron3):
                filename.write(i)
            elif(patron4):
                filename.write(i)
            elif(patron5):
                filename.write(i)
            elif(patron6):
                filename.write(i)
            elif(patron7):
                cont2=cont2+1
            else:
                print("\nSintax error in line ",cont,"\n\t\t",i," verify.")
                error=error+1
            cont=cont+1

    if(error>1):
        exit
    else:
        print("Compile and execution succesfully.")
        encapsulacion()

#Encapsulacion de funciones y lineas del txt generador
def encapsulacion():
    archivo=open("generador.txt")
    if(archivo.readable()):
        lineas=archivo.readlines()
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
                cont=0+1
            else:
                if(patron7):
                    cont=2+1
                else:
                    filename.write(i)

    traduccionmain()

#comenzar a validar funciones
def traduccionmain():
    archivo=open("main.txt")
    if(archivo.readable()):
        lineas=archivo.readlines()
    else:
        print("Error al abrir el archivo.")

    #creación de diccionario
    contenido="string"
    diccionario=[]
    parametros=[]
    #Aqui se empieza a escribir en el cpp
    with open('traduccion.cpp','w') as filename:
        #declaración de librerias y estructura fundamental
        identacion="    "
        librerias=["#include <iostream>","#include <cstring>","#include <cmath>","using namespace std;",  "int main()","{"]
        for j in librerias:
            filename.write(j+"\n")

        for i in lineas:

            patron=re.search(REprint,i)
            patron2=re.search(REinput,i)
            an=re.match(cam,i)
            
            # an=re.search(REfuncion,i)
            # an3=re.search(REtry,i)
            if(patron):
                contenido=re.search(REcont,i).group()
                diccionario=contenido
                #Aqui se debe obtener lo que haya dentro de print
                filename.write(identacion+"printf("+contenido+");\n")
                #CHECAR ESTA LINEA SI LLEGA A HABER ALGUN FALLO
            elif(patron2):
                #Primero obtener la variable
                contenido=re.search(REinputvar,i).group()
                diccionario=contenido
                filename.write(identacion+"int "+contenido+"=0;\n")
                #Here we have getting the text of input
                contenidoaux=re.search(REinputcont,i).group()
                filename.write(identacion+"printf("+contenidoaux+");\n")
                diccionario=contenidoaux
                #Third process
                filename.write(identacion+"scanf(\""+"%d\","+contenido+");\n")
                diccionario=contenido
            # elif(an3):
            #     contenido=re.search(REpam,i).group()
            #     print(contenido)






leertexto()
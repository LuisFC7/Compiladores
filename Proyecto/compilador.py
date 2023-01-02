import re
import numpy as np
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
######################Expresiones regulares
REfunc="\Aimpresion[\s]*[\(][\s]*[\"]([a-zA-Z]+[\s]*)*[\"][\,][a-zA-Z]+[\)]"
# REfunc="\Aimpresion[\(][\"][\s]*([\w]*[\s]*)*[\:]*[\s]*[\"][\s]*[\,][\s]*([\w]+[a-zA-Z]+)+[\s]*[\)]"
REnombrefun="\A([\w]+[a-zA-Z]+)"
REpam1="[\"][\s]*([\w]*[\s]*)*[\"]"
REpam2="[\,]([\w]+[a-zA-Z]+)+"#extrae los parametros
#####
REfill="\A([\w]+[a-zA-Z]+)+[\s]*[\=][\s]*([\w]+[a-zA-Z]+)+[\s]*[\(][\s]*int[\s]*[\(][\s]*([\w]+[a-zA-Z]+)+[\s]*[\)][\s]*[\)]"
REnomf="[\=]([\w]+[a-zA-Z]+)+"
############
RElastfun="([\w]+[a-zA-Z]+)+[\s]*[\=][\s]*([\w]+[a-zA-Z]+)+[\s]*[\(][\s]*([\w]+[a-zA-Z]+)+[\s]*[\)]"
#especiales
REtry="\Aimpresion"
REtrypam1="[\"]([\w]+[\s]*)*[\:][\s]*[\"]"
REtrypam2="[\,][\s]*([\w]+[a-zA-Z]+)+"
######################Aqui comienza la validación de la segunda parte, expresiones regulares para las funciones
############Expresiones regulares para tipo de datos
RElist="([a-zA-Z]+[\d]*)[\s]*[\=][\s]*\[[\s]*\]"
REnum="([a-zA-Z]+[\d]*)[\s]*[\=][\s]*(([\d]+)|(([a-zA-Z]+[\d]*)[\s]*\[[\d]+\]))"
##Esta RE sirve para extraer la cadena despues del return
RElimp="[=][\s]*([a-zA-Z]+[\d]*)*\[(([a-zA-Z]+[\d]*)|([\d]*))[\s]*\]"
RElimp2="[=][\s]*[\d]+"
###Expresiones finales
RElimpf="[\(][\s]*([a-zA-Z]+[\d]*)[\s]*[\)]"
REprintf="\([\s]*[a-zA-Z]+[\d]*[\s]*[\,][\s]*[a-zA-Z]+[\d]*[\s]*\)"
REprintf2="((\([\s]*[a-zA-Z]+[\d]*[\s]*[\,][\s]*[a-zA-Z]+[\d]*[\s]*\))|(\([\s]*[a-zA-Z]+[\d]*[\s]*\))|(\([\s]*[\"][\s]*([a-zA-Z]+[\d]*[\s]*)*[\"][\,][\"][\s]*([a-zA-Z]+[\d]*[\s]*)*[\s]*[\"]\))|(\([\s]*[\"][\s]*([a-zA-Z]+[\d]*[\s]*)*[\"][\,]([a-zA-Z]+[\d]*)\)))"
REvariabled="\A[\s]{4}([a-zA-Z]+[\d]*)[\s]*[\=][\s]*(([\[][\s]*[\]])|([\d]+)|([a-zA-Z]+[\d]*))"
REdecarray="([a-zA-Z]+[\d]*)[\s]*[\=][\s]*[\[][\s]*[\]]"
REvariables="([a-zA-Z]+[\d]*)[\s]*[\=][\s]*(([\d]+)|(([a-zA-Z]+[\d]*)[\s]*[\[](([\d]+)|(([a-zA-Z]+[\d]*))))[\s]*[\]])"
REvariablesimple="([a-zA-Z]+[\d]*)[\s]*[\=][\s]*(([\d]+)|([a-zA-Z]+[\d]*))"
REizq="([a-zA-Z]+[\d]*)[\s]*[\=]"
REder="[\=][\s]*([a-zA-Z]+[\d]*(([\[](([a-zA-Z]+[\d]*)|([\d]+))[\s]*[\]])*)|([\d]+))"
#Expresiones para validación de for
REforl1="[\s]{8}([a-zA-Z]+[\d]*)[\s]*(([\=][\s]*int[\s]*[\(]input[\s]*\([\s]*\"[\s]*([a-z-A-Z]+[\d]*[\s]*)*\:[\s]*\"[\s]*\)[\s]*\))|([\.][\s]*append\([\s]*([a-zA-Z]+[\d]*)[\s]*\)))"
REforl2="[\s]{8}([a-zA-Z]+[\d]*)[\s]*(([\=][\s]*([a-zA-Z]+[\d]*)([\+]|[\*]|[\/]|[\-])[\s]*([a-zA-Z]+[\d]*)([\s]*[\[]([a-zA-Z]*[\d]*)[\s]*[\]]))|([\=]([a-zA-Z]+[\d]*)([\s]*[\[]([a-zA-Z]*[\d]*)[\s]*[\]])([\+]|[\*]|[\/]|[\-])([a-zA-Z]+[\d]*)))"
REforl3="[\"][\s]*([a-zA-Z]+[\d]*[\s]*[\:]*)*[\s]*[\"]"
REforl4="([a-zA-Z]+[\d]*)[\s]*[\=][\s]*int[\s]*[\(][\s]*input[\s]*[\(][\s]*[\"]([a-zA-Z]*[\d]*[\s]*[\:]*[\(]*[\)]*)*[\s]*[\"][\s]*[\)][\s]*[\)]"#nueva para input
REforl5="[\s]{8}([a-zA-Z]+[\d]*)[\s]*[\.][\s]*(append)[\s]*[\(][\s]*([a-zA-Z]+[\d]*)[\s]*[\)]"#Nueva para append
#Expresiones regulares para limpieza y obtención de variables para for
RElimpfor="range[\s]*[\(][\s]*(([a-z-A-Z]+)|([\d]+))[\s]*[\,][\s]*(([a-z-A-Z]+)|([\d]+)|(len[\s]*[\(][\s]*([a-zA-Z]+[\d]*)[\s]*[\)][\s]*))[\)][\s]*\:"
RElimpforr1="[,][\s]*([a-zA-Z]+[\d]*)"
RElimpright="[\,][\s]*(([a-zA-Z]+[\d]*[\s]*[\)])|(len[\s]*[\(]([a-z-A-Z]+[\d]*)[\s]*[\)][\s]*[\)]))"
RElimpright2="[\s]*([a-zA-Z]+|[\d]+)[\s]*[\(]"
RElimpleft="(([a-zA-Z]+[\d]*)|([\d]+))[\s]*[\(][\s]*(([a-zA-Z]+[\d]*)|([\d]+))[\,]"
REconvlen="len[\s]*\(([a-z-A-Z]+[\d]*)[\s]*\)"
#Limpieza de funciones
REappend="[\.][\s]*append[\s]*[\(][\s]*([a-zA-Z]+[\d]*)[\s]*[\)]"
REbfun="([a-zA-Z]+[\d]*)[\s]*[\=][\s]*(([a-zA-Z]+[\d]*)|([\d]+)|(([a-zA-Z]+[\d]*)[\s]*[\[][\s]*(([a-zA-Z]+[\d]*)|([\d]+))[\s]*[\]]))[\s]*([\+]|[\-]|[\*]|[\/])[\s]*(([a-zA-Z]+[\d]*)|([\d]+)|(([a-zA-Z]+[\d]*)[\s]*[\[][\s]*(([a-zA-Z]+[\d]*)|([\d]+))[\s]*[\]]))"
REbfunr="[\=][\s]*((([\w]+)([\+]|[\-]|[\*]|[\/])([\w]+)[\[]*([\w]+)[\s]*[\]]*)|(([\w]+)[\s]*[\[][\s]*([\w]*)[\s]*[\]]([\+]|[\-]|[\*]|[\/])([\w]+)[\[]*([\w]+)[\s]*[\]]*))"
REbfunr2="([\+]|[\-]|[\*]|[\/])(([a-zA-Z]+[\d]*)|([\d]+))[\s]*([\[][\s]*(([a-zA-Z]+[\d]*)|[\d]+)[\s]*[\]])*"#Para borrar nombres de variables o numeros
REbfunr3="[\w]+[\s]*[\=]"
REbfunrl="(([a-zA-Z]+[\d]*)|([\d]+)|(([a-zA-Z]+[\d]*)[\s]*[\[](([a-zA-Z]+[\d]*)|([\d]*))[\s]*[\]]))([\+]|[\-]|[\*]|[\/])"
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
    funciones=[]
    variables=[]
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
            patron3=re.search(REfunc,i)
            patron4=re.search(REfill,i)
            patron5=re.search(RElastfun,i)
            patron6=re.search(REtry,i)
            
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
                filename.write(identacion+"scanf(\""+"%d\",&"+contenido+");\n")
                diccionario=contenido
            elif(patron3):
                re.purge()
                contenido=re.search(REnombrefun,i).group()
                funciones.append(contenido)
                filename.write(identacion+contenido)
                #obtenemos el primer parametro
                contenido=re.search(REpam1,i).group()
                parametros.append(contenido)
                filename.write("("+contenido)
                #obtenermos el segundo parametro
                contenido=re.search(REpam2,i).group()
                parametros.append(contenido[1:])
                filename.write(contenido+");\n")
            elif(patron4):
                #primero extraemos el nombre de la variable del array a declarar
                #hay que declarar primero una variable para el tamaño del array
                tam="tam"
                filename.write(identacion+"int "+tam+"="+parametros[1]+";\n")
                contenido=re.search(REinputvar,i).group()
                variables.append(contenido)
                filename.write(identacion+"int datos["+tam+"];\n")
                variables.append("datos")
                #Ahora se extrae el nombre de la función declarada
                contenido=re.search(REnomf,i).group()
                funciones.append(contenido[1:])
                filename.write(identacion+contenido[1:]+"("+parametros[1]+");\n")
            elif(patron5):
                #obtener el nombre de la variable
                contenido=re.search(REinputvar,i).group()
                variables.append(contenido)
                filename.write(identacion+"int "+contenido+"=0;\n")
                #nombre de  la funcion
                contenido=re.search(REnomf,i).group()
                funciones.append(contenido[1:])
                filename.write(identacion+contenido[1:]+"("+variables[1]+");\n")
            elif(patron6):
                contenido=re.search(REnombrefun,i).group()
                funciones.append(contenido)
                filename.write(identacion+contenido)
                contenido=re.search(REtrypam1,i).group()
                parametros.append(contenido)
                filename.write("("+contenido)
                contenido=re.search(REtrypam2,i).group()
                parametros.append(contenido[1:])
                filename.write(contenido+");\n")
            else:
                print("\nSintax error in line \n\t\t",i," verify.")
        filename.write("}")  
    
    
    #Aqui ya se encapsularon las funciones en una multilista
    encapsulacionfunciones()
        
def encapsulacionfunciones():
    archivo2=open("funciones.txt")
    if(archivo2.readable()):
        lineas2=archivo2.readlines()
    else:
        print("Error al abrir el archivo.")  
    
    comp=[]#este array va servir para comparar con la función de main
    funciones=[]
    informacion=[]
    band=0
    cont=0
            
    #Nueva propuesta
    for i in lineas2:
        cont=cont+1
        patron=re.search(REdef,i)
        if(patron and band==1):
            informacion.append(funciones.copy())
            comp.append(i)
            funciones.clear()
            funciones.append(i)
        elif(patron and band==0):
            funciones.append(i)
            comp.append(i)
            band=1
        else:
            funciones.append(i)
        if(cont==len(lineas2)):
            informacion.append(funciones.copy())
            
    tipofun(informacion)

#En esta función ya se empezó a traducir la parte de las funciones
def tipofun(funciones):
    variables=[]
    tipo=[]
    contenido=[]
    nomfun=[]
    for i in range(len(funciones)):
        for j in range(len(funciones[i])):
            patron=re.search(RElist,funciones[i][j])#patron return
            patron2=re.search(REnum,funciones[i][j])
            patron3=re.search(REreturn,funciones[i][j])
            if(patron):
                #aqui se encuentran las variables para determinar el tipo de return
                variables.append(funciones[i][j])
                tipo.append("array")
            if(patron2):
                variables.append(funciones[i][j])
                tipo.append("int")
            ####Aqui se implementa la busqueda del return
            if(patron3):
                contenido.append(funciones[i][j])
                nomfun.append(funciones[i][0])
    #nomfun nos sirve para guardar los nombres de las  funciones que sean de tipo return
    #limpieza de variables
    Svariable=",".join(variables)
    Svariable=re.sub("\n|[\s]|"+RElimp+"|"+RElimp2,"",Svariable)
    variables.clear()
    variables=Svariable.split(",")
    #limpieza para lista de return
    Sreturn=",".join(contenido)
    Sreturn=re.sub("\n|[\s]|return|"+RElimp+"|"+RElimp2,"",Sreturn)
    contenido.clear()
    contenido=Sreturn.split(",")

    #Aqui ya se pueden clasificar las funciones por tipo int o void
    #Siguiente etapa, hacer match entre con cada variable
    #contenido guarda las coincidencias de return y variables las coincidencias de variables para posible match con return
    #se procede a la escritura de funciones
    arr=[]
    for i in range(len(contenido)):
        check=variables.index(contenido[i])#Indica la posicion en la que se encuentra la coincidencia
        if(tipo[check]=="int"):
            arr.append(tipo[check])
        else:
            arr.append(tipo[check])
        
    #Aqui se da la traducción de las funciones completas
    archivo=open("funciones.txt")
    if(archivo.readable()):
        lineas=archivo.readlines()
    else:
        print("Error al abrir el archivo.")
        
    #Aqui se realiza la traducción de las funciones
    #se invoca directamente a la función de análisis de for
    ciclos,posiciones,shadow=idenfor()
    REext="\([\s]*([a-zA-Z]+[\d]*)[\s]*\)"
    REtipo="([a-zA-Z]+[\d]*)[\s]*[\=]"
    identacion="    "
    contador=0#va servir como detector de impresión de llaves
    iterador=0#sirve para obtener posición de los ciclo for
    diccionariovar=[]
    with open('traduccionfun.cpp','w') as filename:
        for i in lineas:
            patron=re.search(REdef,i)
            patron2=re.search(REprint,i)
            patron3=re.search(REvariabled,i)
            patron4=re.search(REfor,i)
            if(patron):
                if((i in nomfun)==True):
                    var=re.search(REext,i).group()
                    nom=nomfun.index(i)
                    if(arr[nom]=="array"):
                        arr[nom]="int"
                    Slimp=re.sub("def|[\s]|\:|"+RElimp2,"",i)
                    writing=arr[nom]+" "+Slimp+"{"
                    if(contador!=0):
                        filename.write("}\n")
                    filename.write(writing+"\n")
                else:
                    Slimp=re.sub("def|[\s]|\:|"+RElimp2,"",i)
                    writing="void "+Slimp+"{"
                    filename.write(writing+"\n")
            if(patron2):
                var=re.search(REprintf2,i).group()#obtenemos los parametros ya sea uno o varios
                filename.write(identacion+"printf"+var+";"+"\n")
            if(patron3):
                #Primero hacer el caso de análisis del arreglo
                p1=re.search(REdecarray,i)
                p2=re.search(REvariablesimple,i)
                if(p1):
                    if(p1 in diccionariovar):
                        var=diccionariovar[iterador]
                        filename.write(identacion+"vector<int> "+var+";\n")
                    else:
                        var=re.sub("[\s]|[\=]|[\[]|[\]]","",i)
                        filename.write(identacion+"vector<int> "+var+";\n")
                        diccionariovar.append(var)
                #Ahora para el segundo caso variable simple solo casos sin asignación de array
                if(p2):
                    if(p2 in diccionariovar):
                        var=diccionariovar[iterador]
                        tipo=re.sub("\s|"+REtipo,"",i)
                        filename.write(identacion+"int "+var+" = "+tipo+";\n")
                        diccionariovar.append(var)
                    else:
                        var=re.sub("\s|"+REder,"",i)
                        tipo=re.sub("\s|"+REtipo,"",i)#se determina el tipo de variable
                        #Aqui se extrae el tipo
                        filename.write(identacion+"int "+var+" = "+tipo+";\n")
                        diccionariovar.append(var)
            #Aqui se comienza a pasa directo la parte del análisis for
            if(patron4):
                if(iterador in posiciones):
                    for comienzo in range(len(ciclos)):
                        tope=re.search("\n    }",ciclos[comienzo])
                        if(tope):
                            filename.write(ciclos[comienzo])
                            comienzo=comienzo
                            break
                        else:
                            filename.write(ciclos[comienzo])
                            
                    
            contador=contador+1
            iterador=iterador+1
                # #Aqui se debe obtener lo que haya dentro de print
                # filename.write(identacion+"printf("+contenido+");\n")
        filename.write("}")      
        print(posiciones)
#Función que realiza todo el análisis referente a la sintaxis del ciclo for,      
def idenfor():
    archivo=open("funciones.txt")
    if(archivo.readable()):
        lineas=archivo.readlines()
    else:
        print("Error al abrir el archivo.")
        
    posicion=[]
    cadenas=[]
    contador=0
    escritura=[]
    identacion="    "
    identacion2="       "
        
    #Aqui se obtuvieron las coincidencias de todos los for
    for i in lineas:
        patron=re.search(REfor,i)
        patron2=re.search(REforl1,i)
        patron3=re.search(REforl2,i)
        # patron4=re.search(REforl3,i)
        if(patron):
            cadenas.append(i)
            posicion.append(contador)
        if(patron2):
            cadenas.append(i)
            posicion.append(contador)
        if(patron3):
            cadenas.append(i)
            posicion.append(contador)
        
        contador=contador+1
    
    llave=0
    shadow=[]
    cntshadow=0
    for i in range(len(cadenas)):
        #Aqui se ingresa el contador para imprimir la llave de fin de ciclo
        patron=re.search(REfor,cadenas[i])
        patron2=re.search(REconvlen,cadenas[i])
        patron3=re.search(REforl4,cadenas[i])
        patron5=re.search(REforl5,cadenas[i])
        patron6=re.search(REbfun,cadenas[i])
        if(patron):
            if(llave==0):
                llave=1
            else:
                escritura.append("\n    }\n")
            Slimp=re.sub("for|[\s]|in|"+RElimpfor,"",cadenas[i])
            #Aqui se comienza con la primera limpieza del rango uno(va en la detección del ciclo for)
            r1=re.sub("for|[\s]|in|range|\:|"+RElimpright,"",cadenas[i])
            r2=re.sub("for|[\s]|in|range|\:","",cadenas[i])
            r2=re.sub(RElimpleft,"",r2)
            r1=re.sub(RElimpright2,"",r1)#Primer rango
            r2 = r2[:-1]#segundo rango
            if(patron2):
                #Segunda limpieza para el rango 2 en caso de ser de tipo len
                r2=re.sub("len|[\s]|\(|\)","",r2)
                r2="sizeof("+r2+")"
            escritura.append(identacion+"for(int "+Slimp+"="+r1+"; "+Slimp+"<"+r2+"; "+Slimp+"++){\n")
            # shadow.append(cntshadow)
        if(patron3):
            #Primero obtener nombre de variable
            variable=re.sub("int|input|\(|\)|[\s]|\=|"+REforl3,"",cadenas[i])
            aux=variable
            variable=identacion2+"int "+variable+"=0;\n"
            escritura.append(variable)
            #Ahora obtener parte del print
            comillas=re.sub("int|input|\(|\)|\=|"+aux,"",cadenas[i])
            comillas=re.sub("\A[\s]*[\"]|[\"][\s]*","",comillas)
            comillas=identacion2+"printf(\""+comillas+"\");\n"
            escritura.append(comillas)
            #Ahora se ingresa la variable
            ingresar=identacion2+"scanf(\""+"%d\",&"+aux+");\n"
            escritura.append(ingresar)
        if(patron5):
            variable=re.sub("\s|"+REappend,"",cadenas[i])
            #Se obtiene lo que hay dentro de los parentesis
            contenido=re.sub("\s|\.|append|\(|\)|"+variable,"",cadenas[i])
            escritura.append(identacion2+variable+" = "+contenido+";\n")
        if(patron6):
            variable=re.sub("\s|"+REbfunr,"",cadenas[i])
            op1=re.sub("\s|"+REbfunr2,"",cadenas[i])
            op1=re.sub("\s|"+REbfunr3,"",op1)#se obtiene el primer valor de operación
            op2=re.sub("\s|"+REbfunrl,"",cadenas[i])
            op2=re.sub("\s|"+REbfunr3,"",op2)
            #Ahora se obtiene el operador
            op=re.sub("\s|\=|\w|\[|\]","",cadenas[i])
            escritura.append(identacion2+variable+" = "+op1+" "+op+" "+op2+";\n")
    
    escritura.append("\n    }\n")
    
    #obtener finalmente 
    for j in range(len(escritura)):
        patronex=re.search("for",escritura[j])
        if(patronex):
            shadow.append(cntshadow)
        cntshadow=cntshadow+1
    
    # Se retornan los siguientes parametros
    print(shadow)
    print(escritura)
    return escritura,posicion,shadow
               
leertexto()

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
int main()
{
    printf("Bienvenido a compiladores");
    int Datos=0;
    printf("   Datos a introducir: ");
    scanf("%d",Datos);
    impresion("El usuario introducira",Datos);
    const tam=Datos;
    int datos[tam];
    llenarLista(Datos);
    int Suma=0;
    sumatoria(datos);
    impresion("La sumatoria de los numeros es: ",Suma);
    int Producto=0;
    calcularProducto(datos);
    impresion("El producto de los numeros es: ",Producto);
}
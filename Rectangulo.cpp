#include <iostream>
using namespace std;
#include "Rectangulo.h"
Rectangulo::Rectangulo () {
	base=1;
	altura=1;
	TR=CUADRADO;
	count++;
}
Rectangulo::Rectangulo (int b, int a) {
	base=b;
	altura=a;	
	TR= (b!=a? NOCUADRADO : CUADRADO);
	count++;
}
void Rectangulo::ImprimeContador(){
	cout <<"Valor de count "<<count<<" \n";
	cout <<"base"<<base<<" altura: "<<altura<<"\n";
	switch (TR) {
		case CUADRADO: cout <<"CUADRADO  \n"; break;
		case NOCUADRADO: cout <<"NO CUADRADO  \n"; break;
		default: cout <<"DESCONOCIDO \n"; break;
	}
}
void Rectangulo::dimensiones(int a, int b) {
	base = a;
	altura = b;
}

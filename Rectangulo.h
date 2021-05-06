class Rectangulo { 
	public:
		Rectangulo ();
		Rectangulo (int b, int a); 	
		// CUADRADO=0, NOCUADRADO=1
		enum TipoRectangulo {CUADRADO, NOCUADRADO};
		
		TipoRectangulo getTipoRectangulo () {return TR; }
		static int count;
		static float PI;
		int Cuenta;
		void ImprimeContador();
		void dimensiones(int a, int b);
		int area () { return base*altura; }
	private:
		TipoRectangulo TR;
		int base;
		int altura;
};

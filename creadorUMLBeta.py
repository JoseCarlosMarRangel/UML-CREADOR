print("Hola Bienvenido al creador de UML\n")
print("Como se llama tu archivo")
nombre = input()
print("\n")
archivo = open(nombre)
#mensaje = archivo.read()
#print(mensaje)

#escritura = mensaje
Lines = archivo.readlines()
for line in Lines:
    print(line)
    palabras = line.split(" ")


List=[]
lineNumber=1
line_count=0
palabra = "class"
palabra2 ="void"
palabra3 = "static"
palabra4 = "int"
r=0
r2=0
r3=0
r4=0
with open(nombre) as reader:
    line = reader.readline()
    print ("Archivo Ingresado:\n")
    while line != '': 
        print(line, end='') 
        List.append(line.replace("\n", "")) 
        line = reader.readline()
        line_count += 1

        if palabra in line:
        	r+=1
        if palabra2 in line:
        	r2+=1
        if palabra3 in line:
        	r3+=1
        if palabra4 in line:
        	r4+=1
        
print ("\n")
print ("Numero de lineas:")
print (line_count)
print ("Conteo de Palabras:")
print ("La palabra ",palabra,"se repitió ",r," veces en el código")
print ("La palabra ",palabra2,"se repitió ",r2," veces en el código")
print ("La palabra ",palabra3,"se repitió ",r3," veces en el código")
print ("La palabra ",palabra4,"se repitió ",r4," veces en el código")


archivo.close()
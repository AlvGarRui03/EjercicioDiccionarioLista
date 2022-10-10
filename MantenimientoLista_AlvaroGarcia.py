listaArticulos = []
entrada=""

#Usamos un metodo para buscar la posicion en la lista mediante el codigo del objeto
def buscarObjeto(codigo):
    
    for diccionario in listaArticulos:
        if (diccionario.get("Codigo articulo") == codigo):
            return listaArticulos.__getitem__(listaArticulos.index(diccionario))
           
        return None
#Metodo para dar de alta        
def alta():
    cod_articulo=input("Introduzca el codigo de articulo que quiera dar de alta ")
    #Compronamos que no este ya un articulo con ese codigo
    while buscarObjeto(cod_articulo):
          cod_articulo=input("Introduzca el codigo de articulo que quiera dar de alta que no este ya incluido")
    nombre=input("Introduzca el nombre del articulo ")
    descripcion = input("Introduzca la descripcion del articulo ")
    precio = input("Introduzca el precio del articulo ")
    #Metemos los datos al diccionario
    diccionario={"Codigo articulo":cod_articulo,
                 "Nombre":nombre,
                 "Descripcion":descripcion,
                 "Precio":precio
    }
    #Metemos en la lista el diccionario
    listaArticulos.append(diccionario)
#Metodo para dar de baja    
def baja():
    cod=input("Introduzca el codigo del producto que desee dar de baja ")
    articulo=buscarObjeto(cod)
    #Comprobamos que exista ese codigo
    if (articulo != None):
        listaArticulos.remove(articulo)
        print("Se ha eliminado el articulo de codigo " +cod)
    else:
        print("El codigo introducido no esta en la lista")    
#Metodo para modificar los datos del objeto
def modificacion():
    Codigo = input("Introduzca el código del producto que quiera modificar ")
    articulo = buscarObjeto(Codigo)
    if articulo!=None:
        nombre=input("Introduzca el nuevo nombre ")
        articulo.update({"Nombre":nombre})
        descripcion=input("Introduzca la nueva descripcion ")
        articulo.update({"Descripcion ":descripcion})
        precio=input("Introduzca el nuevo precio ")
        articulo.update({"Precio ":precio})
#Metodo para comprobar si el articulo esta el la lista o no  
def busquedas(codArticulo):
    articulo=buscarObjeto(codArticulo)
    if articulo in listaArticulos:
        print("El articulo con codigo "+ codArticulo+ " se encuentra dentro de la lista ")
    else:
        print("El articulo no esta en la lista ")
#Metodo para listar los objetos
def listar():
    for articulo in listaArticulos:
        print (articulo)
#Menu para poder seleccionar las opciones
while entrada != "6":
    entrada = input("Introduzca un numero de 1 a 6: " +
        "\n 1: Para dar un articulo de alta " +
        "\n 2: Para dar un articulo de baja " +
        "\n 3: Para modificar un articulo " +
        "\n 4: Para buscar en función del codigo del articulo " +
        "\n 5: Para listar todos los articulos " +
        "\n 6: Para salirse del programa ")
    if entrada == "1":
        alta()
    elif entrada == "2":
        baja()
    elif entrada == "3":
        modificacion()
    elif entrada=="4":
        codigo=input("Introduzca el codigo del articulo que desea buscar ")
        busquedas(codigo)
    elif entrada=="5":
        listar()
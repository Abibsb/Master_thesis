# import para open
import io
# abro el archivo
archivo = open('1A1T.cif_ringEdges', 'r')
# armo un array de lineas
lineas = archivo.readlines()
# cierro el archivo
archivo.close()
# armo la variable donde parseo
parser = []
# para cada linea
for nlinea in lineas[1:]:
    # separo cada linea por tab
    linea = nlinea.split('\t')
    # comparo los identificadores de cadena
    if linea[0][0] != linea[2][0]:
        # comparo el tamaño del código alfabético
        if len(linea[0].split(':')[3]) != len(linea[2].split(':')[3]):
            # si son las que quiero, las agrego a parser
            parser.append(nlinea)
print(parser)

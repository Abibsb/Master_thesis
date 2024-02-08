# import para open y manejo de archivos
import io
import os
# iterar archivos de la carpeta donde esta el script

#meter todas una lista de inputs
# subsetear todos los archivos que contengan _ringEdges

lista_inputs = [archivo for archivo in os.listdir('.') if "ringEdge" in archivo]
parser = ['PDBID\tNodeId1\tInteraction\tNodeId2\tDistance\tAngle\tEnergy\tAtom1\tAtom2\tDonor\tPositive\tCation\tOrientation Model\n']
for item in lista_inputs:
    # abro el archivo
    archivo = open(item, 'r')
    # armo un array de lineas
    identificador = item.split('.')[0]
    lineas = archivo.readlines()
    # cierro el archivo
    archivo.close()
    # armo la variable donde parseo
    # para cada linea
    for nlinea in lineas[1:]:
        # separo cada linea por tab
        linea = nlinea.split('\t')
        # comparo los identificadores de cadena
        if linea[0][0] != linea[2][0]:
            # comparo el tamaño del código alfabético
            if len(linea[0].split(':')[3]) != len(linea[2].split(':')[3]):
                # si son las que quiero, las agrego a parser
                parser.append(identificador+'\t'+nlinea)
    # print(parser[1])
    # exportar parser como txt file de tablas

with open('maxitabla.csv', mode='w') as file:
    file.write(''.join(parser))

''' ESTO ES EL TRABAJO HORRIBLE QUE HICISTE, ABBY, QUE DEBERÍA DARTE VERGÜENZA, ES INMORAL E INACEPTABLE
    f = open(identificador + '.csv', 'r')
    temp = f.read()
    f.close()
    f = open(identificador + '.csv', 'w')
    f.write)
    f.write(temp)
    f.close()'''

#abrirlo en el parseo y con un for ir recorriendo cada uno\
#por cada input, generar un output con las filas resultantes del parseo y que tenga como nombre 'ID'_parceo.txt

#copiar todas las filas de todos los outputs en una tabla
#anadir una columna que contenga el ID del archivo de parceo de donde surgio la fila


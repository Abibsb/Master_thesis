#11/09/22
#Abrir dataset. Tener en cuenta que hay que poner el nombre del archivo y tenerlo en la misma carpeta que el script. 
#Se guardan todas las lineas que haya en el dataset en "lineas"
archivo = open('tablafull.csv', 'r')
lineas = archivo.readlines()
archivo.close()
#Generar las variables de las interacciones a contar y el ID del .pdb correspondiente
id=''
hbond_ls=0
hbond_lm=0
hbond_sl=0
hbond_ml=0
vdw_ls=0
vdw_lm=0
vdw_sl=0
vdw_ml=0
#Generar un nuevo archivo donde se guarde el parseo generado. Generar header de nueva dataset.
file = open('estadisticas_tablafull.csv', mode='w')
parser = 'PDBID\tHBOND_LIG_SC\tHBOND:LIG_MC\tHBOND:SC_LIG\tHBOND:MC_LIG\tVDW:LIG_SC\tVDW:LIG_MC\tVDW:SC_LIG\tVDW:MC_LIG\n'
file.write(parser)
#Este for chequea primero que el id del .pdb sea diferente al que esta guardado previamente. Si no es el mismo, entonces se suma 1 a la variable de interaccion que se
#encuentre en la columna de interaccion
#Cerrar archivo generado con los resultados del for
for nlinea in lineas[1:]:
    linea = nlinea.split('\t')
    if linea[0] != id:
        if id != '':
            parser = id+'\t'+str(hbond_ls)+'\t'+str(hbond_lm)+'\t'+str(hbond_sl)+'\t'+str(hbond_ml)+'\t'+str(vdw_ls)+'\t'+str(vdw_lm)+'\t'+str(vdw_sl)+'\t'+str(vdw_ml)+'\n'
            file.write(parser)
        id = linea[0]
        hbond_ls=0
        hbond_lm=0
        hbond_sl=0
        hbond_ml=0
        vdw_ls=0
        vdw_lm=0
        vdw_sl=0
        vdw_ml=0
    if linea[2] == 'HBOND:LIG_MC':
        hbond_lm += 1
    if linea[2] == 'HBOND:LIG_SC':
        hbond_ls += 1
    if linea[2] == 'HBOND:MC_LIG':
        hbond_ml += 1
    if linea[2] == 'HBOND:SC_LIG':
        hbond_sl += 1
    if linea[2] == 'VDW:LIG_MC':
        vdw_lm += 1
    if linea[2] == 'VDW:LIG_SC':
        vdw_ls += 1
    if linea[2] == 'VDW:MC_LIG':
        vdw_ml += 1
    if linea[2] == 'VDW:SC_LIG':
        vdw_sl += 1

file.close()

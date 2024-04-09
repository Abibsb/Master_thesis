source: https://github.com/mgalardini/pdb2uniprot

##Steps

1. Descargué el repo como zip --> unzip
2. Generé mi propio archivo "pdb_list.txt" con 10 pdbs respetando el formato dado por el autor
3. Abrí la carpeta local del repo en un terminal y copié el mini-script bash dado por el autor:

bash prepare_commands.sh > commands.txt
parallel --jobs 1 --progress < commands.txt
echo -e "pdb id\tpdb chain\tpdb residue\tpdb position\tuniprot id\tuniprot residue\tuniprot position" > pdb2uniprot.tsv
find out/ -type f -name '*tsv' -exec cat {} >> pdb2uniprot.tsv \;

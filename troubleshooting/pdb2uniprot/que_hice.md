source: https://github.com/mgalardini/pdb2uniprot

##Steps

1. Descargué el repo como zip --> unzip
2. Generé mi propio archivo "pdb_list.txt" con 10 pdbs respetando el formato dado por el autor
3. Abrí la carpeta local del repo en un terminal y copié el mini-script bash dado por el autor:

bash prepare_commands.sh > commands.txt
parallel --jobs 1 --progress < commands.txt
echo -e "pdb id\tpdb chain\tpdb residue\tpdb position\tuniprot id\tuniprot residue\tuniprot position" > pdb2uniprot.tsv
find out/ -type f -name '*tsv' -exec cat {} >> pdb2uniprot.tsv \;

4. Output dado:
![image](https://private-user-images.githubusercontent.com/90363624/320711639-453da024-39bc-43d9-8b07-6bb5e5887d18.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTI2MzM0NDEsIm5iZiI6MTcxMjYzMzE0MSwicGF0aCI6Ii85MDM2MzYyNC8zMjA3MTE2MzktNDUzZGEwMjQtMzliYy00M2Q5LThiMDctNmJiNWU1ODg3ZDE4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA0MDklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNDA5VDAzMjU0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTcxYWJiMDNkZjNiYjUyNTE0YTc4MDQ4NzZlYzg1ZGFjNGY0NDU4NDBjZDhlMzIxYjI3YTk1NTg3MzRiYjM4NzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.7X7EYMMR5jUng5C4xlDbEyQOZrvLfx0YQ6_QUsCfFFc)

5. el .tsv generado está vacío, sólo tiene el header generado en "echo e- "pdb id\tpdb chain\tpdb residue\tpdb position\tuniprot id\tuniprot residue\tuniprot position"

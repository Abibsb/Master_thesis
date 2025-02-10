###############################################################################
import os
from Bio import SeqIO

def filter_fasta_by_uniprot_and_track_pdb(csv_file, fasta_folder, output_folder):
    import csv

    # Step 1: Parse CSV to map Pfam, UniProt, and PDB IDs
    pdb_uniprot_pfam_map = {}
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            pdb_id = row["PDB ID"]
            pfam_codes = row["Pfam Code"].replace(" ", "").split(",")
            uniprot_codes = row["UniProt Code"].replace(" ", "").split(",")
            for pfam in pfam_codes:
                if pfam not in pdb_uniprot_pfam_map:
                    pdb_uniprot_pfam_map[pfam] = {}
                if pdb_id not in pdb_uniprot_pfam_map[pfam]:
                    pdb_uniprot_pfam_map[pfam][pdb_id] = set()
                pdb_uniprot_pfam_map[pfam][pdb_id].update(uniprot_codes)

    # Step 2: Loop through all FASTA files in the input folder
    for fasta_file in os.listdir(fasta_folder):
        if fasta_file.endswith(".fasta"):
            fasta_path = os.path.join(fasta_folder, fasta_file)
            fasta_pfam_code = fasta_file.split(".")[0]

            if fasta_pfam_code not in pdb_uniprot_pfam_map:
                print(f"No matches found for Pfam code: {fasta_pfam_code}")
                continue

            # Extract UniProt codes and associated PDB IDs
            pdb_to_uniprot = pdb_uniprot_pfam_map[fasta_pfam_code]
            all_uniprot_codes = set(code for codes in pdb_to_uniprot.values() for code in codes)

            print(f"Processing Pfam code: {fasta_pfam_code}")
            print(f"Total UniProt codes to match: {len(all_uniprot_codes)}")

            # Match sequences in the FASTA file
            matched_sequences = []
            matched_pdb_ids = set()
            with open(fasta_path, 'r', encoding = 'ascii') as fastafile:
                for record in SeqIO.parse(fastafile, 'fasta'):
                    matching_pdb_ids = [
                        pdb_id for pdb_id, codes in pdb_to_uniprot.items()
                        if any(code in record.id for code in codes)
                    ]
                    if matching_pdb_ids:
                        matched_sequences.append(record)
                        matched_pdb_ids.update(matching_pdb_ids)

            print(f"Number of matched sequences: {len(matched_sequences)}")
            print(f"Matched PDB IDs: {matched_pdb_ids}")

            # Prepare output file paths
            output_fasta = os.path.join(output_folder, f"{fasta_pfam_code}_matched_sequences.fasta")
            output_pdb_file = os.path.join(output_folder, f"{fasta_pfam_code}_matched_pdb_ids.txt")

            # Write matched sequences to the FASTA file
            if matched_sequences:
                with open(output_fasta, 'w') as output_file:
                    SeqIO.write(matched_sequences, output_file, 'fasta')
                print(f"Matched sequences saved to: {output_fasta}")
            else:
                print(f"No sequences matched for Pfam code: {fasta_pfam_code}. Skipping FASTA output.")

            # Write matched PDB IDs to the text file
            if matched_pdb_ids:
                with open(output_pdb_file, 'w') as pdb_file:
                    pdb_file.write("\n".join(matched_pdb_ids))
                print(f"Matched PDB IDs saved to: {output_pdb_file}")
            else:
                print(f"No PDB IDs matched for Pfam code: {fasta_pfam_code}. Skipping PDB output.")


# Example usage
csv_file = "/home/abi/Desktop/merged_file.csv"                  # Path to the CSV file
fasta_folder = "/mnt/usb-Seagate_Basic_NABSSV5R-0:0-part1/Tesis_Maestria/Processed Data/pfam_downloads/alignments_nodupl_mejorado/fasta/"  # Path to the folder containing FASTA files
output_folder = "/mnt/usb-Seagate_Basic_NABSSV5R-0:0-part1/Tesis_Maestria/Processed Data/pfam_downloads/alignments_nodupl_mejorado/fasta/output_results_mascantidad"        # Path to the folder for saving outputs

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

filter_fasta_by_uniprot_and_track_pdb(csv_file, fasta_folder, output_folder)


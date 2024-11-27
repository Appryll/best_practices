from function import transcribe_dna_to_rna
import os

def transcribe_dna_to_rna(dna_sequence):
    return dna_sequence.upper().replace('T', 'U')

# Example usage
dna_sequence = "AGCTATAG"
rna_sequence = transcribe_dna_to_rna(dna_sequence)
print(f"RNA Sequence: {rna_sequence}")
def gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    sequence=sequence.upper()
    g_count=sequence.count('G')
    c_count=sequence.count( 
                           'C'
                           )
    gc_content=(g_count + c_count) / len(sequence) * 100
    return gc_content

# Example usage
sequence = "         AGCTATAG              "
print(f"GC Content: {gc_content(sequence):.2f}%")
def reverse_complement(my_sec):
    
    
    """Generate the reverse complement of a DNA sequence."""
    complement = {  'A':'T',  'T': 'A',  'C': 'G',  'G': 'C'  }
    reversed_sequence = my_sec.upper()[ ::-1 ]
    reverse_complement_sequence = ''.join([complement[base] for base in reversed_sequence])
    return reverse_complement_sequence

# Example usage
my_sec = "AGCTATAG"
print(f"Reverse Complement: {reverse_complement(my_sec)}")
def find_restriction_sites(sequence, enzymes):
    
    
    """
                    Find restriction sites in a DNA sequence for given restriction enzymes.
                    
                    Parameters:
                    sequence : DNA sequence of the plasmid
                    enzymes : Dictionary of enzyme names and their recognition sequences
                    
                    Returns:
                    sites : Dictionary of enzyme names and their cut positions
    """
    
    
    sites = {}
    for enzyme, recognition_site in enzymes.items():
        cut_positions = [i for i in range(len(sequence)) if sequence.startswith(recognition_site, i)]
        if cut_positions:
            sites[enzyme] = cut_positions
    return sites

SEQUENCE = "AGCTGATCGATCGATCGATCGTAGCTAGCTGATCGATCAGCTGATCGATCGATCGATCGTAGCTAGCTGATCGATCAGCTGATCGATCGATCGATCGTAGCTAGCTGATCGATCAGCTGATCGATCGATCGATCGTAGCTAGCTGATCGATC" # Example usage
Enzymes = {"EcoRI":"GAATTC","BamHI":"GGATCC","HindIII":"AAGCTT"}

z = find_restriction_sites(SEQUENCE, Enzymes)
print("Restriction Sites:", z)


import pandas as pd
from dotenv import load_dotenv
load_dotenv()

def read_and_process_csv(input_csv_path, output_csv_path):
    """
    Reads a CSV file, processes the data, and writes the processed data to another CSV file.
    
    Parameters: input_csv_path (str): Path to the input CSV file. / output_csv_path (str): Path to the output CSV file.
    """
    
    # Étape 1 : Lire le fichier CSV
    d = pd.read_csv(input_csv_path)
    
    d['RNA Sequence'] = d['DNA Sequence'].apply(transcribe_dna_to_rna)
    
    # Étape 2 : traiter les données
    
    d [  '  GC Content  '  ] =d [ 'DNA Sequence' ].apply(gc_content)
    d [  '  Reverse Complement  '  ]= d [  'DNA Sequence'  ].apply(reverse_complement)
    
    # Étape 3 : Écrivez les données traitées dans un nouveau fichier CSV
    d.to_csv(output_csv_path, index=True)


inputcsvpath ='1.csv'# Example usage
_output_csv_path = '2.csv'# Example usage
message = os.getenv("MESSAGE")

try:
    read_and_process_csv(inputcsvpath, _output_csv_path)
    print(f"{message}{_output_csv_path}.")
except Exception as e:
    print(f"An error occurred: {e}")

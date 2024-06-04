






## Transcribe a DNA sequence into an RNA sequence.
def transcribe_dna_to_rna(sequence):
    return sequence.upper().replace('T'  ,   'U')

# Example usage
sequence = "ATGCGTACAGTATCGATAACATGACTGCTACGATCGGATACGGGTAACGCCATGTACATTATGCGTACAGTATCGATAACATGACTGCTACGATCGGATACGGGTAACGCCATGTACATT"
rna_sequence = transcribe_dna_to_rna(sequence)
print(f"RNA Sequence: {rna_sequence}")

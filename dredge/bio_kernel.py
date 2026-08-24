import numpy as np

class UniversalBioKernel:
    """
    Core engine handling DNA, RNA, Protein Translation, and Biophysical Indices.
    """
    CODON_TABLE = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

    HYDROPHOBICITY = {
        'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
        'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
        'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
        'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
    }

    @staticmethod
    def transcribe(dna_seq: str) -> str:
        """DNA -> mRNA"""
        return dna_seq.upper().replace('T', 'U')

    @staticmethod
    def reverse_complement(dna_seq: str) -> str:
        """Computes 3'-5' reverse complement."""
        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
        return "".join(comp.get(base, 'N') for base in reversed(dna_seq.upper()))

    @staticmethod
    def translate(dna_seq: str) -> str:
        """DNA -> Protein Amino Acid Chain"""
        seq = dna_seq.upper()
        protein = []
        for i in range(0, len(seq) - 2, 3):
            codon = seq[i:i+3]
            aa = UniversalBioKernel.CODON_TABLE.get(codon, 'X')
            if aa == '*':
                break
            protein.append(aa)
        return "".join(protein)

    @staticmethod
    def calculate_gc_content(dna_seq: str) -> float:
        """Calculates genomic GC-ratio stability."""
        seq = dna_seq.upper()
        gc = seq.count('G') + seq.count('C')
        return round((gc / len(seq)) * 100.0, 2) if seq else 0.0

    @staticmethod
    def mean_hydrophobicity(protein_seq: str) -> float:
        """Kyte-Doolittle Hydrophobicity Index."""
        scores = [UniversalBioKernel.HYDROPHOBICITY.get(aa, 0.0) for aa in protein_seq]
        return round(float(np.mean(scores)), 3) if scores else 0.0

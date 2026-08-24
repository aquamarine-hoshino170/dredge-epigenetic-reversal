import numpy as np

class UniversalBioKernel:
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
        return dna_seq.upper().replace('T', 'U')

    @staticmethod
    def reverse_complement(dna_seq: str) -> str:
        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
        return "".join(comp.get(base, 'N') for base in reversed(dna_seq.upper()))

    @staticmethod
    def translate(dna_seq: str) -> str:
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
        seq = dna_seq.upper()
        gc = seq.count('G') + seq.count('C')
        return round((gc / len(seq)) * 100.0, 2) if seq else 0.0

    @staticmethod
    def mean_hydrophobicity(protein_seq: str) -> float:
        scores = [UniversalBioKernel.HYDROPHOBICITY.get(aa, 0.0) for aa in protein_seq]
        return round(float(np.mean(scores)), 3) if scores else 0.0

    @staticmethod
    def find_crispr_targets(dna_seq: str, pam: str = "GG") -> list:
        """Scans sequence for SpCas9 20nt protospacer targets adjacent to NGG PAM."""
        seq = dna_seq.upper()
        targets = []
        for i in range(len(seq) - 22):
            # Check 20nt protospacer + 3nt PAM (NGG)
            sub = seq[i:i+23]
            protospacer = sub[:20]
            pam_found = sub[21:23]
            if pam_found == pam:
                gc = UniversalBioKernel.calculate_gc_content(protospacer)
                efficiency_score = round(100.0 - abs(50.0 - gc) * 1.5, 2)
                targets.append({
                    "position": i,
                    "protospacer_20nt": protospacer,
                    "pam": sub[20:],
                    "gc_content": gc,
                    "on_target_score": efficiency_score
                })
        return targets

class SequenceAlignmentEngine:
    """
    Dynamic Programming Engine for Global Sequence Alignment (Needleman-Wunsch).
    """
    @staticmethod
    def align_pairwise(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -2) -> tuple:
        n, m = len(seq1), len(seq2)
        score_matrix = np.zeros((n + 1, m + 1), dtype=int)

        for i in range(n + 1):
            score_matrix[i][0] = i * gap
        for j in range(m + 1):
            score_matrix[0][j] = j * gap

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                diag = score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
                delete = score_matrix[i-1][j] + gap
                insert = score_matrix[i][j-1] + gap
                score_matrix[i][j] = max(diag, delete, insert)

        align1, align2 = [], []
        i, j = n, m
        while i > 0 and j > 0:
            current = score_matrix[i][j]
            diag = score_matrix[i-1][j-1]
            if current == diag + (match if seq1[i-1] == seq2[j-1] else mismatch):
                align1.append(seq1[i-1])
                align2.append(seq2[j-1])
                i -= 1
                j -= 1
            elif current == score_matrix[i-1][j] + gap:
                align1.append(seq1[i-1])
                align2.append('-')
                i -= 1
            else:
                align1.append('-')
                align2.append(seq2[j-1])
                j -= 1

        while i > 0:
            align1.append(seq1[i-1])
            align2.append('-')
            i -= 1
        while j > 0:
            align1.append('-')
            align2.append(seq2[j-1])
            j -= 1

        aligned_seq1 = "".join(reversed(align1))
        aligned_seq2 = "".join(reversed(align2))
        return aligned_seq1, aligned_seq2, int(score_matrix[n][m])

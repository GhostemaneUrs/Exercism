def to_rna(dna_strand):
    return dna_strand.translate("".maketrans("CGTA", "GCAU"))

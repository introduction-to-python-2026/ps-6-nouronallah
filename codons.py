def create_codon_dict(file_path):
    codon_dict = {}

    file = open(file_path)
    rows = file.readlines()

    for row in rows:
        parts = row.strip().split('\t')
        codon = parts[0]
        amino_acid = parts[1]
        codon_dict[codon] = amino_acid

    file.close()
    return codon_dict



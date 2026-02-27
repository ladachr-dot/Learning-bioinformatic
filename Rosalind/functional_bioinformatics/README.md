### 🧬 Functional Bioinformatics (`functional_bioinformatics`)

> This section is dedicated to the relationship between genotype and phenotype. It features implemented translation pipelines and database automation.

#### 📋 Solved Tasks:

1. **PROT (Translating RNA into Protein)**
   * **Core:** Translating RNA code into a protein amino acid sequence. Logic: Processing codons in groups of 3 nucleotides, accounting for start and stop signals.

2. **MPRT (Finding a Protein Motif)**
   * **Core:** A mini-pipeline for automated motif searching. The script accesses the UniProt server, parses FASTA files, and utilizes Lookahead regular expressions to find complex protein patterns.

3. **MRNA (Inferring mRNA from Protein)**
   * **Core:** Counting the total number of different RNA strings from which the protein could have been translated.
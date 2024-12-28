Biological data formats are standardized ways of representing and storing biological data, such as DNA sequences, protein structures, and gene expression data. Here are some common biological data formats in bioinformatics:

1. _FASTA format_: A text-based format for representing DNA or protein sequences. Each sequence is preceded by a header line that starts with the ">" symbol.
```
>Sequence_ID
ATCGATCG
```
2. _GenBank format_: A text-based format for representing DNA sequences, annotations, and features. GenBank files contain information about the sequence, such as its accession number, description, and features.
```
LOCUS       SCU49845     405 bp    DNA     linear   HUM 24-JUN-1999
DEFINITION  Homo sapiens mRNA for hemoglobin alpha chain.
ACCESSION   SCU49845
VERSION     SCU49845.1  GI:4550543
DBLINK      BioProject    PRJNA14305
FEATURES             Location/Qualifiers
     gene            1..405
                     /gene="HBA1"
                     /locus_tag="HBA1"
```
3. _PDB format_: A text-based format for representing three-dimensional structures of biological molecules, such as proteins and nucleic acids.
```
ATOM      1  N   SER A   1      -3.883  11.646   1.444  1.00  0.00           N  
ATOM      2  CA  SER A   1      -2.654  11.357   0.744  1.00  0.00           C  
ATOM      3  C   SER A   1      -1.537  10.444   1.193  1.00  0.00           C  
```
4. _GFF format_: A text-based format for representing genomic features, such as genes, exons, and repeats.
```
chr1    gene    1000    2000    .    +    .    ID=gene1;Name=gene1
chr1    exon    1000    1500    .    +    .    ID=exon1;Parent=gene1
chr1    exon    1600    2000    .    +    .    ID=exon2;Parent=gene1
```
5. _BED format_: A text-based format for representing genomic regions, such as genes, exons, and regulatory elements.
```
chr1    1000    2000    gene1    0    +
chr1    1000    1500    exon1    0    +
chr1    1600    2000    exon2    0    +
```
6. _VCF format_: A text-based format for representing genetic variants, such as single nucleotide polymorphisms (SNPs) and insertions/deletions (indels).
```
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
chr1    1000    rs1234  A       G       100     PASS    DP=100;VDB=0.05
chr1    1500    rs5678  C       T       50      PASS    DP=50;VDB=0.1
```
These are just a few examples of the many biological data formats used in bioinformatics. Each format has its own strengths and weaknesses, and the choice of format depends on the specific needs of the research project.

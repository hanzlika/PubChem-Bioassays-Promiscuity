### Bioassay data from PubChem

| Field                 | Description                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------|
| `AID`                 | PubChem BioAssay identifier                                                                           |
| `BioAssay Name`       | BioAssay name provided by depositor                                                                   |
| `Deposit Date`        | Date of deposition                                                                                    |
| `Modify Date`         | Date when it's last modified                                                                          |
| `Source Name`         | Depositor who provided the bioassay record                                                            |
| `Source ID`           | External identifier used by depositor                                                                 |
| `Substance Type`      | Type of tested substance, i.e., small-molecule and nucleotide (RNAi reagent)                          |
| `Outcome Type`        | Activity outcome type, i.e., Screening, Confirmatory, Summary, Literature, and Other                  |
| `Project Category`    | Project category like 'Molecular Libraries Screening Center Network' and others                      |
| `BioAssay Group`      | Bioassays of the same group are closely related records derived from the same publication or project  |
| `BioAssay Types`      | BioAssay types like Biochemical, Cell-based, Organism-based, and Toxicity                             |
| `Protein Accessions`  | NCBI Protein identifiers for the protein targets                                                      |
| `UniProt IDs`         | UniProt identifiers for the protein targets                                                           |
| `Gene IDs`            | NCBI Gene identifiers for the gene targets or the encoding genes of the protein targets               |
| `Target TaxIDs`       | NCBI Taxonomy identifiers for the organism targets                                                    |
| `Taxonomy IDs`        | NCBI Taxonomy identifiers derived from targets and links provided by depositor                        |
| `Number of Tested SIDs` | Number of substances that are tested in a bioassay                                                    |
| `Number of Active SIDs` | Number of substances that are tested active in a bioassay                                             |
| `Number of Tested CIDs` | Number of compounds that are tested in a bioassay                                                     |
| `Number of Active CIDs` | Number of compounds that are tested active in a bioassay                                              |


| Field                 | Description                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `AID`                 | PubChem BioAssay identifier                                                                        |
| `SID`                 | PubChem Substance identifier, the tested substance                                                 |
| `SID Group`           | To differentiate bioactivities because the same SID may be tested multiple times in a single AID   |
| `CID`                 | PubChem Compound identifier corresponding to the tested substance                                  |
| `Activity Outcome`    | i.e., Active, Inactive, Inconclusive, Unspecified, and Probe                                       |
| `Activity Name`       | e.g., IC50, Ki, Kd                                                                                 |
| `Activity Qualifier`  | e.g., <, <=, =, >=, >                                                                              |
| `Activity Value`      | Active concentration value                                                                         |
| `Protein Accession`   | NCBI Protein accession for the protein target                                                      |
| `Gene ID`             | NCBI Gene identifier for the gene target (or the encoding gene of the protein target)              |
| `Target TaxID`        | NCBI Taxonomy identifier for the organism target                                                   |
| `PMID`                | PMID associated with the bioactivity data                                                          |

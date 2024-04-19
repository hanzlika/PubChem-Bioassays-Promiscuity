from rdkit import Chem
import os
from tqdm import tqdm

def extract_and_save_smiles_from_sdf(sdf_path, output_file):
    """
    Extracts SMILES strings and their corresponding compound IDs from an SDF file
    and saves them to a file continuously.
    
    Parameters:
    sdf_path (str): The path to the SDF file.
    output_file (file): An open file object for writing the extracted data.
    """
    suppl = Chem.SDMolSupplier(sdf_path)
    for mol in tqdm(suppl, desc=f"Processing {os.path.basename(sdf_path)}"):
        if mol is not None:
            try:
                compound_id = mol.GetProp("_Name")
                smiles = Chem.MolToSmiles(mol)
                output_file.write(f'{compound_id}\t{smiles}\n')
            except Exception as e:
                # If there's an error during SMILES generation, skip this compound ID.
                continue

def extract_smiles_from_directory_and_save(directory_path, output_path):
    """
    Goes through all SDF files in a directory, extracts a mapping of compound ID to SMILES strings,
    and saves the results continuously to a specified output file.
    
    Parameters:
    directory_path (str): The path to the directory containing SDF files.
    output_path (str): The path to the output file where results will be saved.
    """
    sdf_files = [f for f in os.listdir(directory_path) if f.endswith(".sdf")]
    with open(output_path, 'w') as output_file:
        for filename in tqdm(sdf_files, desc="Total progress"):
            sdf_path = os.path.join(directory_path, filename)
            extract_and_save_smiles_from_sdf(sdf_path, output_file)

# Example usage
directory_path = 'pubchem_compounds/sdfs'
output_path = 'compound_smiles_mapping.txt'
extract_smiles_from_directory_and_save(directory_path, output_path)

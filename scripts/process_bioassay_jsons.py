import pandas as pd
import json
import glob
from tqdm import tqdm
import numpy as np

# Change this to whatever your ROOT is
from file_loading import get_path

def process_json_data(json_data):
    description = json_data['PC_AssaySubmit']['assay']['descr']
    aid = description['aid']['id']
    
    targets = description.get('target')
    target_accession = ""
    if targets:
        if 'protein_accession' in targets[0]['mol_id'].keys():
            target_accession += targets[0]['mol_id']['protein_accession']
    if target_accession == "":
        target_accession = None
    assay_data = json_data['PC_AssaySubmit']['data']
    data_dict = {
        'sid' : [],
        'outcome': [],
        'aid' : [],
        'target' : []
    }
    for entry in assay_data:
        data_dict['sid'].append(entry['sid'])
        data_dict['outcome'].append(entry['outcome'])

    data_dict['aid'] = [aid] * len(data_dict['sid'])
    data_dict['target'] = [target_accession] * len(data_dict['sid'])
    
        
    return pd.DataFrame(data_dict)


if __name__ == '__main__':
    dataframes = []
    
    # Load paths.json to get the base path
    base_path = get_path("pubchem_bioassay_jsons")
    
    json_files = glob.glob(f'{base_path}/*.json')
    
    for file_path in tqdm(json_files, "Processing json files"):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:  # Default encoding
                json_data = json.load(file)
        except UnicodeDecodeError:
            # If a UnicodeDecodeError is encountered, try reading with 'ISO-8859-1' encoding
            with open(file_path, 'r', encoding='ISO-8859-1') as file:
                json_data = json.load(file)
        dataframes.append(process_json_data(json_data))

    print("Merging Dataframes...")
    full_df = pd.concat(dataframes)

    ### OUTCOMES:
    #  1 - Inactive
    #  2 - Active
    #  3 - Inconclusive
    #
    # For our purposes, we only want to know whether the substance has been active or not
    print("Filtering unwanted bioassay outcomes...")
    full_df = full_df[full_df['outcome'].isin([1,2,3])]
    print("Binarizing outcomes into Active/Inactive...")
    full_df['active'] = np.where(full_df['outcome'] == 2, True, False)

    print("Saving...")
    full_df.to_csv(get_path("pubchem_bioassay_csv"), index = False)
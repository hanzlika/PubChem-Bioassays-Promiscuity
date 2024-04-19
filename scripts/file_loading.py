from tqdm import tqdm
import json
import os

def txt_to_dict(filepath, separator=' ', key_col_num=0, val_col_num=1,  max_vals=100_000_000_000):
    """
    Converts a text file with separated columns into a dictionary.
    
    Parameters:
    filepath (str): Path to the input file.
    separator (str): The character used to separate columns in the file.
    key_col_num (int): The column number (0-indexed) to use as dictionary keys.
    val_col_num (int): The column number (0-indexed) to use as dictionary values.
    max_vals (int): The maximum amount of lines loaded into the dict
    
    Returns:
    dict: A dictionary with keys and values extracted from the specified columns.
    """
    result_dict = {}
    with open(filepath, 'r') as file:
        for line in tqdm(file, desc=f"Reading lines from {filepath}"):
            if max_vals <= 0:
                break
            columns = line.strip().split(separator)
            if len(columns) > max(key_col_num, val_col_num):
                key = columns[key_col_num]
                value = columns[val_col_num]
                result_dict[key] = value
            max_vals -= 1
    return result_dict

def get_path(path_key):
    os.chdir('/home/jovyan/')
    with open('paths.json', 'r') as paths_file:
        paths = json.load(paths_file)
        base_path = paths[path_key]
        return base_path
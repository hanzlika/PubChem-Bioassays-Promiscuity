import os
import gzip
import urllib.request
from pathlib import Path
from setuptools import setup, find_packages, Command

class PrepareDataCommand(Command):
    """Custom command to download, unzip, and modify required data files before installation."""
    description = "Download, prepare, and modify required data files"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Organizing files into categories
        data_categories = {
            "Data Preparation Files": {
                "paths": {
                    Path("data/downloaded/pubchem/bioactivities.tsv"): "https://ftp.ncbi.nlm.nih.gov/pubchem/Bioassay/Extras/bioactivities.tsv.gz",
                    Path("data/downloaded/pubchem/bioassays.tsv"): "https://ftp.ncbi.nlm.nih.gov/pubchem/Bioassay/Extras/bioassays.tsv.gz",
                    Path("data/downloaded/panther_protein_families.tsv") : "https://owncloud.cesnet.cz/index.php/s/0KTfriUdNEVz9cn/download",
                    Path("data/downloaded/PAD_target_families.csv") : "https://owncloud.cesnet.cz/index.php/s/Og6RF3yS8C8RyDK/download"
                },
                "size": "~17GB",
                "description": "Data preparation files are only necessary if you want to reproduce the compile_pubchem_data.ipynb notebook."
            },
            "Data Analysis Files": {
                "paths": {
                    Path("data/created/panther_families_table.csv"): "https://owncloud.cesnet.cz/index.php/s/DPG8zQ6R06gTuF6/download",
                    Path("data/created/pubchem_bioactivities_merged.csv"): "https://owncloud.cesnet.cz/index.php/s/6fJlFEyqRmOXWn3/download",
                    Path("data/created/target_families_table.csv"): "https://owncloud.cesnet.cz/index.php/s/A9LxbJKLxRikbi7/download"
                },
                "size": "~2GB",
                "description": "These files are necessary to reproduce the promiscuity analysis."
            }
        }

        # Process each category
        for category_name, category_details in data_categories.items():
            missing_files = [path for path, url in category_details["paths"].items() if not path.exists()]
            if missing_files:
                print(f"\n{category_name} ({category_details['size']}):")
                for missing_path in missing_files:
                    print(f"  Missing: {missing_path}")
                print(f"{category_details['description']}\n")

                user_input = input("Do you want to download the missing files? (yes/no): ")
                if user_input.lower() == 'yes':
                    for file_path in missing_files:
                        self.download_and_unzip(category_details["paths"][file_path], file_path)
                        if file_path.name == "bioactivities.tsv":
                            self.modify_bioactivities(file_path)

    def download_and_unzip(self, url, file_path):
        """Download a gzipped file from a URL and unzip it."""
        compressed_path = file_path.with_suffix('.gz')
        print(f"\nDownloading {url}...")
        urllib.request.urlretrieve(url, compressed_path)
        print("Download completed.")

        print(f"Unzipping {compressed_path}...")
        with gzip.open(compressed_path, 'rb') as f_in:
            with open(file_path, 'wb') as f_out:
                f_out.write(f_in.read())
        print(f"Unzipping completed. File saved to {file_path}")

        # Remove the compressed file after extraction
        os.remove(compressed_path)
        print("Temporary download file removed.")

    def modify_bioactivities(self, file_path):
        """Modify the bioactivities.tsv to only include its first, fourth, and fifth columns."""
        new_file_path = Path("data/created/bioactivities_c1_4_5.tsv")
        print(f"Modifying {file_path} to extract specific columns...")
        with open(file_path, 'r') as original_file:
            with open(new_file_path, 'w') as modified_file:
                for line in original_file:
                    columns = line.split('\t')
                    # Extract the first, fourth, and fifth columns (indexing from 0)
                    selected_columns = [columns[0], columns[3], columns[4]]
                    modified_file.write('\t'.join(selected_columns) + '\n')
        print(f"File modified and saved as {new_file_path}")

setup(
    name='PCBP',
    version='0.1',
    packages=find_packages(),
    cmdclass={
        'prepare_data': PrepareDataCommand
    },
)

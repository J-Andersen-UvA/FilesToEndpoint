import IOPathAndEndpoint as io
import fileSender as fs
import yaml
import os
from tqdm import tqdm

# Load the configuration file
params = None
with open('scripts/config.yaml', 'r') as file:
    params = yaml.safe_load(file)

# Prompt the user for the folders and endpoints
folders_and_endpoints = io.FolderAndEndpointPrompt()
folders_and_endpoints.web_endpoint_fbx = params['default_fbx_endpoint']
folders_and_endpoints.web_endpoint_csv = params['default_csv_endpoint']
folders_and_endpoints.run()

# Define the FBX and CSV folders
fbx_folder = folders_and_endpoints.output_fbx_folder
csv_folder = folders_and_endpoints.output_csv_folder

# Get a list of all .fbx and .csv files in the specified folders
fbx_files = [file for file in os.listdir(fbx_folder) if file.endswith(".fbx") or file.endswith(".FBX")]
csv_files = [file for file in os.listdir(csv_folder) if file.endswith(".csv") or file.endswith(".CSV")]

# Send FBX files to the FBX endpoint
print("Sending FBX files...")
for fbx_file in tqdm(fbx_files, desc="Uploading FBX Files", unit="file"):
    file_path = os.path.join(fbx_folder, fbx_file)
    fs.send_file_to_url(file_path, os.path.splitext(fbx_file)[0], folders_and_endpoints.web_endpoint_fbx)

# Send CSV files to the CSV endpoint
print("Sending CSV files...")
for csv_file in tqdm(csv_files, desc="Uploading CSV Files", unit="file"):
    file_path = os.path.join(csv_folder, csv_file)
    fs.send_file_to_url(file_path, os.path.splitext(csv_file)[0], folders_and_endpoints.web_endpoint_csv)

print("All files have been processed.")

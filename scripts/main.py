import IOPathAndEndpoint as io
import ShogunPost as sp
import yaml
import subprocess
import time
import psutil

# Load the configuration file
params = None
with open('scripts/config.yaml', 'r') as file:
    params = yaml.safe_load(file)

# Prompt the user for the folders and endpoints
# folders_and_endpoints = io.FolderAndEndpointPrompt()
# folders_and_endpoints.web_endpoint_fbx = params['default_fbx_endpoint']
# folders_and_endpoints.web_endpoint_csv = params['default_csv_endpoint']
# folders_and_endpoints.run()



# Path to the Shogun Post executable
shogun_path = r"C:\Program Files\Vicon\ShogunPost1.12\ShogunPost.exe"

# Arguments for launching Shogun Post
args = [shogun_path, "--SkipSplash"]

# Launch Shogun Post and wait for it to open fully
def is_shogun_running():
    """Check if Shogun Post is already running."""
    for process in psutil.process_iter(['name', 'exe']):
        try:
            if process.info['name'] == "ShogunPost.exe" or process.info['exe'] == shogun_path:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

try:
    if is_shogun_running():
        print("Shogun Post is already running. Skipping launch.")
    else:
        print("Launching Shogun Post...")
        process = subprocess.Popen(args)
        time.sleep(5)  # Give it time to initialize
        if process.poll() is None:
            print("Shogun Post has been opened successfully.")
        else:
            print("Failed to start Shogun Post.")
except Exception as e:
    print(f"An error occurred: {e}")

# Connect to Shogun Post
sp_com = sp.ViconShogunPost(params['shogun_post_address'], params['shogun_post_port'])

# Automated Motion Capture Post-Processing with Shogun Post

## Overview

This project automates the post-processing of motion capture data recorded using **Vicon Shogun Live**. After recording sessions, the raw `.mcp` files are processed using **Shogun Post**. The script performs the following tasks:

1. **Converts `.mcp` files to `.fbx` format**.
2. **Extracts marker data and saves it as a `.csv` file**.
3. **Uploads the generated `.fbx` and `.csv` files to a specified web endpoint**.

This setup allows you to run the script after a session and leave it unattended, simplifying the workflow and saving time.

## Prerequisites

1. **Vicon Shogun Live** and **Vicon Shogun Post** installed.
2. Python environment with the `requests` library installed and `Vicon API`
3. A configured web endpoint URL to receive the uploaded files.

## Usage
Execute the Python script after your session, go through the prompts selecting the correct folders.
The Python script then scans the input folder directory for .mcp files, launches Shogun Post and runs with a pipeline script in order to convert the .mcp files. After conversion the files are uploaded to the specified web endpoint (set in the config.yaml) using HTTP POST requests.

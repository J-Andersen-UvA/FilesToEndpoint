# Automated Motion Capture File Uploader with Optional Shogun Post Batch Integration

## Overview

This project streamlines the post-processing of motion capture data, focusing on uploading `.fbx` and `.csv` files to specified web endpoints. Although the core functionality is now focused on file uploads, the repository still retains the necessary setup and scripts for users who want to integrate it with Vicon Shogun Post for automated batch processing.

The script performs the following tasks:

1. Uploads `.fbx` files from the selected folder to the specified FBX endpoint.
2. Uploads `.csv` files from the selected folder to the specified CSV endpoint.
3. Optional: Users can still utilize the provided pipeline for batch processing .mcp files in Shogun Post before uploading.

## Prerequisites

1. (Optional) **Vicon Shogun Live** and **Vicon Shogun Post** installed.
2. Python environment with the `requests` library installed
3. A configured web endpoint URL to receive the uploaded files.

## Usage
Execute the Python script after `.mcp` conversion with Shogun Post batching panel (keeping in mind that we provide a pipeline), go through the prompts selecting the correct folders.
The Python script then scans the input folder directory for `.fbx` and `.csv` files. These are uploaded to the specified web endpoint (set in the config.yaml) using HTTP POST requests.

import os
import tkinter as tk
from tkinter import filedialog, simpledialog

class UserPrompt:
    """
    UserPrompt class provides methods to prompt the user for directory selection and string input using Tkinter dialogs.

    Methods
    -------
    prompt_directory(title)
        Prompts the user to select a directory and returns the selected directory path.
    prompt_string(title, prompt)
        Prompts the user to enter a string and returns the entered string.
    """
    def __init__(self):
        pass

    def prompt_directory(self, title):
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        return filedialog.askdirectory(title=title)

    def prompt_string(self, title, prompt):
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        return simpledialog.askstring(title, prompt)


class FolderAndEndpointPrompt(UserPrompt):
    """
    FolderAndEndpointPrompt class to prompt the user for input and output folder paths and a web endpoint.

    Attributes
    -------
        input_folder (str): The path to the input folder.
        output_fbx_folder (str): The path to the output folder for FBX files.
        output_csv_folder (str): The path to the output folder for CSV files.
        web_endpoint (str): The web endpoint URL.
    Methods
    -------
        prompt_folders(): Prompts the user to select input and output folders.
        confirm_web_endpoint(): Prompts the user to confirm or change the web endpoint.
        run(): Executes the folder and web endpoint prompts.
    """
    def __init__(self):
        super().__init__()
        self.input_folder = ""
        self.output_fbx_folder = ""
        self.output_csv_folder = ""
        self.web_endpoint_fbx = ""
        self.web_endpoint_csv = ""

    def prompt_folders(self):
        self.input_folder = self.prompt_directory("Select Input Folder")
        if not self.input_folder:
            raise ValueError("Input folder is required.")

        self.output_fbx_folder = self.prompt_directory("Select Output Folder for FBX")
        if not self.output_fbx_folder:
            raise ValueError("Output FBX folder is required.")

        self.output_csv_folder = self.prompt_directory("Select Output Folder for CSV")
        if not self.output_csv_folder:
            raise ValueError("Output CSV folder is required.")

    def confirm_web_endpoints(self):
        current_endpoint_fbx = self.prompt_string("Web Endpoint for FBX", f"Current web endpoint for FBX is {self.web_endpoint_fbx}. Enter new endpoint or leave blank to keep current:")
        if current_endpoint_fbx:
            self.web_endpoint_fbx = current_endpoint_fbx

        current_endpoint_csv = self.prompt_string("Web Endpoint for CSV", f"Current web endpoint for CSV is {self.web_endpoint_csv}. Enter new endpoint or leave blank to keep current:")
        if current_endpoint_csv:
            self.web_endpoint_csv = current_endpoint_csv

    def run(self):
        self.prompt_folders()
        self.confirm_web_endpoints()


# example usage
# folder_and_endpoint_prompt = FolderAndEndpointPrompt()
# folder_and_endpoint_prompt.run()
# print(f"Input Folder: {folder_and_endpoint_prompt.input_folder}")
# print(f"Output FBX Folder: {folder_and_endpoint_prompt.output_fbx_folder}")
# print(f"Output CSV Folder: {folder_and_endpoint_prompt.output_csv_folder}")
# print(f"Web Endpoint: {folder_and_endpoint_prompt.web_endpoint_fbx}")

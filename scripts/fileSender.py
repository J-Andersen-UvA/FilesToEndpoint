import json
import requests
import os

def send_file_to_url(file_path, name, upload_url, extra_msgs=[("avatarName", "ViconAvatar")]):
    """
    Synchronously send a file to a specified URL and send a confirmation message via WebSocket.

    Parameters:
    - file_path (str): Path to the file to send.
    - name (str): Name to be included in the WebSocket message.
    - upload_url (str): URL to which the file will be uploaded.
    - extra_msgs (list): Additional key-value pairs to include in the WebSocket message.

    Prints the response from the server after sending the file.
    """
    print(f"Sending file '{os.path.basename(file_path)}' to {upload_url}...")
    try:
        with open(file_path, "rb") as file:
            # Prepare the files dictionary
            files = {"file": (os.path.basename(file_path), file, "application/octet-stream")}
            
            # Add json message to the post request
            json_msg = {"glosName": name}
            for key, value in extra_msgs:
                json_msg[key] = value

            # Send the file via HTTP POST
            response = requests.post(upload_url, files=files, json=json_msg, verify=False)

            # Check if the request was successful
            if response.status_code == 200:
                print(f"File uploaded successfully: {response.text}")
            else:
                print(f"Failed to upload file. Status code: {response.status_code}, Response: {response.text}")

            return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


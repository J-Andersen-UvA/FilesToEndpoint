import sys
import yaml

# Load the configuration file
params = None
with open('scripts/config.yaml', 'r') as file:
    params = yaml.safe_load(file)

sys.path.append(params['shogun_post_sdk_path'])

try:
    import ViconShogunPostSDK
except ImportError as e:
    print(f"ImportError: {str(e)}")
    sys.exit(1)

# Define the class for connecting to Shogun Post
class ViconShogunPost(object):
    def __init__(self, address="localhost", port=805):
        self._Client = ViconShogunPostSDK.Client3.TheClient
        self.Connect(address, port)

    def __del__(self):
        if self._Client.IsConnected():
            self._Client.Disconnect()

    def Connect(self, address, port=805):
        if self._Client.IsConnected():
            self._Client.Disconnect()

        result = self._Client.Connect(address, port)
        if result.Error():  # This line might not be needed if Connect returns a boolean or similar
            raise ConnectionError("Failed to connect to Shogun Post.")

        if not self._Client.IsConnected():
            raise ConnectionError("Unable to connect to ShogunPost application.")

    def processRecording(self, input_file_path, output_fbx_folder, output_csv_folder):
        """
        Processes a recording file in Shogun Post, exporting both CSV and FBX files.
        
        Args:
            input_file_path (str): The path to the input .mcp file.
            output_fbx_folder (str): The folder where the FBX file should be exported.
            output_csv_folder (str): The folder where the CSV file should be exported.
        """
        # Construct the HSL script
        hsl_script = f"""
        // Load the recording file
        loadFile "{input_file_path}";
        
        // Remove Wand markers (optional based on your use case)
        RemoveWand;
        
        // Select all markers
        SelectAllMarkers;
        
        // Export selected markers to CSV
        string $FileNameAppendage = "_MarkerData";
        string $SelectedCharacterOnly = "false";
        string $CSVPath = "{output_csv_folder}/";
        ExportCSV_SelectedMarkers $FileNameAppendage $SelectedCharacterOnly $CSVPath;
        
        // Select the fbx character
        selectByType SolvingBone;
        select "Solving";
        SelectParent_Add_All;
        SelectChildren_Add_All;

        // Export to FBX
        string $frameRateType = "custom";
        int $frameRate = 100;
        setFrameRate $frameRateType $frameRate;
        string $Path = "{output_fbx_folder}/";
        string $fileNameExtension = `GetPathToExportTo` + ".mcp";
        string $fileName = `getFileTitle $fileNameExtension`;
        string $savePath;
        $savePath = $Path + $fileName + ".fbx";
        saveFile $savePath -s;

        // Close the file
        newFile -promptToSave;
        """

        # Execute the HSL script
        return self._Client.HSL(hsl_script)

    # def setPAL100(self):
    #     hsl = """setFrameRate "pal" 100.000000;"""
    #     return self._Client.HSL(hsl)

    # def selectAllMarkers(self):
    #     hsl = """selectByName "ARIEL" "LFHD" "LBHD" "RFHD" "RBHD" "C7" "T10" "CLAV" "STRN" "LFSH" "LBSH" "LUPA" "LELB" "LIEL" "LFRM" "LIWR" "LOWR" "LIHAND" "LOHAND" "RFSH" "RBSH" "RUPA" "RELB" "RIEL" "RFRM" "RIWR" "ROWR" "RIHAND" "ROHAND" "LFWT" "MFWT" "RFWT" "LBWT" "MBWT" "RBWT" "LTHI" "LKNE" "LKNI" "LSHN" "LANK" "LHEL" "LMT5" "LMT1" "LTOE" "RTHI" "RKNE" "RKNI" "RSHN" "RANK" "RHEL" "RMT5" "RMT1" "RTOE";"""
    #     return self._Client.HSL(hsl)

# # Example usage, setting pal
# shogun_post = ViconShogunPost()
# shogun_post.setPAL100()

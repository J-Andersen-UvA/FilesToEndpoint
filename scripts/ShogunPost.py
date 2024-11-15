import sys
sys.path.append(r"C:\Program Files\Vicon\ShogunPost1.12\SDK\Win64")

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
    
    # def setPAL100(self):
    #     hsl = """setFrameRate "pal" 100.000000;"""
    #     return self._Client.HSL(hsl)

    # def selectAllMarkers(self):
    #     hsl = """selectByName "ARIEL" "LFHD" "LBHD" "RFHD" "RBHD" "C7" "T10" "CLAV" "STRN" "LFSH" "LBSH" "LUPA" "LELB" "LIEL" "LFRM" "LIWR" "LOWR" "LIHAND" "LOHAND" "RFSH" "RBSH" "RUPA" "RELB" "RIEL" "RFRM" "RIWR" "ROWR" "RIHAND" "ROHAND" "LFWT" "MFWT" "RFWT" "LBWT" "MBWT" "RBWT" "LTHI" "LKNE" "LKNI" "LSHN" "LANK" "LHEL" "LMT5" "LMT1" "LTOE" "RTHI" "RKNE" "RKNI" "RSHN" "RANK" "RHEL" "RMT5" "RMT1" "RTOE";"""
    #     return self._Client.HSL(hsl)

# # Example usage, setting pal
# shogun_post = ViconShogunPost()
# shogun_post.setPAL100()

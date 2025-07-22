from cx_Freeze import setup, Executable
import os

# Include the directory containing the XML files
include_files = [("haarcascade_frontalface_alt2.xml", "."),
                 ("blur.png",".")] 
# if the xml files are in haarcascades folder. if the files are in the same folder, use [("*.xml",".")]

setup(
    name="PatternsDetection",
    version="1.0",
    description="Pattern detection using OpenCV",
    options={"build_exe": {"include_files": include_files}},
    executables=[Executable("webcam_pattern_detection.py", icon="blur.png")],
)
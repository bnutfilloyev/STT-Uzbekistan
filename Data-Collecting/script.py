import pandas as pd
import glob, os

COMMON_VOICE_PATH = "common-voice-tsv"

# list of all the files in the common voice data folder
files = os.chdir(COMMON_VOICE_PATH)

for file in glob.glob("*.txt"):
    files.append(file)

print(files)
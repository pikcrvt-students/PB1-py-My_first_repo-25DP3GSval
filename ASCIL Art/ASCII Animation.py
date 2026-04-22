import time
import os

frames = [
    "|",
    "i|",
    "in|",
    "ini|",
    "init|",
    "initu|",
    "initul|",
    "inituli|",
    "inituliz|",
    "initulizi|",
    "initulizin|",
    "initulizing|",
    "initulizing.|",
    "initulizing..|",
    "initulizing...|",
    "initulizing...",
    "initulizing..|",
    "initulizing.|",
    "initulizing|",
    "initulizin|",
    "initulizi|",
    "inituliz|",
    "inituli|",
    "initul|",
    "initu|",
    "init|",
    "ini|",
    "in|",
    "i|",
    "|",
    "",
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        time.sleep(0.08)
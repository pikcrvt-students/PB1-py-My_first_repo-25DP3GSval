import time
import os

frames = [
"""R  
 O 
   T""",
""" R 
 O 
  T """,
"""  R
 O 
T""",
"""   
TOR
    """,
"""T  
 O 
   R""",
""" T 
 O 
  R """,
"""  T
 O 
R""",
"""   
ROT
    """,
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        time.sleep(0.3)
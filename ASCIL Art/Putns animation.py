import time
import os

frames = ["""
          
  _____<>
>-\\//_/
  //""",
"""
  \\\\
  _\\\\__<>
>-\\___/
  """
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        time.sleep(0.5)
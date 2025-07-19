import sys
import pandas as pd

print(sys.argv)

day = sys.argv[1]

print(f"Pandas version: {pd.__version__}")
print(f"Job finished for day {day}")
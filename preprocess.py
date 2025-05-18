import os
import pandas as pd

# read data
df = pd.read_csv(os.path.join("enhanced_student_habits_performance_dataset.csv"))

print(df.head())

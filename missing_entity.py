import pandas as pd
import numpy as np
import os

# File paths
base_dir = r'C:\Users\Rudransh\Desktop\crypto data'
input_file = os.path.join(base_dir, 'cleaned.csv')
output_file = os.path.join(base_dir, 'uniform_cleaned.csv')

# Load dataset
df = pd.read_csv(input_file)

# Critical fields to preserve
critical_fields = ['txhash', 'block']

# 1. Handle 'Age' if it exists
if 'Age' in df.columns:
    def parse_age(age_str):
        try:
            parts = str(age_str).split()
            total_seconds = 0
            for i in range(0, len(parts), 2):
                num = int(parts[i])
                unit = parts[i+1].lower()
                if 'day' in unit:
                    total_seconds += num * 86400
                elif 'hour' in unit:
                    total_seconds += num * 3600
                elif 'min' in unit:
                    total_seconds += num * 60
                elif 'sec' in unit:
                    total_seconds += num
            return total_seconds
        except:
            return np.nan

    df['Age_seconds'] = df['Age'].apply(parse_age)
    df.drop(columns=['Age'], inplace=True)
    df['Age_seconds'] = df['Age_seconds'].fillna(df['Age_seconds'].median())

# Recompute non-critical fields after drop
non_critical_fields = [col for col in df.columns if col not in critical_fields]

# 2. Numeric imputation
numeric_cols = df[non_critical_fields].select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# 3. Categorical imputation
categorical_cols = df[non_critical_fields].select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna('Unknown')

# Save the cleaned file
df.to_csv(output_file, index=False, encoding='utf-8')
print("Cleaned file saved to:", output_file)

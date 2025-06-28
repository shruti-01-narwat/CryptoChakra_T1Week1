import pandas as pd
import os

# File paths
base_dir = r'C:\Users\Rudransh\Desktop\crypto data'
input_file = os.path.join(base_dir, 'transactions_with_labels.csv')
output_file = os.path.join(base_dir, 'cleaned.csv')

# Load CSV
df = pd.read_csv(input_file)

# Drop unnecessary columns
columns_to_drop = ['From', 'To'] + [col for col in df.columns if col.startswith('Unnamed')]
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Save cleaned data
df.to_csv(output_file, index=False, encoding='utf-8')
print("Cleaned file saved to:", output_file)

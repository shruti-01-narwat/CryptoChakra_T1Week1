import pandas as pd
import os

# File paths
base_dir = r'C:\Users\Rudransh\Desktop\crypto data'
tx_file = os.path.join(base_dir, 'Eth_Txs.xlsx')
addr_file = os.path.join(base_dir, 'addresses.xlsx')
output_file = os.path.join(base_dir, 'transactions_with_labels.csv')

# Load transaction data
df_tx = pd.read_excel(tx_file)

# Drop "Unnamed: 0" if it exists
if 'Unnamed: 0' in df_tx.columns:
    df_tx.drop(columns=['Unnamed: 0'], inplace=True)

try:
    df_addr = pd.read_excel(addr_file)
except FileNotFoundError:
    print("⚠️ Address file not found. Creating synthetic address labels...")
    # Create synthetic labels with same number of rows
    categories = ['EXCHANGE', 'GAMBLING', 'MARKETPLACE', 'MIXER', 'DEFI', 'WALLET']
    df_addr = pd.DataFrame({
        'entity': [f'Entity_{i}' for i in range(len(df_tx))],
        'address': [f'0xSyntheticAddress{i:05d}' for i in range(len(df_tx))],
        'category': [categories[i % len(categories)] for i in range(len(df_tx))],
        'source': ['Synthetic'] * len(df_tx)
    })
    df_addr.to_excel(addr_file, index=False)
    print(f"Synthetic address labels saved to: {addr_file}")

# Trim to same length
min_len = min(len(df_tx), len(df_addr))
df_tx = df_tx.iloc[:min_len].reset_index(drop=True)
df_addr = df_addr.iloc[:min_len].reset_index(drop=True)

# Drop the 'address' column to avoid duplication
if 'address' in df_addr.columns:
    df_addr.drop(columns=['address'], inplace=True)

# Merge side-by-side (1-to-1 synthetic labeling)
df_merged = pd.concat([df_tx, df_addr], axis=1)

# Save merged file
if os.path.exists(output_file):
    os.remove(output_file)

df_merged.to_csv(output_file, index=False, encoding='utf-8')
print("Row-wise merged data saved to:", output_file)

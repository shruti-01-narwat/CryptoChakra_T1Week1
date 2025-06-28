
# 🧠 CryptoChakra — Week 1 (Data Preparation & Cleaning)

🔗 Repository: [CryptoChakra\_T1Week1](https://github.com/shruti-01-narwat/CryptoChakra_T1Week1)
📁 Data Folder (Google Drive):
➡️ [https://drive.google.com/drive/folders/1nCpGDS8c5c2RjGjv9toWDDDIkgWbM1pr?usp=drive\_link](https://drive.google.com/drive/folders/1nCpGDS8c5c2RjGjv9toWDDDIkgWbM1pr?usp=drive_link)



## Overview

This repository contains the first-week implementation of the CryptoChakra project, focused on cryptocurrency transaction data wrangling, cleaning, and preparation. The goal is to preprocess Ethereum transaction-like data with labeled addresses and clean it for downstream analytics/modeling tasks such as wallet/entity classification.



## 📦 Contents

Due to GitHub file limits, only scripts are committed here. All raw and generated data files are stored in the linked Google Drive folder above.

### Data Sources

* `Eth_Txs.xlsx` — Simulated Ethereum transaction data (txhash, block, timestamp, value, From, To, memo, etc.)
* `addresses.xlsx` — Manually created/synthetic labeled addresses with entity type and address hash.
* `transactions_with_labels.csv` — Merged file from the above two.
* `cleaned.csv` — Output of `data_cleaner.py` after removing unnecessary columns.
* `uniform_cleaned.csv` — Final dataset with missing values handled, ready for modeling.

### Rationale for Synthetic Dataset

🧪 Note: There is a scarcity of openly available Ethereum transaction datasets that contain "memo"/"input" fields or labeled address categories. Therefore, a synthetic labeled address file (`addresses.xlsx`) was generated and merged row-wise (1:1) with transaction records to simulate a realistic labeled dataset.



## 📂 Folder Structure

```
crypto data/
├── addresses.xlsx                 
├── Eth_Txs.xlsx                   
├── transactions_with_labels.csv   
├── cleaned.csv                    
├── uniform_cleaned.csv           
├── data_cleaner.py               
├── data_merger.py                
├── missing_entity.py             
```

---

## ⚙️ Code Description

### `data_merger.py`

* Merges `Eth_Txs.xlsx` and `addresses.xlsx` row-wise (1-to-1 pairing).
* If `addresses.xlsx` is missing, generates synthetic address labels.
* Output: `transactions_with_labels.csv`

### `data_cleaner.py`

* Drops redundant columns: `From`, `To`, and any column starting with `Unnamed`.
* Output: `cleaned.csv`

### `missing_entity.py`

* Handles missing values:

  * Parses `Age` column into seconds (`Age_seconds`)
  * Fills numeric columns using median imputation
  * Fills categorical columns with `"Unknown"`
* Preserves critical fields (`txhash`, `block`)
* Output: `uniform_cleaned.csv`



## ✅ How to Run

Make sure you have Python 3.10+ and required libraries:

```bash
pip install pandas numpy scikit-learn
```

Run scripts in order:

```bash
python data_merger.py
python data_cleaner.py
python missing_entity.py
```



## 📌 Notes & Design Decisions

* Synthetic address label file created due to unavailability of labeled datasets.
* Row-wise merging for simplicity and prototype speed.
* No change to critical fields (`txhash`, `block`).
* Lightweight and structured for quick experimentation.



## 📂 File Access

All large data files stored in Google Drive:
➡️ [https://drive.google.com/drive/folders/1nCpGDS8c5c2RjGjv9toWDDDIkgWbM1pr?usp=drive\_link](https://drive.google.com/drive/folders/1nCpGDS8c5c2RjGjv9toWDDDIkgWbM1pr?usp=drive_link)

Download and place them in a folder named `crypto data` in the root.



## 👩‍💻 Author

Shruti Narwat
GitHub: [shruti-01-narwat](https://github.com/shruti-01-narwat)



## 🔒 License

This project is for academic and prototype use only.

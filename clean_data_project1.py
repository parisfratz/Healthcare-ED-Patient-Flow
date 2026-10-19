import pandas as pd

# 1. Φόρτωση δεδομένων
df = pd.read_csv("ed_patient_data.csv")

"""
#Το df.shape σου δίνει το μέγεθος του πίνακα (γραμμές, στήλες), οπότε το shape[0] απομονώνει καθαρά τον αριθμό των γραμμών.
print("----DATASET------")
print(f"Συνολικές γραμμές: {df.shape[0]}, Columns: {df.shape[1]}")

#df.columns: Παίρνει όλες τις επικεφαλίδες (τα ονόματα των στηλών) από το DataFrame σου. Από μόνο του, επιστρέφει ένα αντικείμενο τύπου Index.
#.tolist(): Μετατρέπει αυτό το Index σε μια κλασική λίστα Python (List).
print("Dataset Columns:")
print(df.columns.tolist())

#Το df.head(3) σου επιστρέφει τις πρώτες 3 γραμμές σαν μια γρήγορη «προεπισκόπηση» για να τσεκάρεις ότι τα δεδομένα φόρτωσαν σωστά.
print("\n--FIRST LINES---")
print(df.head(3))
"""

print("--- 1. ΕΛΕΓΧΟΣ ΓΙΑ ΚΕΝΑ & ΔΙΠΛΟΤΥΠΑ ---")
print("Κενές τιμές (Missing values) ανά στήλη:")

print(df.isnull().sum())

duplicates = df.duplicated().sum()
print(f"Duplicated Records: {duplicates}")

# 2. Καθαρισμός (Data Cleaning)
# Αφαιρούμε τυχόν διπλότυπα
if duplicates > 0:
    df = df.drop_duplicates()
else:
    print("No duplicates in dataset!")

# Καθαρίζουμε τα κείμενα από τυχόν περιττά κενά (whitespace)
for col in df.select_dtypes(include=['object', 'str']).columns:
    df[col] = df[col].astype(str).str.strip()

print(f"\nΣυνολικές γραμμές μετά τον καθαρισμό: {len(df)}")

# 3. Εξαγωγή του καθαρού αρχείου για το Power BI
df.to_csv('cleaned_clinical_data.csv', index=False)
print
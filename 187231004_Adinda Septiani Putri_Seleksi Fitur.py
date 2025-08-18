import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy.stats import chi2_contingency

Data = pd.read_excel("Heart_Disease_Prediction.xlsx")
df = pd.DataFrame(Data)

#Menampilkan Data Awal
print("Data Awal")
print (df)

df.info()

# Membuat LabelEncoder
le = LabelEncoder()

# Mengganti kolom "Heart Disease" dengan hasil encoding
df['Heart Disease'] = le.fit_transform(df['Heart Disease'])

# Menampilkan hasil
print(df)

# Menyimpan hasil ke dalam DataFrame
chi_square_results = []

# Melakukan uji chi-square
# Heart_Disease_Prediction
#contingency_table = pd.crosstab(df['Chest pain type'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['BP'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['Cholesterol'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['FBS over 120'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['EKG results'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['Age'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['Max HR'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['Exercise angina'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['ST depression'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['Slope of ST'], df['Heart Disease'])
#contingency_table = pd.crosstab(df['Number of vessels fluro'], df['Heart Disease'])
contingency_table = pd.crosstab(df['Thallium'], df['Heart Disease'])
print("Tabel Kontingensi:\n", contingency_table)

# Melakukan uji chi-square
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Menampilkan hasil
print(f"Chi-Square Value: {chi2}")
print(f"P-Value: {p}")

# Menentukan apakah ada hubungan signifikan
alpha = 0.05
if p < alpha:
    print("Terdapat hubungan signifikan antara Thallium dan Heart Disease")
else:
    print("Tidak terdapat hubungan signifikan antara Thallium dan Heart Disease")

# Konversi hasil ke DataFrame
df_results = pd.DataFrame(chi_square_results, columns=["Thallium", "Chi-Square Value", "P-Value"])

# Simpan hasil ke file CSV
df_results.to_csv("Heart Disease_Chisquare.csv", index=False)

print("\n Hasil seleksi fitur telah disimpan dalam 'Heart Disease_Chisquare.csv'")
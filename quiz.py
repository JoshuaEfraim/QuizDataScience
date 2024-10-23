import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("healthcare.csv") 
missing_values = df.isna().sum()
columns_with_missing = missing_values[missing_values > 0]
print(columns_with_missing)

df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])
df["Duration of Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
print(df)

patients80 = df[df["Age"] >= 80]
meanduration= patients80["Duration of Stay"].mean()
print(meanduration)

print(df["Medical Condition"].min())

arthritis = df[df["Medical Condition"] == "Arthritis"]
olderarthritis = arthritis[arthritis["Age"] >= 80]["Billing Amount"].mean()
youngerarthritis = arthritis[arthritis["Age"] <= 20]["Billing Amount"].mean()
print(f"older average: {olderarthritis}")
print(f"young average: {youngerarthritis}")

highestbilling = df[df["Billing Amount"] == df["Billing Amount"].max()]
mostdays = highestbilling["Duration of Stay"].values[0]
print(mostdays)

rows_missing = df.isna().any(axis=1).sum()
print(rows_missing)

df["Name"] = df["Name"].str.lower()


clean_df = df.dropna()
remaining_records = clean_df.shape[0]
print(remaining_records)

condition_counts = clean_df["Medical Condition"].value_counts()
print(condition_counts)

patients15male = df[df["Age"] <= 15 & df["Gender"] == "Male"]
patients15female = df[df["Age"] <= 15 & df["Gender"] == "Female"]
x1=patients15male["Room Number"]
y1=patients15male["Billing Amount"]
x2= patients15female["Room Number"]
y2=patients15female["Billing Amount"]
plt.scatter(x1, y1, c ="r",linewidths = 2, marker ="D", edgecolor ="b", s = 70, alpha=0.5)
plt.scatter(x2, y2, c ="k",linewidths = 2,marker ="p",edgecolor ="red",s = 150,alpha=0.5)

plt.title('Multiple Scatter plot')
plt.xlabel('Room Number')
plt.ylabel('Billing Amount')

plt.show()

diabetes_patients = clean_df[clean_df["Medical Condition"] == "Diabetes"]
sns.boxplot(data=diabetes_patients, x="Blood Type", y="Age")
plt.title("Patient with Diabetes")
plt.xlabel("Blood Type")
plt.ylabel("Age")
plt.show()
import pandas as pd
raw_csv_data = pd.read_csv("C:/Users/Mko/Desktop/Udemy/SQL Python tableau/Absenteeism_data.csv")
print(raw_csv_data)
df = raw_csv_data.copy()
print(df)
pd.options.display.max_columns = None
pd.options.display.max_rows = 12
df = df.drop(["ID"], axis=1)
df['Reason for Absence'].max()
df['Reason for Absence'].unique()
reason_columns =pd.get_dummies(df['Reason for Absence'])
reason_columns
reason_columns['check'] = reason_columns.sum(axis=1)
reason_columns
reason_columns['check'].sum(axis=0)
reason_columns['check'].unique
reason_columns = reason_columns.drop(['check'],axis=1)
reason_columns =pd.get_dummies(df['Reason for Absence'], drop_first =True)
reason_columns
df.columns.values
reason_columns.columns.values
df = df.drop(['Reason for Absence'], axis=1)
df
reason_columns.loc[:,1:14]

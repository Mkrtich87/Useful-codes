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
reason_type_1=reason_columns.loc[:,1:14].max(axis=1)
reason_type_2=reason_columns.loc[:,15:17].max(axis=1)
reason_type_3=reason_columns.loc[:,18:21].max(axis=1)
reason_type_4=reason_columns.loc[:,22:].max(axis=1)
reason_type_1
df = pd.concat([df,reason_type_1,reason_type_2,reason_type_3,reason_type_4], axis = 1)
df
df.columns.values
column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1','Reason_2', 'Reason_3', 'Reason_4']
      
df.columns=column_names
df.head()
column_names_reordered = ['Reason_1','Reason_2', 'Reason_3', 'Reason_4', 'Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']
df=df[column_names_reordered] 
df(head)
df_reason_mod=df.copy()
df_reason_mod
df_reason_mod['Date']

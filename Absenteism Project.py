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
df.head()
df_reason_mod=df.copy()
df_reason_mod
df_reason_mod['Date']
type(df_reason_mod["Date"])
type(df_reason_mod["Date"][0])
df_reason_mod["Date"] = pd.to_datetime(df_reason_mod["Date"])
df_reason_mod["Date"]
pd.set_option("max_rows", None)
df_reason_mod["Date"]
df_reason_mod
print("Default max_rows: {} and min_rows: {}".format(
pd.get_option("max_rows"), pd.get_option("min_rows")))
pd.set_option("max_rows", 20)
df_reason_mod
df_reason_mod = df.copy()
df_reason_mod
df_reason_mod["Date"] = pd.to_datetime(df_reason_mod["Date"], format = '%d/%m/%Y')
df_reason_mod["Date"]
df_reason_mod.info()
df_reason_mod["Date"][0].month
df_reason_mod.shape
list_months = []
list_months
for i in range (df_reason_mod.shape[0]):
    list_months.append(df_reason_mod["Date"][i].month)
list_months
len(list_months)
df_reason_mod["Month Value"] = list_months
df_reason_mod
df_reason_mod['Date'][699].weekday()
df_reason_mod['Date'][699]
def date_to_weekday(date_value):
    return date_value.weekday()
df_reason_mod['Day of the Week'] = df_reason_mod['Date'].apply(date_to_weekday)
df_reason_mod.head()
df_reason_mod = df_reason_mod.drop(["Date"], axis=1)
df_reason_mod.columns.values
column_names_upd = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Month Value', 'Day of the Week',
       'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education', 'Children',
       'Pets', 'Absenteeism Time in Hours']
df_reason_mod = df_reason_mod[column_names_upd]
df_reason_mod.head()
df_reason_date_mod = df_reason_mod.copy()
df_reason_date_mod
type(df_reason_date_mod['Daily Work Load Average'][0])
df_reason_date_mod["Education"].unique()
df_reason_date_mod["Education"] = df_reason_date_mod["Education"].map({1:0,2:1,3:1,4:1})
df_reason_date_mod["Education"].unique()




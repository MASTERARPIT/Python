import pandas as pd

file_path ='data.csv'
data=pd.read_csv(file_path)
filterdata = data[data['ever_married'] == 'No']
filterdata = data[data['avg_glucose_level'] >30]

print(filterdata)
sortdata=filterdata.sort_values(by='avg_glucose_level')
print(sortdata)


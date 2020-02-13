import pandas as pd 
import re

terms_list = pd.read_csv('terms_list.csv', dtype=str)
query_data = pd.read_csv('query_data.csv')
query_data.astype
output = terms_list

#reindex might be unnecessary due to "for column in colmn_list" statement possibly 
#creating new column in ouput file automatically but my knowledge is limited
output.reindex(columns=[
	'Impressions',
	'Clicks',
	'Cost',
	'Conversions',
	'Conv. value',
	])

output.fillna(0)
clmn_list = query_data.columns.tolist()
clmn_list.pop(0)
print(query_data.dtypes)
#iterates through each check term in the terms_list, adds data from KPI rows for 
#search term if check term is in search term as individual word
for x in terms_list.iloc[:,0]:
	for y in query_data['Search term']:
		if re.search(fr'\b{{x}}\b', y):
			for column in clmn_list:
				current_value = output.at(x, column) 
				current_value += query_data.at(y, column)
				x = 0
				x+=1
				print(x)

output['ROAS'] = output['Conv. value']/output['Cost']
output['Avg. CPC'] = output['Cost']/output['Clicks']
output['AOV'] = output['Conv. value']/output['Conversions']

output.to_csv('output.csv')




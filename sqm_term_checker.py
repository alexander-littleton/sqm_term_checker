import pandas as pd 
import re

terms_list = pd.read_csv('terms_list.csv', dtype='object')
query_data = pd.read_csv('query_data.csv')
output = terms_list

#reindex might be unnecessary due to "for column in colmn_list" statement possibly 
#creating new column in ouput file automatically but my knowledge is limited
output['Impressions']=0.0
output['Clicks']=0.0
output['Cost']=0.0
output['Conversions']=0.0
output['Conv. value']=0.0

clmn_list = query_data.columns.tolist()
clmn_list.pop(0)

#iterates through each check term in the terms_list, adds data from KPI rows for 
#search term if check term is in search term as individual word
xint=0
for x in terms_list.iloc[:,0]:
	print(x)
	yint=0
	for y in query_data['Search term']:
		if re.search(r'\b'+x.lower()+r'\b', y.lower()):
			for column in clmn_list:
				current_value = float(output.at[xint, column])
				current_value += float(query_data.at[yint, column])
				output.at[xint, column] = (current_value)
		yint+=1
	xint+=1

output['ROAS'] = output['Conv. value']/output['Cost']
output['Avg. CPC'] = output['Cost']/output['Clicks']
output['AOV'] = output['Conv. value']/output['Conversions']

output.to_csv('output.csv')




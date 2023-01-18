import pandas as pd
tn = 'impianti_sportivi.csv'
arco = 'CSV/ArcoComuneScraped.csv'
tn_scrape = 'CSV/TrentoComuneScraped.csv'
pg = 'CSV/PagineGialleScraped.csv'

df = pd.read_csv('impianti_sportivi.csv', sep=';')

wAddress = 3
wName = 40
wMun = 1

def importDF(name, sep = ','):
    df = pd.read_csv(name, sep = sep)
    return df


# A Naive recursive Python program to find minimum number
# operations to convert str1 to str2


def editDistance(str1, str2, m = 0, n = 0):
	# Create a table to store results of subproblems
	m = len(str1)
	n = len(str2)
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	# Fill d[][] in bottom up manner
	for i in range(m + 1):
		for j in range(n + 1):

		# If first string is empty, only option is to
		# insert all characters of second string
			if i == 0:
				dp[i][j] = j # Min. operations = j

	# If second string is empty, only option is to
	# remove all characters of second string
			elif j == 0:
				dp[i][j] = i # Min. operations = i

	# If last characters are same, ignore last char
	# and recur for remaining string
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]

# If last character are different, consider all
# possibilities and find minimum
			else:
				dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
				dp[i-1][j],	 # Remove
				dp[i-1][j-1]) # Replace
	return dp[m][n]
# This code is contributed by Bhavya Jain


# This code is contributed by Bhavya Jain

def checkSim(df1, df2):
	sim = []
	current = []
	id2 = []
	countId = 100
	for k in range(len(df2)):
		id2.append(countId)
		countId+=1
	for i in range(len(df1)):
		str1 = df1.iloc[i]['Address'] + " " + df1.iloc[i]['Municipality'] + " " + df1.iloc[i]['Name']
		
		add1 = df1.iloc[i]['Address']
		name1 = df1.iloc[i]['Name']
		mun1 = df1.iloc[i]['Municipality']
		
		for j in range(len(df2)):			
			str2 = df2.iloc[j]['Address'] + " " + df2.iloc[j]['Municipality'] + " " + df2.iloc[j]['Name']
			add2 = df2.iloc[j]['Address']
			name2 = df2.iloc[j]['Name']
			mun2 = df2.iloc[j]['Municipality']
			distAdd = editDistance(add1, add2) 
			distName = editDistance(name1, name2)
			distMun = editDistance(mun1, mun2)

			dist = distAdd
			
			if distAdd < wAddress:
					print(str1, " ", str2)
					sim.append(dist)

	return sim

tn_df = importDF(tn, ';')
tn_s_df = importDF(tn_scrape)
pg_df = importDF(pg)

k= checkSim(tn_df, pg_df)

print(k)
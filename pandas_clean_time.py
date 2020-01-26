# clean up time data in pandas (Q&A)
# dataset contains opening and closing times of restaurants

import pandas as pd

# added first column as the identifier of the restaurant
data = [
['r1', '11', '30', 'am', '9', 'pm'],
['r2', '11', '30', 'am', '9', '30', 'pm'],
['r3', '11', 'am', '12', '30', 'am'],
['r4', '11', 'am', '10', 'pm']]

# making a dataframe from the list
df = pd.DataFrame(data)
print(df)

# fixing the rows that have messed up data
for index, row in df.iterrows():
    if row[2] in ('am', 'pm'):
        df.iloc[[index],3:7] = df.iloc[[index],2:6].values.tolist()
        df.iloc[[index],[2]] = '00'
    if row[5] in ('am', 'pm'):
        df.iloc[[index],[6]] = df.iloc[[index],[5]].values.tolist()
        df.iloc[[index],[5]] = '00'

# renaming columns - begin and end time
df.columns = ['entity', 'b_hour', 'b_min', 'b_ampm', 'e_hour', 'e_min', 'e_ampm']
print(df)

# combining the time columns into a single value
df['open'] = df['b_hour'] + ':' + df['b_min'] + " " + df['b_ampm']
df['close'] = df['e_hour'] + ':' + df['e_min'] + " " + df['e_ampm']

# showing the final result only
print(df.loc[:, ['entity', 'open', 'close']])

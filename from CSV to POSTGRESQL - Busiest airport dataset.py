import pandas as pd

 # Create or load your dataset into a Pandas DataFrame
 data = pd.read_csv(r"C:\Users\Admin\Desktop\Databases for practice\List of busiest airports by passenger traffic 2018 a.csv")

# view the top 5 rows OF THE DATAFRAME IN PANDAS
data.head()

# viewing information such as number of null values, summary, counts etc. of all columns
data.info()

# VIEWING ONLY THE NUMBER OF MISSING VALUES FOR EACH COLUMN
data.isnull().sum()

# VIEWING ALL MISSING VALUES OF A PARTICULAR COLUMN
# this one will extract top 5 empty values under the Tax revenue column

# data[data['Tax revenue (%)'].isnull()].head()

# THIS ONE WILL FILL ALL THE BLANK SPACES OF A COLUMN WITH EITHER A NUMBER OR TEXT OR WITH 'UNKNOWN'.
# data['Tax revenue (%)'].fillna('0', inplace=True)
# data.head()
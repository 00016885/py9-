import pandas as pd
import matplotlib.pyplot as plt
import argparse
import seaborn as sns
df = sns.load_dataset('iris')
# print(df['species'].value_counts())
parser = argparse.ArgumentParser(description='Sample CLI using argparse')
parser.add_argument("name", help="Your name")
args = parser.parse_args()
# print(df[args.name].value_counts())
print(f'Hello, This we have, {args.name} equals=',df[args.name].value_counts())
#
# # reading the dataset
#
# # Load the data
# df = pd.read_csv('data.csv')  # download it from WIUT intranet
# # print first 5 rows of the dataframe
# print(df.head())
# # exploring data
# print(df.shape)
# print(df.dtypes)
# print(df['Health_Camp_ID'].value_counts())
# # Check for missing values
# print(df.isnull().sum())
# # Remove duplicates
# df = df.drop_duplicates()
# # Fill missing values with a specific value (e.g., 0)
# df = df.fillna(0)
#
# # Calculate descriptive statistics
# print(df.describe())
# # Create a visualization (e.g., a bar plot)
# # df['column_name'].value_counts().plot(kind='bar')
# df['Var1'].value_counts().plot(kind='bar')  # example
# plt.show()
#
#
# # User interface
# parser = argparse.ArgumentParser(description='Sample CLI using argparse')
# parser.add_argument("name", help="Your name")
# parser.add_argument("age", help="Your age", type=int)
# args = parser.parse_args()
# print(f"Hello, {args.name}. You are {args.age} years old.")

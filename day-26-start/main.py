import pandas

data = pandas.read_csv("data.cvs")
dict_data = {row.country:row.capital for (index, row) in data.iterrows()}

print(dict_data)
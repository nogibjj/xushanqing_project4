import sqlite3
import pandas as pd
conn = sqlite3.connect("food.db")
cursor = conn.cursor()

'''
## create new table for top_50_fast_food_US.csv
table = 'CREATE TABLE company (company TEXT,category TEXT,sales_in_millions_2019 INTEGER,sales_per_unit_thousands_2019 INTEGER,franchised_units_2019 INTEGER,company_owned_units_2019 INTEGER,total_units_2019 INTEGER,unit_change_from_2018 INTEGER)'
cursor = conn.cursor()
cursor.execute(table)
conn.commit()
print('Table created successfully')
# # load the data into a Pandas DataFrame
companys = pd.read_csv('top_50_fast_food_US.csv')
# write the data to a sqlite table
companys.to_sql('company', conn, if_exists='append', index = False)
'''

# fetch all rows from cars table
cursor.execute('''SELECT * FROM company''').fetchall()

# Select first 5 record from the table
def first_five():
    query_select = 'SELECT * FROM company LIMIT 5'
    for i in cursor.execute(query_select):
        print(i)

def top_three_companies():
#query 1: select top 3 selling_price fast food companies
    query1 =  """SELECT company,category,sales_in_millions_2019
            FROM company
            Order by sales_in_millions_2019 DESC
            LIMIT 3;"""
    top_price = cursor.execute(query1).fetchall()
    print("\n Top 3 sell price fast food companies:")
    for company in top_price:
        print(company)


#query 2: select top 3 closed units change from 2018 companies
def top_three_close_unit_companies():
    query2 =  """SELECT company,category,unit_change_from_2018
            FROM company
            Order by unit_change_from_2018 ASC
            LIMIT 3;"""
    top_close = cursor.execute(query2).fetchall()
    print("\n Top 3 closed units change from 2018 companies:")
    for company in top_close:
        print(company)


#query 3: select top 3 sells burger
def top_seller(category):
    s = """SELECT company,category,sales_in_millions_2019
            FROM company Where category='{category}'
            Order by sales_in_millions_2019 DESC
            LIMIT 3;"""

    query3 =  s.format(category = category)
    top_company = cursor.execute(query3).fetchall()
    res = " Top 3 sells {category} :".format(category = category)
    for company in top_company:
        res += "{company},".format(company = company)
    return res








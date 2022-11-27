category = "burger"
s = """SELECT company,category,sales_in_millions_2019
        FROM company Where category='{category}'
        Order by sales_in_millions_2019 DESC
        LIMIT 3;"""

query3 =  s.format(category = category)
print(query3)
top_burger = ["KFC","Mcdouls"]
res = " Top 3 sells {category} :".format(category = category)
for company in top_burger:
    res += "{company},".format(company = company)
print(res)
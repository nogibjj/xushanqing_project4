from fastapi import FastAPI
import uvicorn
from test_sql import top_seller, top_three_companies, first_five

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, welcome to the top 50 fast food in US dataset, lets's begin to using sql to query fast food chain company in US! category: burger, snack,chicken,sandwich,pizza,global"}

@app.get("/{category}")
async def query(category):
    """select top 3 sellers in this category (burger)"""
    print(category)
    result = top_seller(category)
    string = "Latest Result for {} is:  {}".format(category,result)
    return {string}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
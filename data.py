from faker import Faker
import pandas as pd

fake=Faker()

class people():
    birth_date: str
    salary: int
    active_credit_size:int
    co_borrower_size:int 
    co_credit_peoples: int
    poruch: bool
    children_count:int
    children_aliment_count:int 
    marriage:bool
    amount:int
    period: int
    credit_raiting:int

data=[]
for i in range(2000):
    data.append(
    {"birth_date": fake.date(),
    "salary": fake.pyint(min_value=10000,max_value=1000000),
    "active_credit_size":fake.pyint(),
    "co_borrower_size":fake.pyint() ,
    "co_credit_peoples": fake.pyint(),
    "poruch": fake.pybool(),
    "children_count":fake.pyint(max_value=4),
    "children_aliment_count":fake.pyint(max_value=4) ,
    "marriage":fake.pybool(),
    "amount":fake.pyint(min_value=10000,max_value=10000000),
    "period": fake.pyint(max_value=360),
    "credit_raiting":fake.pyint(max_value=2)}
    )


dt=pd.DataFrame(data)

dt.to_csv("test.csv",index=False)
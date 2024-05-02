import streamlit as st
from koefs import min_date,max_date,rasschet,clear_salary
import pandas as pd
from neural_network import date_func, classify
st.title("Выпускная квалификационная работа ")
st.title("Экспертная система оценки кредитоспособности заёмщика")


st.write("Введите данные")


birth_date = st.date_input("Введити дату рождения", min_value=min_date)
salary = st.number_input("Введите среднюю зарплату за 6 месяцев", min_value=0)

active_credit = st.radio("Имеется ли у вас кредит/ипотека?", ["Да", "Нет"], index=1)
if active_credit == "Да":
    active_credit_size = st.number_input("Введите размер платежа")

co_borrower = st.radio("Являетесь ли созаемщиком?", ["Да", "Нет"], index=1)
if co_borrower == "Да":
    co_borrower_size = st.number_input(
        "Введите размер платежа кредита, в котором вы являетесь созаемщиком"
    )
    co_credit_peoples = st.number_input("Введите количество заемщиков",min_value=2,max_value=15)

poruch = st.radio("Являетесь ли поручителем?", ["Да", "Нет"], index=1)


children = st.radio("Имеются ли у вас дети?", ["Да", "Нет"], index=1)
if not children == "Нет":
    children_count = st.number_input("Введите количество детей",min_value=1, max_value=100)

children_aliment = st.radio("Платите ли вы алименты?", ["Да", "Нет"], index=1)
if children_aliment == "Да":
    children_aliment_count = st.number_input(
        "Введите количество детей, за которых вы платите", min_value=1,max_value=100
    )

marriage = st.radio("Находитесь ли вы в браке?", ["Да", "Нет"], index=1)

amount = st.number_input("Введите желаемую сумму кредита", min_value=0)
period = st.number_input("Введите желаемый период", min_value=0, max_value=360)

if st.button(label='Проверить'):
    clear_sal=clear_salary(salary,
             active_credit_size if active_credit=='Да' else 0,
             co_borrower_size/co_credit_peoples if co_borrower=='Да' else 0,
             poruch,
             children_count if children=='Да' else 0,
             children_aliment_count if children_aliment=='Да' else 0,
             marriage)

    dta=pd.DataFrame({"birth_date":date_func(birth_date),
                        "salary":salary,
                        "active_credit_size":active_credit_size if active_credit=='Да' else 0,
                        "co_borrower_size":co_borrower_size if co_borrower=='Да' else 0,
                        "o_credit_peoples":co_credit_peoples  if co_borrower=='Да' else 0,
                        "poruch":True if poruch=="Да" else False,
                        "children_count":children_count if children=='Да' else 0,
                        "children_aliment_count":children_aliment_count if children_aliment=='Да' else 0,
                        "marriage":True if marriage=="Да" else False,
                        "amount":amount,
                        "period":period,
                        }, index=[0])
    
    info  = classify(dta)
   
    rasschet(birth_date,clear_sal, amount, period, info)
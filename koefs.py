
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt

max_date = dt.date.today()
min_date = max_date.replace(year=max_date.year - 80)
max_date = max_date.replace(year=max_date.year - 18)
def get_k(salary: int):
    """
    К – коэффициент, зависящий от величины Дч:
    К = 0,3 при Дч в эквиваленте до
    500 долл.;
    К = 0,4 при Дч в эквиваленте от 501 до
    1 тыс. долл.;
    К = 0,5 при Дч в эквиваленте от 1 001 до
    2 тыс. долл.;
    К = 0,6 при Дч в эквиваленте свыше
    2 000 долл.; ко
    """
    if salary < 50000:
        return 0.3
    elif salary < 100000:
        return 0.4
    elif salary < 200000:
        return 0.5
    else:
        return 0.6


def clear_salary(salary,active_credit_size, co_borrower_size,poruch,children_count,children_aliment_count,marriage):
    """
    input: 
        salary - зарплата
        active_credit_size - размер платежей по кредитам
        co_borrower_size - размер платежей по кредитам, где вы являетесь созаемщиком
        poruch - являетесь ли вы поручителем
        children_count - количество детей
        children_aliment_count - количество детей за которых вы платите алименты
        marriage - находитесь ли вы в браке
    return: 
        clear_salary - зарплата, которая может пойти на кредит
    """
    
    if children_aliment_count== 0:
        children_aliment_k = 1
    elif children_aliment_count== 1:
        children_aliment_k = 0.7
    elif  children_aliment_count == 2:
        children_aliment_k = 0.6
    else:
        children_aliment_k = 0.5
    size = 12000
    children_val = (children_count*size)/2 if marriage == "Да" else children_count*size

    
    return salary *children_aliment_k  - active_credit_size - co_borrower_size - children_val

def solvency(salary: int, amount: int, period: int):
    """
    Рассчет платежеспособности
    """

    return salary * get_k(salary) * period


def credit_size(solvency: float, period: int, persent: int = 15):
    """
    Рассчет максимального размера кредита
    """

    return solvency / (1 + (persent / 100) * (period / 12))


def rasschet(birth_date, salary, amount, period,info):
    if birth_date > max_date:
        st.write("Мы не выдаем кредит, если вам нет 18 лет")
        return
    solvency_size = solvency(salary, amount, period)
    max_credit = credit_size(solvency_size, period, persent=12)
    match amount < max_credit:
        case False:
            st.write("Мы не можем предложить кредит по заданным параметрам")
            st.write(f"Максимальная сумма: {round(max_credit,0)}руб.")
        case True:
            if info<0.7:
                st.write("Вероятность одобрения низкая")
            elif info<1.5:
                st.write("Вероятность одобрения средняя")
            else:
                st.write("Вероятность одобрения высокая")
           



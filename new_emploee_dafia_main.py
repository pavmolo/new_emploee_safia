import streamlit as st
import numpy as np
import pandas as pd

# Функция приложения
def show_predict_page():
    #image = Image.open('https://www.kaizen.com/images/kaizen_logo.png')
    #st.image(image, caption='Kaizen Institute')
    st.markdown('''<a href="http://kaizen-consult.ru/"><img src='https://www.kaizen.com/images/kaizen_logo.png' style="width: 50%; margin-left: 25%; margin-right: 25%; text-align: center;"></a><p>''', unsafe_allow_html=True)
    st.title("Определи свой потенциал")
    val_list = ['Рубль', 'Доллар США']
    val_0 = st.radio("Выберите валюту:", val_list, index=0)
    if val_0 == 'Рубль':
        val = 'млн₽'
    else:
        val = 'тыс$'
    st.subheader('Нам необходима информация, чтобы спрогнозировать ваши показатели прибыли')
    industry = st.radio("Ваша отрасль:", industry_list)
    market_state = st.radio("Охарактеризуйте состояние сектора, в котором вы работаете:", gro_state_list)
    revenue = st.number_input(f"Какова ваша выручка, {val} в год:", value=0)
    margin = st.slider("Какова ваша маржа операционной прибыли, % к выручке:", -20, 80, 0, 2)
    growth = st.slider("Каков ваш среднегодовой рост выручки в % за последние 3 года", -20, 100, 0, 5)
    lost = lost_profit(industry, market_state, revenue, margin, growth)
    lost = pd.Series(lost).round(0)
    st.title("Результат")
    col1, col2, col3 = st.columns(3)
    proc_lost_rev = - (lost[0] / revenue * 100)
    proc_lost_1 = - (lost[1] / revenue * 100)
    proc_lost_2 = - (lost[2] / revenue * 100)
    
    
# Вызываем приложение
show_predict_page()

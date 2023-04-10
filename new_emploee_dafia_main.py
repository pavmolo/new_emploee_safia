import streamlit as st
import numpy as np
import pandas as pd
import pickle5 as pickle
from catboost import CatBoostRegressor

def create_new_dict(sex, age, fam, childrens, ed):
    num_input = []
    num_input.append(age)
    
    if sex == "Мужчина":
        num_input.append(1)
    else:
        num_input.append(0)
        
    num_input.append(childrens)
    
    if fam == "Холост / Не замужем":
        num_input.append(2)
    else:
        num_input.append(1)
        
    if ed == 'Высшее':
        num_input.append(0)
    elif ed == 'Неоконченное высшее':
        num_input.append(1)
    elif ed == 'Среднее':
        num_input.append(3)
    else:
        num_input.append(4)    
    
    return num_input




# Функция приложения
def show_predict_page():
    #image = Image.open('https://www.kaizen.com/images/kaizen_logo.png')
    #st.image(image, caption='Kaizen Institute')
    st.markdown('''<a href="http://kaizen-consult.ru/"><img src='https://www.kaizen.com/images/kaizen_logo.png' style="width: 50%; margin-left: 25%; margin-right: 25%; text-align: center;"></a><p>''', unsafe_allow_html=True)
    st.title("Определи потенциал сотрудника")
    sex_list = ['Мужчина', 'Женщина']
    ed_list = ['Высшее', 'Неоконченное высшее', 'Среднее', 'Среднеспециальное']
    fam_list = ['Холост / Не замужем', 'Женат / Замужем']
    st.subheader('Нам необходима информация, чтобы спрогнозировать срок службы')
    sex = st.radio("Пол:", sex_list)
    age = st.slider("Возраст", 16, 50, 20, 1)
    fam = st.radio("Семейное положение:", fam_list)
    childrens = st.slider("Количество детей", 0, 5, 0, 1)
    ed = st.radio("Образование:", ed_list)
    
    num_input = create_new_dict(sex, age, fam, childrens, ed)

    load_model = pickle.load(open('model.pickle', 'rb'))
    pred = load_model.predict([num_input]) #вставляем итоговый список
    st.title(f"Числовой вход: {num_input}")
    st.title(f"Оценка срока службы: {pred} месяцев")
    
# Вызываем приложение
show_predict_page()

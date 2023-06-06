#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[ ]:


st.title('Welcome to BMI Calculator')

weight = st.number_input("Enter weight (in kgs)")
height = st.number_input("Enter height (in cms)")
try:
    bmi = weight/((height/100)**2)
except:
    st.text("Enter some value of height")
    
if(st.button('Calculate BMI')):
    
    st.text("Your BMI index is {}.".format(bmi))
    
    if(bmi<16):
        st.error("You are EXTREMELY Underweight!")
    elif(bmi>=16 and bmi<18.5):
        st.warning("You are UNDERWEIGHT!")
    elif(bmi>=18.5 and bmi<25):
        st.success("You are Healthy!")
    elif(bmi>=25 and bmi<30):
        st.warning("You are Overweight!")
    elif(bmi>=30):
        st.error("You are EXTREMELY Overweight!")


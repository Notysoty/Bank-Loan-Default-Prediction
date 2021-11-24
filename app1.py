
#%%writefile app1.py
 
import pickle
import streamlit as st
import pandas as pd
import numpy as np
 
# loading the trained model
pickle_in = open('xgboost_model.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(age,ed,employ,address,income,debtinc,creddebt,othdebt):   
  
    # Making predictions 
    prediction = classifier.predict( 
        np.array([[age,ed,employ,address,income,debtinc,creddebt,othdebt]]))
     
    if prediction == 0:
        pred = 'Not Default'
    else:
        pred = 'Default'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Bank Loan Prediction</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    age = st.number_input("Age of the Applicant")
    ed = st.number_input("Education")
    employ = st.number_input("Employment") 
    address = st.number_input("Address of the Applicant")
    income = st.number_input("Gross Income of the Applicant")
    debtinc = st.number_input("Debt to Income Ratio of the Applicant")
    creddebt = st.number_input("Credit to Debt Ratio of the Applicant")
    othdebt = st.number_input("Any other Debts of the Applicant")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(age,ed,employ,address,income,debtinc,creddebt,othdebt) 
        st.success('The applicant might {}'.format(result))
        #print(result)
     
if __name__=='__main__': 
    main()
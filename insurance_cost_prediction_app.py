
import pickle
import streamlit as st

#loading the saved model

prediction_model = pickle.load(open('/content/drive/MyDrive/Medical insurance cost prediction /random_forest_regression_model.pkl', 'rb'))


# Creating the Title
st.title("Medical Insurance Cost Prediction")
st.subheader("Calculating the insurance charges that could be charged by an insurer based on a person's attributes")

# Taking the users input
# columns for input fields

col1, col2 = st.columns(2)

with col1:
  age = st.text_input("Enter Age of the Customer")

with col2: 
  sex = st.selectbox("Select Gender type", ['Male', 'Female'])

with col1:  
  bmi = st.text_input("Enter BMI value eg. 27.8")

with col2:
  children = st.text_input("Enter the Number of children")

with col1:
  smoker = st.selectbox("Is the person smoker?", ['Yes', 'No'])

with col2:
   region = st.selectbox("Enter the Region", ['Southeast' ,'Northwest' ,'Southwest' ,'Northeast'])

# converting text input to numeric to get back predictions from backend model.
if sex == 'Male':
    sex_male = 1
else:
    sex_male= 0
    
if smoker == 'Yes':
    smoker_yes	 = 1
else:
    smoker_yes	= 0
    
if region == 'Southeast':
    region_northwest = 0
    region_southeast = 1
    region_southwest = 0
elif region == 'Northwest':
    region_northwest = 1
    region_southeast = 0
    region_southwest = 0
elif region == 'Southwest':
    region_northwest = 0
    region_southeast = 0
    region_southwest = 1
else:
    region_northwest = 0
    region_southeast = 0
    region_southwest = 0

# Final prediction
if st.button('Predict'):           # when the submit button is pressed
    prediction =  prediction_model.predict([[age, bmi, children, sex_male, smoker_yes, region_northwest, region_southeast, region_southwest]])
    st.balloons()
    st.success(f'The estimated medical insurance charges will be around ${round(prediction[0],2)}')

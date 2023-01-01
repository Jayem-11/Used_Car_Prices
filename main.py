import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from tensorflow.keras.models import load_model
import requests


st.write("""

# Used Car Price Prediction

""")

#=========================================================================================
st.write("""

## Brand

""")

brand = st.text_input('Enter brand',0)

#=========================================================================================
st.write("""

## Model

""")

model = st.text_input('Enter model',0)

#=========================================================================================

st.write("""

# Mileage

""")

mileage = st.slider('Enter Mileage', value=10000, min_value=0, max_value=200000, step=1) 

#===========================================================================================


st.write("""

## Year

""")

year = st.text_input('Enter Year',2020)



#===========================================================================================
st.write("""

## Fuel Type

""")

fuel = st.radio('What fuel type are you looking for ?',['Gas','Electric','Hybrid','Plug-In Hybrid','Diesel','CNG','Hydrogen'],index = 0)
fuel_dict = {'Diesel': 1, 'CNG': 0, 'Electric': 2, 'Gas': 3, 'Hybrid': 4, 'Plug-In Hybrid': 6, 'Hydrogen': 5}
fuel_type = fuel_dict.get(fuel)

#===========================================================================================


#=========================================================================================
st.write("""

## Previous Owners

""")

ownerCount = st.slider('Enter owner count', value=5, min_value=1, max_value=100, step=1) 

ownerCount = float(ownerCount)
#=========================================================================================

#=========================================================================================
st.write("""

## Accidents

""")

accidentCount = st.slider('Enter accident count', value=5, min_value=1, max_value=100, step=1) 


#======================================================================================

st.write("""

## Transmission

""")

trans = st.radio('Select the type of transmission ?',['Manual','Automatic'],index = 0)
trans_dict = {'Manual': 1, 'Automatic': 0}
transmission = trans_dict.get(trans)

#========================================================================================



#===========================================================================================
st.write("""

## State

""")

sta = st.radio(' Select state',['CA','NY','NJ','PA','CT'],index = 0)
state_dict = {'CT': 1, 'CA': 0, 'NJ': 2, 'NY': 3, 'PA': 4}
state = state_dict.get(sta)

#===========================================================================================

#=========================================================================================
st.write("""

## City

""")

city = st.text_input('Enter city',0)

#=============================================================================================


#===========================================================================================
st.write("""

## Body Style

""")

body = st.radio('What body style are you looking for ?',['SUV','Sedan','Pick Up Truck','Hatchback','Coupe','Minivan','Convertible','Cargo Van','Wagon',
'Passenger van','Chassis cab truck'],index = 0)

body_dict = {'Chassis Cab Truck': 1, 'Cargo Van': 0, 'Convertible': 2, 'Coupe': 3, 'Hatchback': 4, 'Passenger Van': 6, 'Minivan': 5,'Pickup Truck': 7,
'SUV': 8,'Sedan': 9, 'Wagon':10}

body_style = body_dict.get(body)

#===========================================================================================


#===========================================================================================
st.write("""

## Drive Train

""")

drive = st.radio(' Select drive Train',['FWD','AWD','4WD','RWD'],index = 0)
drive_dict = {'AWD': 1, '4WD': 0, 'FWD': 2, 'RWD': 3}
drive_train = drive_dict.get(drive)

#===========================================================================================



st.write("""

## Engine

""")

engine = st.selectbox('choose type of engine', ('2.0L Inline-4 Gas Turbocharged', '5.8L V-12 Gas', '3.5L V-6 Gas',
       '3.0L V-6 Gas Turbocharged', '2.5L Inline-4 Gas', '5.0L V-8 Gas',
       '1.8L Inline-4 Gas', '2.4L Inline-4 Gas', '3.7L V-6 Gas',
       '1.5L Inline-4 Gas Turbocharged', '2.5L Flat-4 Gas',
       '4.0L V-8 Gas Turbocharged', '3.6L V-6 Gas',
       '3.0L Inline-6 Gas Turbocharged', '2.5L Inline-5 Gas Turbocharged',
       '5.3L V-8 Gas', '4.6L V-8 Gas', '2.4L Inline-4 Gas Turbocharged',
       '2.5L Inline-4 Hybrid', '1.4L Inline-4 Gas Turbocharged',
       '5.5L V-8 Gas', '3.0L V-6 Gas Supercharged',
       '2.0L Inline-4 Gas Supercharged and Turbocharged', '3.3L V-6 Gas',
       '3.5L V-6 Gas Turbocharged', '2.3L Inline-4 Gas Turbocharged',
       '2.0L Inline-4 Gas', '3.8L Flat-6 Gas', '5.4L V-8 Gas',
       '2.7L V-6 Gas', '4.0L V-6 Gas', '2.0L V-4 Gas Turbocharged',
       '2.5L Inline-5 Gas', '3.0L V-6 Diesel Turbocharged',
       '6.0L W-12 Gas Turbocharged', '6.6L V-12 Gas Turbocharged',
       '2.0L Inline-4 Plug-In Hybrid Supercharged and Turbocharged',
       '1.2L Inline-4 Gas', '3.5L V-6 Hybrid',
       '4.6L V-8 Gas Turbocharged', '4.7L V-8 Gas Turbocharged',
       '2.7L V-6 Gas Turbocharged', '1.8L Inline-4 Hybrid',
       '1.5L Inline-4 Plug-In Hybrid', '4.2L V-8 Gas',
       '2.0L Inline-4 Hybrid', '2.5L Flat-4 Gas Turbocharged',
       '1.6L Inline-4 Gas', '3.7L Inline-5 Gas', '3.2L V-6 Gas',
       '5.2L V-12 Gas Turbocharged', '1.5L Inline-4 Gas',
       '2.3L V-4 Gas Turbocharged', '1.3L Inline-4 Hybrid',
       '2.0L Inline-4 Plug-In Hybrid', '4.7L V-8 Gas',
       '3.6L Flat-6 Gas Turbocharged', '1.8L Inline-4 Gas Turbocharged',
       '2.3L Inline-4 Gas', '2.0L Flat-4 Gas',
       '1.6L Inline-4 Gas Turbocharged', '2.7L Inline-4 Gas',
       '3.0L Flat-6 Gas Turbocharged', '3.2L Inline-6 Gas',
       '3.6L V-6 Gas Turbocharged', '4.8L V-8 Gas',
       '4.4L V-8 Gas Turbocharged', '6.7L V-8 Diesel Turbocharged',
       '2.9L V-6 Plug-In Hybrid Turbocharged', '5.2L V-10 Gas',
       '1.5L Inline-4 Hybrid', '3.0L Inline-6 Gas',
       '2.4L Flat-4 Gas Turbocharged', '3.0L V-6 Gas',
       '3.0L Inline-6 Diesel Turbocharged',
       '2.7L Inline-4 Gas Turbocharged', '3.3L V-6 Hybrid Turbocharged',
       '6.2L V-8 Gas', '5.7L V-8 Gas', '6.4L V-8 Gas',
       '4.8L V-8 Gas Turbocharged', '2.5L V-6 Gas',
       '3.0L Inline-6 Hybrid Turbocharged', '6.0L V-8 Gas',
       '2.5L Inline-4 Gas Turbocharged', '3.0L V-6 Hybrid Turbocharged',
       '3.5L Inline-5 Gas', '4.3L V-6 Gas', '1.2L Inline-3 Gas',
       '6.0L V-8 Diesel', '5.9L V-8 Gas', '5.0L V-8 Gas Supercharged',
       '2.0L Inline-4 Plug-In Hybrid Turbocharged', 'L - Electric',
       '5.6L V-8 Gas', '2.1L Inline-4 Diesel Turbocharged',
       '1.4L Inline-4 Gas', '3.8L V-8 Gas Turbocharged',
       '1.5L Inline-3 Gas Turbocharged', '3.8L V-6 Gas',
       '6.0L V-8 Gas Turbocharged', '4.0L V-8 Gas',
       '2.0L Flat-4 Gas Turbocharged', '6.6L V-8 Diesel Turbocharged',
       '6.8L V-10 Gas', '5.5L V-12 Gas Turbocharged',
       '5.5L V-8 Gas Turbocharged', '2.0L Inline-4 Hybrid Turbocharged',
       '1.3L Rotary- Gas', '1.4L Inline-4 Plug-In Hybrid',
       '3.8L V-6 Gas Supercharged', '5.3L V-8 Hybrid',
       '4.0L V-8 Hybrid Turbocharged', '4.3L V-8 Gas',
       '2.9L V-6 Gas Turbocharged', '5.0L V-8 Gas Turbocharged',
       '5.3L Inline-8 Gas Turbocharged', '2.2L Inline-4 Gas',
       '3.4L Flat-6 Gas', '6.2L V-8 Gas Supercharged', '3.6L Flat-6 Gas',
       '1.6L Inline-4 Hybrid', '2.4L Inline-4 Hybrid',
       '5.0L V-8 Gas Twin-Turbo', '3.5L V-6 Gas Supercharged',
       '1.0L Inline-3 Gas Turbocharged', '6.7L V-6 Diesel Turbocharged',
       '3.8L V-6 Gas Turbocharged', '2.3L Inline-4 Gas Supercharged',
       '3.7L V-6 Gas Turbocharged', '5.4L V-8 CNG',
       '1.3L Inline-4 Gas Turbocharged', '2.7L V-4 Gas Turbocharged',
       '0.6L Inline-2 Plug-In Hybrid', '1.8L Inline-4 CNG',
       '4.0L V-8 Plug-In Hybrid Turbocharged',
       '1.5L Inline-3 Plug-In Hybrid Turbocharged',
       '0.6L Inline-2 Electric', 'L - Hydrogen',
       '1.8L Inline-4 Plug-In Hybrid', '2.7L Flat-6 Gas',
       '6.4L V-8 Diesel Turbocharged', '5.0L V-8 Diesel Turbocharged',
       '6.8L V-8 Gas Turbocharged', '2.0L Inline-4 Diesel Turbocharged',
       '4.1L V-8 Gas', '6.0L V-8 Hybrid', '5.2L V-8 Gas',
       '4.0L Flat-6 Gas', '7.3L V-8 Diesel Turbocharged',
       '1.4L Inline-4 Plug-In Hybrid Turbocharged',
       '2.2L Inline-4 Diesel Turbocharged', '7.0L V-8 Gas',
       '6.1L V-8 Gas', '1.6L Inline-4 Plug-In Hybrid', '6.6L V-8 Gas',
       '1.6L Inline-4 Diesel Turbocharged', '3.3L V-6 Gas Turbocharged',
       '4.8L V-6 Gas Turbocharged',
       '3.0L Inline-6 Hybrid Supercharged and Turbocharged',
       '2.8L Inline-6 Gas', '2.4L V-4 Gas', '1.7L Inline-4 Gas',
       '3.6L V-6 Plug-In Hybrid'))


# encoding the engine name
edf1 = pd.read_csv('engine_encoded')

engine = edf1[edf1['engine'] == engine]['engine_1'].to_list()

engine = engine[0]

# Button
predict_bt = st.button('Predict')
#===========================================================================================    

input_data = np.array([[    
                            # brand, 
                            # model, 
                            mileage,
                            year,
                            fuel_type,
                            ownerCount,
                            accidentCount,
                            transmission,
                            state,
                            body_style, 
                            engine,
                            drive_train,

                        ]])

#=================================================================================================


#=================================================================================================
X = pd.read_csv('x_cleaned')

X.drop('Unnamed: 0', axis = 1,inplace=True)
#Scaling
trans = StandardScaler()

#scaling predictor variable

X = trans.fit_transform(X)
X = pd.DataFrame(X)

#=================================================================================================

inp = pd.DataFrame(input_data)
inp.to_csv('inp')

inp = trans.transform(inp.values)

# loading model

saved_model = load_model("model")




def make_predictions():
    #predict
    result = saved_model.predict(inp)
    return result[0][0]


#Animation function
@st.experimental_memo
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


if predict_bt:

    result = make_predictions()

    if result > 0:
        st.write('# Price:  ', result)
        st.balloons()
    elif result == 0:
        st.error('## Fill in the Details')

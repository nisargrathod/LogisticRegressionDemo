import streamlit as stm
import joblib

stm.set_page_config(page_title = "This is a Multipage WebApp") 
stm.title("Industrial Training For Govt Faculty")

status = stm.radio("Select Gender: ", ('Male', 'Female'))
if (status == 'Male'):
    stm.success("Male")
else:
    stm.success("Female")


Category = stm.selectbox("Categories: ",['Age',])

name = stm.text_input("Enter Your Age", "Type Here ...") 

Category = stm.selectbox("Categories: ",['Fare',])

name = stm.text_input("Enter Ticket Fare", "Type Here ...") 

stm.write("Choose Categories: ", Category)

status = stm.radio("Select Passenger Class: ", ('1st-Upper', '2nd-Middle','3rd-Lower'))
if (status == '1st-Upper'):
    stm.success("1st-Upper")
elif(status == '2nd-Middle'):
    stm.success("2nd-Middle")
else:
    stm.success("3rd-Lower")	

status = stm.radio("Select Passenger Class: ", ('Cherbourg', 'Queenstown','Southampton'))
if (status == 'Cherbourg'):
    stm.success("Cherbourg")
elif(status == 'Queenstown'):
    stm.success("Queenstown")
else:
    stm.success("Southampton")	

if(stm.button('Submit')):
    result = status.title()
    stm.success(result)
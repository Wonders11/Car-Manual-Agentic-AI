import streamlit as st
from langgraph_app.router import route_request

st.title("Car Manual Chatbot")

company = st.text_input("Company")
model = st.text_input("Model")
fuel_type = st.text_input("Fuel Type")
query = st.text_area("Your Query")

if st.button("Ask"):
    response = route_request(company, model, fuel_type, query)
    st.write(response)

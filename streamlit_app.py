import streamlit as st

def calculate_future_value(principal, rate, time):
  future_value = principal * (1 + rate/100) ** time
  return future_value

st.title("Financial Calculator")

principal = st.number_input("Enter Principal Amount: ")
rate = st.number_input("Enter Annual Interest Rate (%): ")
time = st.number_input("Enter Time Period (Years): ")

if st.button("Calculate Future Value"):
  result = calculate_future_value(principal, rate, time)
  st.write(f"Future Value: Rs.{result:.2f}")

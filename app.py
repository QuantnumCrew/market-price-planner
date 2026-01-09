import streamlit as st
from logic.revenue_calculator import calculate_net_revenue

st.title("🌾 Agri Market & Harvest Planner")

price = st.number_input("Market Price per unit", 100)
qty = st.number_input("Quantity", 100)
transport = st.number_input("Transport Cost", 500)
loss = st.slider("Storage Loss Rate", 0.0, 0.2, 0.05)

net = calculate_net_revenue(price, qty, transport, loss)
st.success(f"Net Revenue: ₹{net}")

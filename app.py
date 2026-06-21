import streamlit as st

# 1. Page ki setting aur title
st.set_page_config(page_title="Automated Payroll System", layout="wide")

# 2. Sidebar Menu
st.sidebar.title("Navigation Menu 📋")
page = st.sidebar.radio("Go to:", ["Dashboard Home 🏠", "Employee Profiles 👥", "Attendance & Leaves 📅", "Salary Calculator 💰"])

# 3. Dashboard Home Page
if page == "Dashboard Home 🏠":
    st.title("Automated Payroll Dashboard 💸")
    st.write("Welcome to the Admin Control Panel.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Employees", value="150")
    col2.metric(label="Total Payroll This Month", value="Rs. 4,500,000")
    col3.metric(label="Pending Approvals", value="5")

# 4. Employee Profiles Page
elif page == "Employee Profiles 👥":
    st.title("Employee Profiles Management 👥")
    st.write("Yahan se aap naye employees add kar sakte hain.")

# 5. Attendance Page
elif page == "Attendance & Leaves 📅":
    st.title("Attendance & Leaves Tracker 📅")
    st.write("Employees ki hazri ka hisab-kitab yahan hoga.")

# 6. Salary Calculator Page
elif page == "Salary Calculator 💰":
    st.title("Salary & Tax Calculator 💰")
    st.write("Yahan system khud ba khud bonus aur tax calculate karega.")
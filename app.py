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
    st.markdown("---")
st.subheader("➕ Add New Employee Profile")

# Naye employee ki details lene ke liye input boxes
with st.form("employee_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        emp_name = st.text_input("Employee Name")
        emp_role = st.selectbox("Role/Designation", ["Teacher", "Admin", "Coordinator", "IT Support"])
    with col2:
        basic_salary = st.number_input("Basic Salary (Rs.)", min_value=0, step=5000)
        emp_email = st.text_input("Email Address")
    
    submit_btn = st.form_submit_button("Save Employee Profile")

if submit_btn:
    if emp_name:
        st.success(f"🎉 Profile created successfully for {emp_name} ({emp_role})!")
    else:
        st.warning("Please enter the employee name.")
        st.markdown("---")
st.subheader("🧮 Quick Salary Calculator")

col1, col2, col3 = st.columns(3)

with col1:
    sal_input = st.number_input("Enter Basic Salary (Rs.)", min_value=0, value=30000, step=1000)
with col2:
    allowances = st.number_input("Allowances / Bonus (Rs.)", min_value=0, value=0, step=500)
with col3:
    deductions = st.number_input("Deductions / Tax (Rs.)", min_value=0, value=0, step=500)

# Net Salary Calculate karne ka formula
net_salary = sal_input + allowances - deductions

# Screen par result khoobsurat tareeqay se dikhane ke liye
st.metric(label="Net Take-Home Salary", value=f"Rs. {net_salary:,}")
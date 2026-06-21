import streamlit as st

# Page Configuration for professional look
st.set_page_config(page_title="Automated Payroll System", page_icon="💼", layout="wide")

# --- INITIALIZE DATABASE (Session State) ---
# Agar memory mein pehle se data nahi hai, toh dummy data initialize karein
if "employee_list" not in st.session_state:
    st.session_state.employee_list = [
        {"name": "Maliha", "role": "Teacher", "salary": 45000, "email": "maliha@academy.com"},
        {"name": "Masooma", "role": "Coordinator", "salary": 55000, "email": "masooma@academy.com"},
        {"name": "Fatima", "role": "Admin", "salary": 40000, "email": "fatima@academy.com"},
        {"name": "Laiba", "role": "IT Support", "salary": 50000, "email": "laiba@academy.com"}
    ]

# Custom Styling for a decent and attractive look
st.markdown("""
    <style>
    .main-title { font-size: 38px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size: 16px; color: #555555; margin-bottom: 25px; }
    .metric-box { padding: 20px; background-color: #F3F4F6; border-radius: 10px; border-left: 5px solid #1E3A8A; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.title("Navigation Menu")
page = st.sidebar.radio("Go to:", ["🏠 Dashboard Home", "➕ Add Employee Profile", "🧮 Salary Calculator", "📅 Attendance & Leaves"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **FYP Project**\nAutomated Payroll Management Control Panel.")

# --- CALCULATE METRICS DYNAMICALLY ---
total_emp_count = len(st.session_state.employee_list) + 146  # Hum base 150 rakh rahe hain dummy dikhane ke liye
total_payroll = sum(emp['salary'] for emp in st.session_state.employee_list) + 4310000

# --- PAGE 1: DASHBOARD HOME ---
if page == "🏠 Dashboard Home":
    st.markdown('<p class="main-title">Automated Payroll Dashboard 💼</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Welcome to the Admin Control Panel. Quick system overview metrics are below.</p>', unsafe_allow_html=True)
    
    # Grid layout for Key Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric(label="Total Employees", value=f"{total_emp_count}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric(label="Total Payroll This Month", value=f"Rs. {total_payroll:,}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric(label="Pending Approvals", value="5")
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Display Registered Employees List
    st.markdown("<br><br><h3>📋 Registered System Profiles</h3>", unsafe_allow_html=True)
    st.table(st.session_state.employee_list)

# --- PAGE 2: ADD EMPLOYEE PROFILE ---
elif page == "➕ Add Employee Profile":
    st.markdown('<p class="main-title">Add New Employee Profile</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Fill out the form below to create a secure employee record in the system.</p>', unsafe_allow_html=True)
    
    with st.form("employee_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            emp_name = st.text_input("Employee Full Name")
            emp_role = st.selectbox("Role / Designation", ["Teacher", "Admin", "Coordinator", "IT Support"])
        with col2:
            basic_salary = st.number_input("Basic Salary (Rs.)", min_value=0, step=5000, value=25000)
            emp_email = st.text_input("Official Email Address")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submit_btn = st.form_submit_button("Save Employee Profile")
    
    if submit_btn:
        if emp_name and emp_email:
            # Append new data to our session state list
            new_emp = {"name": emp_name, "role": emp_role, "salary": basic_salary, "email": emp_email}
            st.session_state.employee_list.append(new_emp)
            st.success(f"🎉 Profile created successfully for {emp_name} ({emp_role})! Go check Dashboard Home.")
        else:
            st.error("Please fill in both Employee Name and Email Address before saving.")

# --- PAGE 3: SALARY CALCULATOR ---
elif page == "🧮 Salary Calculator":
    st.markdown('<p class="main-title">Quick Salary Calculator</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Compute net payouts instantly by adjusting allowances and statutory deductions.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        sal_input = st.number_input("Base Salary (Rs.)", min_value=0, value=30000, step=1000)
    with col2:
        allowances = st.number_input("Allowances / Bonus (Rs.)", min_value=0, value=0, step=500)
    with col3:
        deductions = st.number_input("Deductions / Tax (Rs.)", min_value=0, value=0, step=500)
    
    net_salary = sal_input + allowances - deductions
    st.markdown("---")
    st.metric(label="Net Take-Home Salary", value=f"Rs. {net_salary:,}")

# --- PAGE 4: ATTENDANCE & LEAVES ---
elif page == "📅 Attendance & Leaves":
    st.markdown('<p class="main-title">Attendance & Leave Tracker</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Monitor employee check-ins, monthly attendance percentages, and leave requests.</p>', unsafe_allow_html=True)
    st.info("System Module under configuration: Database integration setup coming next.")
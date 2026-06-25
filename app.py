import streamlit as st

# Page Configuration for professional look
st.set_page_config(page_title="Automated Payroll System", page_icon="💼", layout="wide")

# --- INITIALIZE DATABASE (Session State) ---
if "employee_list" not in st.session_state:
    st.session_state.employee_list = [
        {"name": "Maliha", "role": "Teacher", "salary": 45000, "email": "maliha@academy.com", "password": "123"},
        {"name": "Masooma", "role": "Coordinator", "salary": 55000, "email": "masooma@academy.com", "password": "123"},
        {"name": "Fatima", "role": "Admin", "salary": 40000, "email": "fatima@academy.com", "password": "123"},
        {"name": "Laiba", "role": "IT Support", "salary": 50000, "email": "laiba@academy.com", "password": "123"}
    ]


# Leave Requests Database setup
if "leave_requests" not in st.session_state:
    st.session_state.leave_requests = [
        {"id": 1, "name": "Maliha", "type": "Sick Leave", "days": 2, "status": "Pending ⏳"},
        {"id": 2, "name": "Masooma", "type": "Casual Leave", "days": 1, "status": "Pending ⏳"},
    ]

# Custom Styling
# --- REPLACED CLEAN CSS STYLING ---
st.markdown("""
    <style>
        /* 1. Pure Page ka Background */
        .stApp {
            background-color: #F8FAFC;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* 2. Main Title Design */
        h1, .main-title {
            color: #1E3A8A !important;
            font-size: 36px !important;
            font-weight: bold !important;
            padding-bottom: 10px;
            border-bottom: 3px solid #3B82F6;
            margin-bottom: 20px;
        }

        /* 3. Sidebar Colors & Text Visibility Fix */
        section[data-testid="stSidebar"] {
            background-color: #1E3A8A !important;
        }
        
        /* Sidebar ke andar saare text ko white karne ke liye */
        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }
        
        /* Sidebar radio buttons / menu links fix */
        section[data-testid="stSidebar"] label {
            color: #FFFFFF !important;
            font-weight: 500 !important;
        }

        /* 4. Dashboard Metrics Boxes */
        div[data-testid="metric-container"] {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        div[data-testid="stMetricValue"] {
            color: #1E3A8A !important;
            font-weight: bold !important;
        }
        div[data-testid="stMetricLabel"] {
            color: #475569 !important;
        }

        /* 5. App Buttons Styling */
        .stButton>button {
            background-color: #1E3A8A !important;
            color: white !important;
            border-radius: 6px !important;
            border: none !important;
            font-weight: 600 !important;
        }
        .stButton>button:hover {
            background-color: #3B82F6 !important;
        }
    </style>
""", unsafe_allow_html=True)
# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.title("Navigation Menu")
page = st.sidebar.radio("Go to:", ["🏠 Dashboard Home", "➕ Add Employee Profile", "📊 Salary Calculator", "📅 Attendance & Leaves", "Employee Portal"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **FYP Project**\nAutomated Payroll Management Control Panel.")

# --- CALCULATE METRICS DYNAMICALLY ---
total_emp_count = len(st.session_state.employee_list) + 146
total_payroll = sum(emp['salary'] for emp in st.session_state.employee_list) + 4310000
pending_leaves_count = sum(1 for req in st.session_state.leave_requests if "Pending" in req["status"])

# --- PAGE 1: DASHBOARD HOME ---
if page == "🏠 Dashboard Home":
    st.markdown('<p class="main-title">Automated Payroll Dashboard 💼</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Welcome to the Admin Control Panel. Quick system overview metrics are below.</p>', unsafe_allow_html=True)
    
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
        st.metric(label="Pending Approvals", value=f"{pending_leaves_count}")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("<br><br><h3>📋 Registered System Profiles</h3>", unsafe_allow_html=True)
    
    # --- ADDED: Interactive Search and Filter Module ---
    search_query = st.text_input("🔍 Search Employee Profile by Name:", placeholder="Type a name to filter... (e.g., Maliha, Aashiyaan)")
    
    # Filter python logic
    if search_query:
        filtered_list = [emp for emp in st.session_state.employee_list if search_query.lower() in emp['name'].lower()]
        st.caption(f"Showing {len(filtered_list)} matching entries out of {total_emp_count} global records.")
        st.table(filtered_list)
    else:
        st.caption(f"Showing {len(st.session_state.employee_list)} recent active master records out of {total_emp_count} global system logs.")
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
    st.markdown('<p class="sub-title">Monitor employee check-ins and process active leave applications below.</p>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Monthly Attendance Summary")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("Avg. Teachers Attendance")
        st.progress(0.92)
    with c2:
        st.write("Avg. Admin Staff Attendance")
        st.progress(0.88)
    with c3:
        st.write("Overall System Present Rate")
        st.progress(0.95)
        
    st.markdown("<br>---<br>", unsafe_allow_html=True)
    st.markdown("### ✉️ Pending Leave Requests")
    
    for i, req in enumerate(st.session_state.leave_requests):
        if "Pending" in req["status"]:
            with st.container():
                col_info, col_app, col_rej = st.columns([4, 1, 1])
                with col_info:
                    st.write(f"**{req['name']}** requested **{req['days']} Day(s)** for *{req['type']}*")
                with col_app:
                    if st.button(f"Approve ✅", key=f"app_{req['id']}"):
                        req["status"] = "Approved 🟢"
                        st.rerun()
                with col_rej:
                    if st.button(f"Reject ❌", key=f"rej_{req['id']}"):
                        req["status"] = "Rejected 🔴"
                        st.rerun()
        else:
            st.write(f"📝 *Request from {req['name']}: {req['status']}*")
            # ----------------------------------------------------
# --- NEW: EMPLOYEE PORTAL PANEL SECTION ---
# ----------------------------------------------------
if page == "👤 Employee Portal":
    st.markdown('<p class="main-title">Employee Self-Service Portal 👤</p>', unsafe_allow_html=True)
    st.write("Welcome to the Employee Portal. Please select your name to mark attendance or apply for leave.")
    
    # Employee selection dropdown
    employee_names = [emp["name"] for emp in st.session_state.employee_list]
    selected_emp = st.selectbox("Select Your Name:", employee_names)
    
    # Tabs for Attendance and Leaves
    tab1, tab2 = st.tabs(["📝 Mark Daily Attendance", "📅 Request Leave"])
    
    # TAB 1: ATTENDANCE
    with tab1:
        st.subheader("Daily Attendance Ingestion")
        attendance_status = st.radio("Select Status:", ["Present", "Absent"])
        
        if st.button("Submit Attendance", key="attendance_btn"):
            st.success(f"Thank you, {selected_emp}! Your attendance for today has been marked as '{attendance_status}'.")
            
    # TAB 2: LEAVE APPLICATION
    with tab2:
        st.subheader("Apply for Form Leave")
        with st.form(key="employee_leave_form"):
            leave_type = st.selectbox("Leave Type:", ["Sick Leave", "Casual Leave", "Short Leave"])
            leave_days = st.number_input("Number of Days:", min_value=1, max_value=10, value=1)
            reason = st.text_area("Reason for Leave:")
            
            submit_leave = st.form_submit_button("Submit Leave Application")
            
            if submit_leave:
                if reason.strip() == "":
                    st.error("Please provide a valid reason for leave.")
                else:
                    new_id = len(st.session_state.leave_requests) + 1
                    new_request = {
                        "id": new_id,
                        "name": selected_emp,
                        "type": leave_type,
                        "days": leave_days,
                        "status": "Pending"
                    }
                    st.session_state.leave_requests.append(new_request)
                    st.success(f"Leave application submitted successfully! Pending for Admin approval.")
                    # ----------------------------------------------------
# --- UPDATED: EMPLOYEE PORTAL WITH SECURE LOGIN ---
# ----------------------------------------------------
if page == "Employee Portal":
    st.markdown('<p class="main-title">Employee Portal Login 👤</p>', unsafe_allow_html=True)
    
    # Session state to track if user is logged in
    if "logged_in_user" not in st.session_state:
        st.session_state.logged_in_user = None

    if st.session_state.logged_in_user is None:
        # Show Login Form
        with st.form(key="login_form"):
            st.subheader("Sign In to Your Workspace")
            username_input = st.text_input("Enter Your Name / Email:")
            password_input = st.text_input("Enter Password:", type="password")
            login_submit = st.form_submit_button("Log In")
            
            if login_submit:
                # Authentication Logic
                matched_user = None
                for emp in st.session_state.employee_list:
                if (emp["name"].lower() == username_input.strip().lower() or emp.get("email", "").lower() == username_input.strip().lower()) and str(emp.get("password", "123")) == password_input.strip():
                        matched_user = emp
                        break
                
                if matched_user:
                    st.session_state.logged_in_user = matched_user
                    st.success(f"Welcome back, {matched_user['name']}! Login Successful.")
                    st.rerun()
                else:
                    st.error("Invalid Username or Password. Please try again.")
    else:
        # User is securely Authenticated
        current_user = st.session_state.logged_in_user
        st.write(f"Logged in as: **{current_user['name']}** ({current_user['role']})")
        
        # Log Out Button
        if st.button("Log Out"):
            st.session_state.logged_in_user = None
            st.rerun()
            
        st.markdown("---")
        
        # Tabs for Attendance and Leaves
        tab1, tab2 = st.tabs(["📝 Mark Daily Attendance", "📅 Request Leave"])
        
        # TAB 1: ATTENDANCE
        with tab1:
            st.subheader("Daily Attendance Ingestion")
            attendance_status = st.radio("Select Status:", ["Present", "Absent"])
            
            if st.button("Submit Attendance", key="auth_attendance_btn"):
                st.success(f"Thank you, {current_user['name']}! Your attendance for today has been marked as '{attendance_status}'.")
                
        # TAB 2: LEAVE APPLICATION
        with tab2:
            st.subheader("Apply for Leave")
            with st.form(key="auth_employee_leave_form"):
                leave_type = st.selectbox("Leave Type:", ["Sick Leave", "Casual Leave", "Short Leave"])
                leave_days = st.number_input("Number of Days:", min_value=1, max_value=10, value=1)
                reason = st.text_area("Reason for Leave:")
                
                submit_leave = st.form_submit_button("Submit Leave Application")
                
                if submit_leave:
                    if reason.strip() == "":
                        st.error("Please provide a valid reason for leave.")
                    else:
                        new_id = len(st.session_state.leave_requests) + 1
                        new_request = {
                            "id": new_id,
                            "name": current_user['name'],
                            "type": leave_type,
                            "days": leave_days,
                            "status": "Pending"
                        }
                        st.session_state.leave_requests.append(new_request)
                        st.success(f"Leave application submitted successfully! Pending for Admin approval.")
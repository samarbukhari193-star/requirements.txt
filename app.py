import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page config - professional look
st.set_page_config(
    page_title="Restaurant Management Dashboard",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern custom CSS for beautiful tabs
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
        justify-content: center;
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .stTabs [data-baseweb="tab"] {
        height: 65px;
        padding: 0 35px;
        background-color: white;
        border-radius: 10px;
        font-size: 17px;
        font-weight: 600;
        color: #2c3e50;
        border: 1px solid #ddd;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4361ee !important;
        color: white !important;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🍽️ Restaurant Management Dashboard")
st.markdown("Professional analytics for staff, bills, customers, food, and kitchen operations.")

# Generate sample data
np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=100, freq="D")

staff_data = pd.DataFrame({
    "Date": dates,
    "Staff": np.random.choice(["Alice", "Bob", "Charlie", "Diana", "Eve"], 100),
    "Hours": np.random.uniform(4, 12, 100).round(1),
    "Tips": np.random.uniform(20, 150, 100).round(2)
})

bill_data = pd.DataFrame({
    "Date": dates,
    "Bill ID": range(1001, 1101),
    "Amount": np.random.uniform(50, 350, 100).round(2),
    "Table": np.random.randint(1, 25, 100)
})

customers_data = pd.DataFrame({
    "Date": dates,
    "Total Customers": np.random.randint(60, 220, 100),
    "New Customers": np.random.randint(8, 35, 100),
    "Satisfaction": np.random.uniform(3.8, 5.0, 100).round(2)
})

food_category_data = pd.DataFrame({
    "Category": ["Appetizers", "Main Courses", "Desserts", "Beverages", "Specials"],
    "Sales ($)": [28000, 92000, 18000, 35000, 22000],
    "Orders": [1400, 4200, 950, 2400, 1100]
})

kitchen_data = pd.DataFrame({
    "Date": dates,
    "Dish": np.random.choice(["Pasta", "Salmon", "Burger", "Pizza", "Tiramisu"], 100),
    "Prep Time (min)": np.random.uniform(8, 35, 100).round(1),
    "Status": np.random.choice(["On Time", "Delayed", "Rush"], 100, p=[0.85, 0.10, 0.05])
})

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👥 Staff / Waiters",
    "💳 Bills",
    "🧑‍🤝‍🧑 Customers",
    "🍲 Food Categories",
    "🔪 Kitchen"
])

with tab1:
    st.header("Staff & Waiters Performance")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Hours (Last 30 Days)", f"{staff_data['Hours'].tail(30).sum():.1f}")
    with col2:
        st.metric("Total Tips (Last 30 Days)", f"${staff_data['Tips'].tail(30).sum():.0f}")
    
    fig = px.bar(staff_data.groupby("Staff")["Hours"].sum().reset_index(), x="Staff", y="Hours", color="Staff", title="Total Hours by Staff")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(staff_data.tail(20))

with tab2:
    st.header("Bills Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Bill", f"${bill_data['Amount'].mean():.2f}")
    with col2:
        st.metric("Total Revenue", f"${bill_data['Amount'].sum():.0f}")
    
    fig = px.histogram(bill_data, x="Amount", nbins=25, title="Bill Amount Distribution")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(bill_data.tail(20))

with tab3:
    st.header("Customer Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Avg Daily Customers", f"{customers_data['Total Customers'].mean():.0f}")
    with col2:
        st.metric("Avg Satisfaction", f"{customers_data['Satisfaction'].mean():.2f}/5.0")
    
    fig = px.line(customers_data, x="Date", y=["Total Customers", "New Customers"], title="Customer Trends Over Time")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(customers_data.tail(20))

with tab4:
    st.header("Food Categories Performance")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Top Category", "Main Courses")
    with col2:
        st.metric("Total Sales", f"${food_category_data['Sales ($)'].sum():,}")
    
    fig1 = px.pie(food_category_data, values="Sales ($)", names="Category", title="Sales Share")
    fig2 = px.bar(food_category_data, x="Category", y="Orders", color="Category", title="Orders by Category")
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)

with tab5:
    st.header("Kitchen Operations")
    issues = kitchen_data[kitchen_data["Status"] != "On Time"].shape[0]
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Prep Time", f"{kitchen_data['Prep Time (min)'].mean():.1f} min")
    with col2:
        st.metric("Delayed/Rush Orders", issues)
    
    fig = px.box(kitchen_data, x="Dish", y="Prep Time (min)", color="Dish", title="Prep Time by Dish")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(kitchen_data.tail(20))

# Footer
st.markdown("---")
st.caption("Professional Restaurant Dashboard • Deployed with ❤️ on Streamlit")

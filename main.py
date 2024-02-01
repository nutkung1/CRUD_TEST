import streamlit as st
import pymysql
pymysql.install_as_MySQLdb()
st.title("Hello")
# Initialize connection.
conn = st.connection('mysql', type='sql')
tab1, tab2, tab3 = st.tabs(["Farmer", "Cultivated_areas", "Fertilizer"])
option = st.sidebar.selectbox("Select an Operations", ("สร้าง", "อ่าน", "อัพเดท", "ลบ"))
#farmer tab
with tab1:

        # Perform query.
    df = conn.query('select * from farmer;', ttl=600)

    st.write(df)

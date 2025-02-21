import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")

# Custom CSS
st.markdown("""
<style>
   .stApp {
        background-color: black;
        color: white;
   }
</style>
""", unsafe_allow_html=True)

# Title & Description
st.title("▶️ Data Sweeper Sterling Integrator by Nazia Shoukat")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization. Creating the project for quarter 3.")

# File Uploader
uploaded_files = st.file_uploader("Choose a file to upload (accepts CSV or Excel files):", type=["csv", "xlsx"], accepts_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # File details
        st.write(f"🔍 Preview the head of the DataFrame for {file.name}")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from the file: {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed successfully")

            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values have been filled successfully")

        # Select Columns to Keep
        st.subheader("🎯 Select Columns to Keep")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Conversion Options
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer, file_name=file_name,
                mime=mime_type
            )

    st.success("✅ All files processed successfully")


# import streamlit as st 
# import pandas as pd
# import os
# import io import BytesIo



# st.set_page_config(page_title == "Data Sweeper",layout="wide")


# # custom css
# st.markdown("""
# <style>
#    .stApp{
#         background-color: black;
#         color:white;
#               }
# </style>
# """,
# unsafe_allow_html=True
# )

# # Title & Description
# st.title("▶️Data Sweeper sterling integrator by Nazia Shoukat")
# st.write("Transform your files between CSV and Excel formates with built-in data cleaning and visualization Creating the project for quarter 3")

# # File Uploader
# uploaded_file = st.file_uploader("Choose a file to upload(accepts CSV or Excel files):",type=["CSV","xlsx"],accepts_multiple_files=(True))

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#            df = pd.read_csv(file)
#         elif file_ext == "xlsx":
#             df = pd.read_excel(file)
#         else:
#             st:error(f"unsupported  file type:{file_ext}") continue
#             #file details
#             st.write("🔍 Preview the head of the Dataframe")
#             st.dataframe(df.head())


#        # Data Cleaning Options
#         st.subheader("🧹 Data Cleaning Options")
#         if st.checkbox(f"Clean data for {file.name}"): col1,col2 = st.columns(2) 

#         with col1:
#             if st.button("Remove Duplicates from the file:{file.name}"):
#                 df.drop_duplicates(inplace=True)
#                 st.write("Duplicates removed successfully")  

#         with col2:
#             if st.button("fill missing values for {file.name}"):
#                 numeric_cols = df.select_df.select_dtypes(includes=["number"]).columns
#                 df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].mean())  
#                 st.write("✅ Missing values have been filled successfully")    
    
#     st.subheader("🎯 Select Column to keep")
#     columns = st.multiselect(f"Choose columns for {file.name}",df.columns,default.df.columns)
#     df = df[columns]

#     # Data visualization
#     st.subheader("📊 Data Visualization for")
#     if st.checkbox(f"show visualization for {file.name}"):
#         st.bar_chart(df.select_dtypes(includes = "number").iloc[:,:2])

#     # Conversion Options
#     st.subheader("🔄 Conversion Options")
#     Conversion_type = st.radio(f"Convert {file.name} to:",["CSV" , "Excel"],key=file.name)
#     if st.button(f"Convert{file.name}"):
#         buffer = BytesIo()
#         if Conversion_type == "CSv":
#             df.to.csv(buffer,
#                       index=False)
#                       file_name = file.name = file.name.replace(file_ext,".csv")
#                       mine_type = "text/csv"
                
#                 elif Conversion_type
#                 == "Excel":
#                     df.to.to_excel(buffer,index = False)
#                     file_name = file.name.replace(file_ext,"xlsx")
#                     mine_type = "application/vnd.openxmlformates-officedocument.spreadsheetml.sheet"
#                 buffer.seek(0)  

#                 st.download_button(
#                     label = f"Download {file.name} as {Conversion_type}",
#                     data = buffer,file_name = file_name,
#                     mine=mine_type
#                 )  

# st.success("✅ All files pro cessed successfully")
            

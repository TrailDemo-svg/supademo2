import streamlit as st
from supabase import create_client
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

# Supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

# Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.5-flash")

st.title("Supabase + Gemini Demov3")

# if st.button("Load Data"):

#     result = (
#         supabase
#         .table("employees1")
#         .select("*")
#         .execute()
#     )

#     st.write("Employee Data")
#     st.write(result.data)
result = supabase.table("employees").select("*").execute()

question = st.text_input("Ask about employees") 

if st.button("Ask"):
    prompt = f"""
    Employee data:
    {result.data}

    User question:
    {question}

    Answer only from employee data.
    """
    #prompt = f"Summarize this employee data: {result.data}"

    response = model.generate_content(prompt)

    st.subheader("AI Summary")
    st.write(response.text)
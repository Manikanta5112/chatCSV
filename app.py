import streamlit as st
from langchain.agents import create_pandas_dataframe_agent, create_csv_agent
from langchain.llms import OpenAI
from typing import TextIO
import os
import logging

os.environ['OPENAI_API_KEY'] = "sk-"

def get_answer(file: TextIO, query: str, llm) -> str:
    logging.info(file.name)
   
    agent = create_csv_agent(llm,  file.name, verbose=False)
    logging.info(agent.json)
    return agent.run(query)

def main():

    st.set_page_config(page_title="Chat CSV")

    uploaded_files = st.file_uploader("upload your csv file", 
    label_visibility='collapsed', type=["csv"])

    if uploaded_files is not None:
        query = st.text_input("query about CSV")

        llm = OpenAI(temperature=0.1)


        if query is not None and len(query)>0:
            st.markdown(get_answer(uploaded_files, query, llm))
    

if __name__=='__main__':
    main()
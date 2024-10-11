
# invoke : LLM model 호출 directly
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

# content = "apple"

# result=llm.invoke("please make a poem about "+content)
# print(result)



import streamlit as st

st.title("Poet")
topic = st.text_input("Enter a title for your poem")

if st.button("Generate poem"):
    with st.spinner("Generating poem..."):
        result=llm.invoke("please make a poem about "+topic)
        st.write("topic of poem: ", topic)
        st.write(result)


# streamlit run poetMain.py
# https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML
# https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGMLv3-Q2-K

# invoke : LLM model 호출 directly
# from langchain_community.llms import Ollama
# llm = Ollama(model="llama2")

# from langchain_llms import CTransformers #C 기반 Transformer를 부를 수 있음
from langchain_community.llms import CTransformers



llm = CTransformers(
    model = "models/llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
    )


import streamlit as st

st.title("Poet")
topic = st.text_input("Enter a title for your poem")

if st.button("Generate poem"):
    with st.spinner("Generating poem..."):
        result=llm.invoke("please make a poem about "+topic)
        st.write("topic of poem: ", topic)
        st.write(result)


# streamlit run local_LLM_Main.py
# Using Steamlit we are creating frontend
import streamlit as st

# Below code is backend code for the app.py file
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


st.title("My chatbot using DeepSeek-R1")

template = '''question:  {question}
answer = Generate the answer step by StopIteration'''

prompt = ChatPromptTemplate.from_template(template)

# you can also use ollama-7b model after installing ollama
# model = OllamaLLM(model="llama-7b", prompt=prompt)
model = OllamaLLM(model="deepseek-r1")

chain = prompt | model

question  = input("Enter your Question here:  ")


if question:
    try:
        formatted_prompt = prompt.format(question=question)
        response = chain.invoke({"question":question})
        # print("Response: ", response)
        st.write(response)
        
    except Exception as e:
        # print(f"Error: {e}")
        st.write(f"Error: {e}")
        







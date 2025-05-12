# Using Steamlit we are creating frontend
import streamlit as st

# Below code is backend code for the app.py file
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Define the Generate_answer function
def Generate_answer(prompt):
    """
    Generates the answer step by StopIteration.

    Args:
        prompt: The prompt to generate the answer for.

    Returns:
        The answer step.
    """

    # Split the prompt into a list of instructions.
    instructions = prompt.split(".")

    # Initialize the answer step to the first instruction.
    answer_step = instructions[0]

    # Generate the answer by iterating over the remaining instructions.
    for instruction in instructions[1:]:
        # Check if the instruction is a verb.
        if "verb" in instruction:
            # Get the verb's object.
            object = instructions[instructions.index(instruction) + 1]

            # Add the object to the answer step.
            answer_step += " " + object

        # Check if the instruction is a noun.
        elif "noun" in instruction:
            # Get the noun's name.
            noun = instructions[instructions.index(instruction) + 1]

            # Add the noun to the answer step.
            answer_step += " " + noun

        # Check if the instruction is a stop word.
        elif "stop" in instruction:
            # Break out of the loop.
            break

    # Return the answer step.
    return answer_step

# Update the prompt template to make it more conversational
template = '''You are a helpful assistant. Answer the following question in a concise and clear manner:

Question: {question}
Answer:'''

prompt = ChatPromptTemplate.from_template(template)

# you can also use ollama-7b model after installing ollama
# model = OllamaLLM(model="llama-7b", prompt=prompt)
# model = OllamaLLM(model="deepseek-r1")
model = OllamaLLM(model="gemma:2b")

chain = prompt | model

# Update Streamlit interface
st.title("My chatbot using Gemma:2b")

# Input box for user question
question = st.text_input("Enter your Question here:")

if question:
    try:
        # Format the prompt with the user's question
        formatted_prompt = prompt.format(question=question)

        # Generate the response using the Gemma:2b model
        response = chain.invoke({"question": question})

        # Display the response on the Streamlit interface
        st.write("Response:", response)

    except Exception as e:
        # Display any errors on the Streamlit interface
        st.write(f"Error: {e}")

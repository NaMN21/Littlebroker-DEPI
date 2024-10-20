import streamlit as st
from transformers import pipeline

# Initialize the pipeline
pipe = pipeline("text-generation", model="openai-community/gpt2")

# Create the Streamlit app
def main():
    st.title("GPT-2 Text Generation")

    # Prompt input field
    prompt = st.text_input("Enter your prompt:")

    # Generate button
    if st.button("Generate"):
        # Generate text using the pipeline
        generated_text = pipe(prompt, max_length=100)
        st.text_area("Generated Text:", value=generated_text[0]['generated_text'])

if __name__ == "__main__":
    main()
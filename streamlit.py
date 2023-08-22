import streamlit as st

def english_quiz():
    st.title("English Quiz Exercise")
    
    # Create a sentence with missing words
    sentence = "I ___ my friend at the ___ yesterday."
    
    # List of options for the missing words
    options = {
        "first": ["met", "see", "talked"],
        "second": ["park", "mall", "movie theater"]
    }
    
    # Display sentence with missing words as placeholders
    st.write("Fill in the blanks:")
    st.write(sentence.replace("___", "__________"))
    
    # Display dropdowns for each missing word
    user_answers = {}
    for blank, word_options in options.items():
        user_answers[blank] = st.selectbox(f"Choose the correct word for {blank} blank:", word_options)
    
    # Check answers and provide feedback
    correct_answers = {
        "first": "met",
        "second": "movie theater"
    }
    
    num_correct = sum(1 for blank, answer in user_answers.items() if answer == correct_answers[blank])
    st.write(f"You got {num_correct} out of {len(options)} correct!")

# Run the quiz function
english_quiz()

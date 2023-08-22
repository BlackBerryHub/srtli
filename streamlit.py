import streamlit as st
import random
import time

# Global variables for tracking progress and score
progress = 0
score = 0

# Define tasks
tasks = [
    ("Fill in the Blanks", "Fill in the missing words in the sentence."),
    ("Multiple Choice", "Choose the correct option for the question."),
    ("Sentence Rearrangement", "Rearrange the words to form a sentence.")
]

# Shuffle the tasks order
random.shuffle(tasks)

def english_quiz():
    global progress, score
    
    st.title("English Quiz Exercise")
    
    st.sidebar.write(f"Progress: {progress}/{len(tasks)}")
    st.sidebar.write(f"Score: {score}/{len(tasks)}")
    
    if progress < len(tasks):
        task_name, task_desc = tasks[progress]
        st.subheader(task_name)
        st.write(task_desc)
        
        if task_name == "Fill in the Blanks":
            fill_in_the_blanks()
        elif task_name == "Multiple Choice":
            multiple_choice()
        elif task_name == "Sentence Rearrangement":
            sentence_rearrangement()
    else:
        show_summary()

def fill_in_the_blanks():
    global score
    
    sentence = "I ___ my friend at the ___ yesterday."
    options = {
        "first": ["met", "see", "talked"],
        "second": ["park", "mall", "movie theater"]
    }
    
    user_answers = {}
    for blank, word_options in options.items():
        user_answers[blank] = st.selectbox(f"Choose the correct word for {blank} blank:", word_options)
    
    correct_answers = {
        "first": "met",
        "second": "movie theater"
    }
    
    num_correct = sum(1 for blank, answer in user_answers.items() if answer == correct_answers[blank])
    score += num_correct
    
    st.write(f"You got {num_correct} out of {len(options)} correct!")
    
    if num_correct == len(options):
        st.success("Well done! All answers are correct.")
        st.write("🎉👏")
    else:
        st.warning("You have some incorrect answers. Here are the explanations:")
        for blank, correct_answer in correct_answers.items():
            if user_answers[blank] != correct_answer:
                st.write(f"For the {blank} blank, the correct answer is '{correct_answer}'.")
        st.write("😔")

def multiple_choice():
    global score
    
    question = "What is the capital of France?"
    choices = ["Paris", "London", "Berlin", "Madrid"]
    correct_answer = "Paris"
    
    # Display countdown timer
    timer_placeholder = st.empty()
    for seconds in range(10, 0, -1):
        timer_placeholder.write(f"Time left: {seconds} seconds")
        time.sleep(1)
    
    timer_placeholder.empty()
    
    user_choice = st.radio(question, choices)
    
    if user_choice == correct_answer:
        score += 1
        st.success("Correct!")
        st.write("🎉👏")
    else:
        st.error(f"Oops! The correct answer is {correct_answer}.")
        st.write("😔")

def sentence_rearrangement():
    global score
    
    sentence = "yesterday / I / the / park / visited"
    words = sentence.split(" / ")
    random.shuffle(words)
    
    st.write("Rearrange the words to form a sentence:")
    user_order = st.selectbox("Select the correct order:", words)
    
    if user_order == " ".join(words):
        score += 1
        st.success("Well done! You rearranged the sentence correctly.")
        st.write("🎉👏")
    else:
        st.error("Oops! Try rearranging the words again.")
        st.write("😔")

def show_summary():
    st.title("Quiz Summary")
    st.write(f"You scored {score} out of {len(tasks)}!")

    # Review answers
    st.subheader("Review Your Answers")
    for task_name, _ in tasks:
        st.write(f"{task_name}:")
        # Display the user's answer and whether it's correct or incorrect
        if task_name == "Fill in the Blanks":
            st.write("Your answer:", " ".join(user_answers.values()))
            st.write("Correct answer: met, movie theater")
        elif task_name == "Multiple Choice":
            st.write("Your answer:", user_choice)
            st.write("Correct answer: Paris")
        elif task_name == "Sentence Rearrangement":
            st.write("Your answer:", user_order)
            st.write("Correct answer: I visited the park yesterday")

    # Show progress as a pie chart
    progress_chart = st.empty()
    progress_data = [score, len(tasks) - score]
    progress_labels = ["Correct", "Incorrect"]
    progress_chart.pie(progress_data, labels=progress_labels, autopct="%1.1f%%", startangle=90)
    st.pyplot(progress_chart)

# Reset the quiz
def reset_quiz():
    global progress, score
    progress = 0
    score = 0
    random.shuffle(tasks)

# Add a reset button
if st.sidebar.button("Reset Quiz"):
    reset_quiz()

# Run the quiz function
english_quiz()

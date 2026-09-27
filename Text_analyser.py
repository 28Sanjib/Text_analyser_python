import streamlit as st

st.title("Text Analyzer Dashboard")

# Get input from the user using a text area
text = st.text_area('Enter your text here:')

# Add the analyse button
if st.button("Analyse"):
    # Ensure there is text to analyze
    if text.strip():
        # Calculate sentences
        Total_sentence_count = text.count('.')
        
        # Calculate punctuation and spaces to exclude from letter count
        total_punc_list = [' ', ',', '.', '"', ';']
        count = 0
        for pun in total_punc_list:
            count = count + text.count(pun)
            
        total_letters = len(text) - count
        
        # Calculate total words using split()
        total_words = len(text.split())
        
        # Calculate average word length
        if total_words > 0:
            Avg_word_length = total_letters / total_words
        else:
            Avg_word_length = 0.0

        # Display the results using Streamlit metrics
        st.subheader("Results")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Sentences", Total_sentence_count)
        with col2:
            st.metric("Letters", total_letters)
        with col3:
            st.metric("Words", total_words)
        with col4:
            st.metric("Avg Word Length", f"{Avg_word_length:.2f}")
    else:
        # Show a warning if the button is clicked but the text box is empty
        st.warning("Please enter some text to analyze.")

import streamlit as st

# Custom CSS for streamlit button styling 
st.markdown(
    """
    <style>
    /* Target the container holding the buttons within each column */
    div.row-widget.stButton > button { 
        display: block;
        margin: 0 auto; 
        width: 80%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app
st.title('Cyberbullying Detection System')


def predict_cyberbully(msg):
    return 0.5

message = st.text_area("Enter your message here:")
if st.button('Predict'):
    if message.strip() != "":
        prediction = predict_cyberbully(message)
        if prediction > 0.5:
            st.error("This message contains cyberbullying content.")
        else:
            st.success("This message does not contain cyberbullying content.")
    else:
        st.warning("Please enter a message.")
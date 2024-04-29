import streamlit as st
import pickle

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


ENCODER_PATH = "models/encoders/tfidf_vectorizer.pkl"
MODEL_PATH = "models/v2_tfidf/svc-tfidf.pkl"

model = pickle.load(open(MODEL_PATH, 'rb'))
encoder = pickle.load(open(ENCODER_PATH, 'rb'))

def __encode_text(text):
    return encoder.transform([text])

def predict_cyberbully(msg):
    return model.predict(__encode_text(msg).reshape(1, -1))

message = st.text_area("Enter your message here:")
if st.button('Predict'):
    if message.strip() != "":
        prediction = predict_cyberbully(message)
        print(prediction)
        if prediction[0] > 0.5:
            st.error("This message contains cyberbullying content.")
        else:
            st.success("This message does not contain cyberbullying content.")
    else:
        st.warning("Please enter a message.")
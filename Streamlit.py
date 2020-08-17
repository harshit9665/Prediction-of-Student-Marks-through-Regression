import streamlit as st
import pickle as pkl

pickle_in = open('regressor.pickle', 'rb')
regressor = pkl.load(pickle_in)

pickle_in.close()
st.title('SCORE PREDICTION WEBAPP')
st.markdown("This application is a Streamlit dashboard that can be used "
            "to predict the score of a student acording to his study hours")
st.header('ADD HOURS OF STUDY BELOW')

hours = st.number_input("ENTER HOURS")

st.success("PREDICTED SCORE OF THE STUDENT: {}".format(regressor.predict([[hours]])))
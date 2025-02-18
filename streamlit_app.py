import streamlit as st
import subprocess
import requests
import time

# Start the Flask app
flask_process = subprocess.Popen(['python', 'app.py'])

# Wait for the Flask app to start
time.sleep(5)

# Example to ensure Streamlit displays output
st.title('Car Price Prediction')
st.write('This is a simple example to ensure Streamlit displays output correctly.')

# Interact with the Flask app
st.write('Fetching data from Flask app...')
response = requests.get('http://127.0.0.1:5002/')
if response.status_code == 200:
    st.write('Flask app is running!')
else:
    st.write('Failed to connect to Flask app.')

# Add more Streamlit code as needed to interact with your Flask app

# Stop the Flask app when Streamlit app is closed
def stop_flask():
    flask_process.terminate()

st.on_event("shutdown", stop_flask)

import streamlit as st
import random
import datetime

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="KrishiAI - Smart Agriculture Assistant",
    page_icon="🌾🤖",
    layout="wide"
)

# ------------------------------
# Background Image CSS (Home Page)
# ------------------------------
bg_css = """
<style>
.stApp {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/6/65/Indian_farmer_in_field.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.overlay {
    background: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 12px;
}
</style>
"""

# ------------------------------
# Home Page
# ------------------------------
st.markdown(bg_css, unsafe_allow_html=True)

st.markdown(
    """
    <div class="overlay">
        <h1>🌾 Welcome to KrishiAI (कृषि AI)</h1>
        <h3>Your Smart Agriculture Assistant</h3>
        <p>
        🚜 Helping Farmers & Citizens with: <br>
        🌱 AI-based Crop Advisory <br>
        🐛 Pest & Disease Diagnosis <br>
        💰 Market Prices (मंडी भाव) <br>
        🌦️ Weather Information <br>
        📝 Citizen Problem Reporting <br>
        📰 Daily Agriculture News & Events
        </p>
        <hr>
        <p>👉 Use the sidebar menu to explore features.</p>
    </div>
    """,
    unsafe_allow_html=True
)

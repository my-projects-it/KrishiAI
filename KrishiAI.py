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
# Language Selector
# ------------------------------
st.sidebar.markdown("### 🌐 Language")
language = st.sidebar.radio("Choose Language", ["English", "हिन्दी"])

# ------------------------------
# Translation Dictionary
# ------------------------------
T = {
    "English": {
        "app_title": "🌾🤖 KrishiAI - Smart Agriculture Assistant",
        "welcome": "🌿 Welcome to KrishiAI",
        "about": """
        🚜 Helping Farmers & Citizens with:  
        🌱 AI-based Crop Advisory  
        🐛 Pest & Disease Diagnosis  
        💰 Market Prices  
        🌦️ Weather Information  
        📝 Citizen Problem Reporting  
        📰 Daily Agriculture News & Events  
        """,
        "menu": ["🏠 Home", "🌱 AI Crop Advisory", "🐛 AI Pest Diagnosis", 
                 "💰 AI Market Prices", "🌦️ AI Weather Info", 
                 "📝 AI Citizen Help", "📰 Agriculture News & Events"],
        "soil": "Select Soil Type",
        "season": "Select Season",
        "symptom": "Describe Problem",
        "problem": "Describe your problem",
        "button_suggestion": "Get AI Suggestion",
        "button_diagnosis": "Get AI Diagnosis",
        "button_help": "Get AI Help",
        "last_updated": "⏰ Last updated",
        "helplines": "📞 Helplines: 100 (Police), 101 (Fire), 108 (Ambulance)"
    },
    "हिन्दी": {
        "app_title": "🌾🤖 KrishiAI - स्मार्ट कृषि सहायक",
        "welcome": "🌿 कृषि AI में आपका स्वागत है",
        "about": """
        🚜 किसानों और नागरिकों की मदद के लिए:  
        🌱 AI आधारित फसल सलाह  
        🐛 कीट/रोग निदान  
        💰 मंडी भाव  
        🌦️ मौसम जानकारी  
        📝 नागरिक समस्या रिपोर्टिंग  
        📰 कृषि समाचार और घटनाएँ  
        """,
        "menu": ["🏠 होम", "🌱 AI फसल सलाह", "🐛 AI कीट/रोग निदान", 
                 "💰 AI मंडी भाव", "🌦️ AI मौसम जानकारी", 
                 "📝 AI नागरिक सहायता", "📰 कृषि समाचार"],
        "soil": "मिट्टी का प्रकार चुनें",
        "season": "मौसम चुनें",
        "symptom": "समस्या लिखें",
        "problem": "अपनी समस्या लिखें",
        "button_suggestion": "AI सलाह प्राप्त करें",
        "button_diagnosis": "AI निदान प्राप्त करें",
        "button_help": "AI मदद प्राप्त करें",
        "last_updated": "⏰ अंतिम अपडेट",
        "helplines": "📞 हेल्पलाइन: 100 (पुलिस), 101 (फायर), 108 (एम्बुलेंस)"
    }
}

txt = T[language]

# ------------------------------
# Title
# ------------------------------
st.title(txt["app_title"])

# ------------------------------
# Sidebar Navigation
# ------------------------------
menu = st.sidebar.radio("Go to", txt["menu"])

# ------------------------------
# Home Page
# ------------------------------
if menu == txt["menu"][0]:
    st.header(txt["welcome"])
    st.markdown(txt["about"])

# ------------------------------
# Crop Advisory
# ------------------------------
elif menu == txt["menu"][1]:
    st.header(txt["menu"][1])
    soil = st.selectbox(txt["soil"], ["Black Soil", "Loamy Soil", "Sandy Soil"])
    season = st.selectbox(txt["season"], ["Summer", "Rainy", "Winter"])
    if st.button(txt["button_suggestion"]):
        st.success(f"Suggested Crops for {soil} in {season} season.")

# ------------------------------
# Pest Diagnosis
# ------------------------------
elif menu == txt["menu"][2]:
    st.header(txt["menu"][2])
    symptom = st.text_area(txt["symptom"])
    if st.button(txt["button_diagnosis"]):
        st.info(f"Diagnosis for: {symptom}")

# ------------------------------
# Market Prices
# ------------------------------
elif menu == txt["menu"][3]:
    st.header(txt["menu"][3])
    st.write("👉 Wheat: ₹2200 / Quintal")
    st.write("👉 Rice: ₹1900 / Quintal")
    st.caption(f"{txt['last_updated']}: {datetime.datetime.now().strftime('%H:%M:%S')}")

# ------------------------------
# Weather Info
# ------------------------------
elif menu == txt["menu"][4]:
    st.header(txt["menu"][4])
    st.success("☀️ Sunny | Temp: 30°C")
    st.caption(f"{txt['last_updated']}: {datetime.datetime.now().strftime('%H:%M:%S')}")

# ------------------------------
# Citizen Help
# ------------------------------
elif menu == txt["menu"][5]:
    st.header(txt["menu"][5])
    problem = st.text_area(txt["problem"])
    if st.button(txt["button_help"]):
        st.success("✅ Department Assigned: Public Works Department")
        st.info(txt["helplines"])

# ------------------------------
# News & Events
# ------------------------------
elif menu == txt["menu"][6]:
    st.header(txt["menu"][6])
    st.write("📰 PM Kisan 21st Installment in Nov-Dec 2025.")
    st.write("📰 New subsidy announced for solar pumps.")

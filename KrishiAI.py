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
# Language Toggle
# ------------------------------
st.sidebar.markdown("### 🌐 Language / भाषा")
language = st.sidebar.radio("", ["English", "हिन्दी"])

# ------------------------------
# Text Dictionary
# ------------------------------
TEXT = {
    "English": {
        "home_title": "🌾 Welcome to KrishiAI",
        "home_sub": "Your Smart Agriculture Assistant",
        "home_info": """
        🚜 Helping Farmers & Citizens with:  
        🌱 AI-based Crop Advisory  
        🐛 Pest & Disease Diagnosis  
        💰 Market Prices  
        🌦️ Weather Information  
        📝 Citizen Problem Reporting  
        📰 Daily Agriculture News & Events
        """,
        "menu": ["🏠 Home", "🌱 AI Crop Advisory", "🐛 AI Pest Diagnosis", "💰 AI Market Prices",
                 "🌦️ AI Weather Info", "📝 AI Citizen Help", "📰 Agriculture News & Events"],
        "soil": "Select Soil Type",
        "season": "Select Season",
        "get_suggestion": "Get AI Suggestion",
        "describe_problem": "Describe Problem",
        "get_diagnosis": "Get AI Diagnosis",
        "get_help": "Get AI Help",
        "complaint_draft": "📄 Complaint Draft",
        "helplines": "📞 Helplines: 100 (Police), 101 (Fire), 108 (Ambulance)",
        "last_updated": "⏰ Last updated"
    },
    "हिन्दी": {
        "home_title": "🌾 कृषि AI में आपका स्वागत है",
        "home_sub": "आपका स्मार्ट कृषि सहायक",
        "home_info": """
        🚜 किसानों और नागरिकों की मदद के लिए:  
        🌱 AI आधारित फसल सलाह  
        🐛 कीट/रोग निदान  
        💰 मंडी भाव  
        🌦️ मौसम जानकारी  
        📝 नागरिक समस्या रिपोर्टिंग  
        📰 कृषि समाचार और घटनाएँ
        """,
        "menu": ["🏠 होम", "🌱 AI फसल सलाह", "🐛 AI कीट/रोग निदान", "💰 AI मंडी भाव",
                 "🌦️ AI मौसम जानकारी", "📝 AI नागरिक सहायता", "📰 कृषि समाचार"],
        "soil": "मिट्टी का प्रकार चुनें",
        "season": "मौसम चुनें",
        "get_suggestion": "AI सलाह प्राप्त करें",
        "describe_problem": "समस्या लिखें",
        "get_diagnosis": "AI निदान प्राप्त करें",
        "get_help": "AI मदद प्राप्त करें",
        "complaint_draft": "📄 शिकायत का प्रारूप",
        "helplines": "📞 हेल्पलाइन: 100 (पुलिस), 101 (फायर), 108 (एम्बुलेंस)",
        "last_updated": "⏰ अंतिम अपडेट"
    }
}
txt = TEXT[language]

# ------------------------------
# Functions
# ------------------------------
def crop_advisory(soil, season):
    soil = soil.lower()
    season = season.lower()

    suggestions = []
    if "black" in soil or "काली" in soil:
        if "summer" in season or "गर्मी" in season:
            suggestions = ["Soybean 🌱", "Cotton 👕", "Maize 🌽"]
        elif "rainy" in season or "बरसात" in season:
            suggestions = ["Pulses 🫘", "Groundnut 🥜", "Millets 🌾"]
        else:
            suggestions = ["Wheat 🌾", "Chickpea 🟤", "Mustard 🌼"]

    elif "loamy" in soil or "दोमट" in soil:
        if "rainy" in season or "बरसात" in season:
            suggestions = ["Rice 🍚", "Sugarcane 🍭", "Vegetables 🥬"]
        else:
            suggestions = ["Potato 🥔", "Onion 🧅", "Tomato 🍅"]

    elif "sandy" in soil or "रेतीली" in soil:
        if "winter" in season or "सर्दी" in season:
            suggestions = ["Wheat 🌾", "Mustard 🌼", "Chickpea 🟤"]
        else:
            suggestions = ["Groundnut 🥜", "Bajra 🌾", "Castor 🌱"]

    if suggestions:
        return f"✅ Recommended Crops: {', '.join(suggestions)}\n\n💡 Tip: Rotate crops yearly to improve soil fertility and reduce pest attack."
    else:
        return "⚠️ No direct match found. Please consult local Krishi Vigyan Kendra."

def pest_diagnosis(symptom):
    symptom = symptom.lower()
    if not symptom.strip():
        return "⚠️ Please describe symptoms or upload an image for better diagnosis."

    if "yellow" in symptom or "पीले" in symptom:
        return "🔎 Likely Cause: Nitrogen deficiency or Leaf Blight\n💡 Solution: Spray Urea (2%) foliar spray and ensure balanced fertilizer use."

    elif "hole" in symptom or "छेद" in symptom:
        return "🔎 Likely Cause: Stem borer or Leaf-eating caterpillar\n💡 Solution: Use pheromone traps, spray Neem oil (5 ml/L) or recommended pesticide."

    elif "rot" in symptom or "सड़न" in symptom:
        return "🔎 Likely Cause: Fungal infection (Root/Stem rot)\n💡 Solution: Treat seeds with fungicide before sowing and apply Copper oxychloride spray."

    elif "insect" in symptom or "कीड़े" in symptom:
        return "🔎 Likely Cause: General pest attack\n💡 Solution: Identify pest, use light traps, and adopt IPM (Integrated Pest Management)."

    else:
        return "📷 Please upload a photo for precise AI-based image diagnosis or contact nearest agriculture officer."

base_prices = {"Wheat | गेहूँ": 2200, "Rice | धान": 1900, "Soybean | सोयाबीन": 4800, "Cotton | कपास": 6200}
def get_dynamic_prices():
    prices = {}
    for crop, base in base_prices.items():
        fluctuation = random.randint(-100, 100)
        prices[crop] = f"₹{base + fluctuation} / Quintal | क्विंटल"
    return prices

def get_weather():
    conditions = ["☀️ Sunny | धूप", "🌧️ Rainy | बारिश", "⛅ Partly Cloudy | आंशिक बादल", "🌪️ Windy | तेज़ हवा"]
    temp = random.randint(20, 40)
    return f"{random.choice(conditions)} | Temp: {temp}°C"

def classify_problem(problem):
    problem = problem.lower()
    if "road" in problem or "गड्ढा" in problem:
        return "Public Works Department (PWD)"
    elif "electricity" in problem or "बिजली" in problem:
        return "Electricity Board"
    elif "water" in problem or "पानी" in problem:
        return "Jal Board"
    elif "hospital" in problem or "health" in problem:
        return "Health Department"
    elif "police" in problem or "सुरक्षा" in problem:
        return "Police Department"
    else:
        return "Municipal Corporation"

def generate_complaint(problem, dept):
    return f"""
To,
{dept}

Subject: Complaint regarding public issue

Respected Sir/Madam,
Problem: {problem}
Kindly take immediate action.

धन्यवाद,
Citizen
"""

def agriculture_news():
    news_list = [
        "PM Kisan 21st Installment likely in Nov-Dec 2025. [Govt Link](https://pmkisan.gov.in/)",
        "GST rates reduced for agricultural products. [News Link](https://newsonair.gov.in/)",
        "eNAM portal updated with new crops. [eNAM Portal](https://www.enam.gov.in/)",
        "Weather Alert: Heavy rainfall expected. [IMD](https://mausam.imd.gov.in/)",
        "Agri Ministry announces new subsidy for solar pumps. [Agri Ministry](https://agricoop.nic.in/)"
    ]
    for news in news_list:
        st.write("📰 " + news)

# ------------------------------
# Sidebar Navigation
# ------------------------------
menu = st.sidebar.radio("📌 Navigation", txt["menu"])

# ------------------------------
# Pages
# ------------------------------
if menu == txt["menu"][0]:  # Home
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
            background-attachment: fixed;
            color: #003300;
        }
        .overlay {
            background: rgba(255, 255, 255, 0.85);
            padding: 25px;
            border-radius: 12px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown(f"<div class='overlay'><h1>{txt['home_title']}</h1><h3>{txt['home_sub']}</h3><p>{txt['home_info']}</p></div>", unsafe_allow_html=True)

elif menu == txt["menu"][1]:
    st.header(txt["menu"][1])
    soil = st.selectbox(txt["soil"], ["Black Soil | काली मिट्टी", "Loamy Soil | दोमट मिट्टी", "Sandy Soil | रेतीली मिट्टी"])
    season = st.selectbox(txt["season"], ["Summer | गर्मी", "Rainy | बरसात", "Winter | सर्दी"])
    if st.button(txt["get_suggestion"]):
        st.success(crop_advisory(soil, season))

elif menu == txt["menu"][2]:
    st.header(txt["menu"][2])
    symptom = st.text_area(txt["describe_problem"])
    if st.button(txt["get_diagnosis"]):
        st.info(pest_diagnosis(symptom))

elif menu == txt["menu"][3]:
    st.header(txt["menu"][3])
    prices = get_dynamic_prices()
    for crop, price in prices.items():
        st.write(f"👉 {crop}: {price}")
    st.caption(f"{txt['last_updated']}: {datetime.datetime.now().strftime('%H:%M:%S')}")

elif menu == txt["menu"][4]:
    st.header(txt["menu"][4])
    st.success(get_weather())
    st.caption(f"{txt['last_updated']}: {datetime.datetime.now().strftime('%H:%M:%S')}")

elif menu == txt["menu"][5]:
    st.header(txt["menu"][5])
    problem = st.text_area(txt["describe_problem"])
    if st.button(txt["get_help"]):
        if problem.strip():
            dept = classify_problem(problem)
            st.success(f"✅ Responsible Department: {dept}")
            st.text_area(txt["complaint_draft"], generate_complaint(problem, dept), height=250)
            st.info(txt["helplines"])
        else:
            st.warning("⚠️ Please enter a problem")

elif menu == txt["menu"][6]:
    st.header(txt["menu"][6])
    agriculture_news()

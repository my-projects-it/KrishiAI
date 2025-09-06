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
# Background Image + CSS
# ------------------------------
st.markdown(
    """
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        color: #004d00;
    }
    .stApp {
        background: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3, h4 {
        color: #006600;
    }
    .menu-button {
        background-color: #66cc66;
        color: white;
        font-weight: bold;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
        cursor: pointer;
        box-shadow: 2px 2px 5px grey;
        transition: all 0.3s ease;
    }
    .menu-button:hover {
        background-color: #339933;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# App Title
# ------------------------------
st.title("🌾🤖 KrishiAI - Smart Agriculture Assistant")
st.subheader("Your AI Assistant for Farming, Market, Weather & Citizen Help (आपका कृषि AI सहायक)")

# ------------------------------
# AI Crop Advisory
# ------------------------------
def crop_advisory(soil, season):
    if soil == "Black Soil | काली मिट्टी" and season == "Summer | गर्मी":
        return "AI Suggestion (सुझाव): Soybean, Cotton, Maize (सोयाबीन, कपास, मक्का)"
    elif soil == "Loamy Soil | दोमट मिट्टी" and season == "Rainy | बरसात":
        return "AI Suggestion (सुझाव): Rice, Sugarcane, Vegetables (धान, गन्ना, सब्जियाँ)"
    elif soil == "Sandy Soil | रेतीली मिट्टी" and season == "Winter | सर्दी":
        return "AI Suggestion (सुझाव): Wheat, Chickpea, Mustard (गेहूँ, चना, सरसों)"
    else:
        return "AI Suggestion (सुझाव): Consult local agriculture expert (स्थानीय कृषि विशेषज्ञ से सलाह लें)"

# ------------------------------
# AI Pest Diagnosis
# ------------------------------
def pest_diagnosis(symptom):
    symptom = symptom.lower()
    if "yellow" in symptom or "पीले" in symptom:
        return "AI Diagnosis (निदान): Nitrogen deficiency or Leaf Blight (नाइट्रोजन कमी / पत्ती झुलसा रोग). Apply Urea (यूरिया का छिड़काव)."
    elif "insect" in symptom or "कीड़े" in symptom:
        return "AI Diagnosis (निदान): Pest attack (कीट प्रकोप). Use Neem Oil or Recommended Pesticide (नीम तेल / कीटनाशक)."
    elif "rot" in symptom or "सड़न" in symptom:
        return "AI Diagnosis (निदान): Fungal Infection (फफूंदी संक्रमण). Apply Fungicide (फफूंदनाशक)."
    else:
        return "AI Diagnosis (निदान): Upload photo for precise AI analysis (सटीक निदान के लिए फोटो अपलोड करें)."

# ------------------------------
# Market Prices
# ------------------------------
base_prices = {
    "Wheat | गेहूँ": 2200,
    "Rice | धान": 1900,
    "Soybean | सोयाबीन": 4800,
    "Cotton | कपास": 6200
}
def get_dynamic_prices():
    prices = {}
    for crop, base in base_prices.items():
        fluctuation = random.randint(-100, 100)
        prices[crop] = f"₹{base + fluctuation} / Quintal | क्विंटल"
    return prices

# ------------------------------
# Weather Info
# ------------------------------
def get_weather():
    conditions = ["☀️ Sunny | धूप", "🌧️ Rainy | बारिश", "⛅ Partly Cloudy | आंशिक बादल", "🌪️ Windy | तेज़ हवा"]
    temp = random.randint(20, 40)
    condition = random.choice(conditions)
    return f"{condition} | Temp: {temp}°C | तापमान: {temp}°C"

# ------------------------------
# Citizen Problem Reporting
# ------------------------------
def classify_problem(problem):
    problem = problem.lower()
    if "road" in problem or "गड्ढा" in problem:
        return "Public Works Department (PWD) | लोक निर्माण विभाग"
    elif "electricity" in problem or "बिजली" in problem:
        return "Electricity Board | विद्युत विभाग"
    elif "water" in problem or "पानी" in problem:
        return "Jal Board | जल विभाग"
    elif "hospital" in problem or "health" in problem or "अस्पताल" in problem:
        return "Health Department | स्वास्थ्य विभाग"
    elif "police" in problem or "सुरक्षा" in problem:
        return "Police Department | पुलिस विभाग"
    else:
        return "Municipal Corporation | नगर निगम"

def generate_complaint(problem, dept):
    return f"""
To,
{dept}

Subject: Complaint regarding public issue

Respected Sir/Madam,

I, a concerned citizen, would like to report the following issue:
Problem: {problem}

I request you to kindly take immediate action to resolve this matter.

Thank you,
Citizen

सेवा में,
{dept}

विषय: जनसमस्या के संबंध में शिकायत

मान्यवर,

मैं एक जागरूक नागरिक हूँ और आपकी संज्ञान में यह समस्या लाना चाहता हूँ:
समस्या: {problem}

आपसे निवेदन है कि कृपया शीघ्र कार्यवाही करें।

धन्यवाद,
नागरिक
"""

# ------------------------------
# Agriculture News & Events (Sample)
# ------------------------------
def agriculture_news():
    news_list = [
        "PM Kisan 21st Installment likely in Nov-Dec 2025. [Govt Link](https://pmkisan.gov.in/)",
        "GST rates reduced for agricultural products from 22 Sept 2025. [News Link](https://newsonair.gov.in/)",
        "eNAM portal updated with new crops. [eNAM Portal](https://www.enam.gov.in/)",
        "Weather Alert: Heavy rainfall expected in Maharashtra. [IMD](https://mausam.imd.gov.in/)",
        "Agri Ministry announces new subsidy for solar pumps. [Agri Ministry](https://agricoop.nic.in/)"
    ]
    for news in news_list:
        st.write("📰 " + news)

# ------------------------------
# Special Menu Buttons
# ------------------------------
st.subheader("🌿 Select Feature (फीचर चुनें)")
col1, col2 = st.columns(2)

with col1:
    if st.button("🌱 AI Crop Advisory | फसल सलाह", key="crop"):
        st.session_state.menu = "AI Crop Advisory"

    if st.button("🐛 AI Pest Diagnosis | कीट/रोग निदान", key="pest"):
        st.session_state.menu = "AI Pest Diagnosis"

    if st.button("💰 AI Market Prices | मंडी भाव", key="market"):
        st.session_state.menu = "AI Market Prices"

with col2:
    if st.button("🌦️ AI Weather Info | मौसम जानकारी", key="weather"):
        st.session_state.menu = "AI Weather Info"

    if st.button("📝 AI Citizen Help | नागरिक सहायता", key="citizen"):
        st.session_state.menu = "AI Citizen Help"

    if st.button("📰 Agriculture News & Events | कृषि समाचार", key="news"):
        st.session_state.menu = "Agriculture News & Events"

# ------------------------------
# Default menu state
# ------------------------------
if "menu" not in st.session_state:
    st.session_state.menu = "AI Crop Advisory"

menu = st.session_state.menu

# ------------------------------
# Main Logic
# ------------------------------
if menu == "AI Crop Advisory":
    st.header("🌱 AI Crop Suggestion (फसल सलाह)")
    soil = st.selectbox("Select Soil Type (मिट्टी का प्रकार चुनें)", ["Black Soil | काली मिट्टी", "Loamy Soil | दोमट मिट्टी", "Sandy Soil | रेतीली मिट्टी"])
    season = st.selectbox("Select Season (मौसम चुनें)", ["Summer | गर्मी", "Rainy | बरसात", "Winter | सर्दी"])
    if st.button("Get AI Suggestion (AI सलाह प्राप्त करें)"):
        st.success(crop_advisory(soil, season))

elif menu == "AI Pest Diagnosis":
    st.header("🐛 AI Pest & Disease Diagnosis (कीट/रोग निदान)")
    symptom = st.text_area("Describe Problem (समस्या लिखें: yellow leaves, कीड़े, सड़न etc.)")
    if st.button("Get AI Diagnosis (AI निदान प्राप्त करें)"):
        st.info(pest_diagnosis(symptom))

elif menu == "AI Market Prices":
    st.header("💰 AI Powered Market Prices (मंडी भाव)")
    prices = get_dynamic_prices()
    for crop, price in prices.items():
        st.write(f"👉 {crop}: {price}")
    st.caption(f"⏰ Last updated: {datetime.datetime.now().strftime('%H:%M:%S')}")

elif menu == "AI Weather Info":
    st.header("🌦️ AI Weather Update (मौसम जानकारी)")
    st.success(get_weather())
    st.caption(f"⏰ Last updated: {datetime.datetime.now().strftime('%H:%M:%S')}")

elif menu == "AI Citizen Help":
    st.header("📝 AI Citizen Problem Reporting (नागरिक शिकायत)")
    problem = st.text_area("Describe your problem (समस्या लिखें)")
    if st.button("Get AI Help (AI मदद प्राप्त करें)"):
        if problem.strip() == "":
            st.warning("Please enter a problem (कृपया समस्या लिखें)")
        else:
            dept = classify_problem(problem)
            st.success(f"✅ Responsible Department (जिम्मेदार विभाग): {dept}")
            complaint = generate_complaint(problem, dept)
            st.text_area("📄 Complaint Draft (शिकायत पत्र)", complaint, height=250)
            st.info("📞 Important Helplines: 100 (Police), 101 (Fire), 108 (Ambulance)")

elif menu == "Agriculture News & Events":
    st.header("📰 Agriculture News & Events (कृषि समाचार और घटनाएँ)")
    agriculture_news()

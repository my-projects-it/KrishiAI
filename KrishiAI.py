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
# Background Image + Animations CSS
# ------------------------------
st.markdown(
    """
    <style>
    /* Background Animation */
    body {
        background: linear-gradient(-45deg, #d4fcd6, #f0fff0, #e0ffe0, #c8f7c5);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Main App Card */
    .stApp {
        background: rgba(255, 255, 255, 0.92);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0, 100, 0, 0.2);
    }

    /* Heading Color & Animation */
    h1, h2, h3, h4 {
        color: #006400 !important;
        text-shadow: 1px 1px 2px #99ff99;
        animation: fadeIn 2s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }

    /* Menu Buttons */
    .menu-button {
        background: linear-gradient(135deg, #66cc66, #339933);
        color: white;
        font-weight: bold;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
        cursor: pointer;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .menu-button:hover {
        background: linear-gradient(135deg, #33cc33, #228822);
        transform: scale(1.08);
    }

    /* Text Fade-in Effect */
    .stMarkdown, .stText, .stAlert {
        animation: fadeIn 1.5s ease-in;
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
# --------

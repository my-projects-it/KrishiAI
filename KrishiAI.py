import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="KrishiAI - Smart Farming App", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown(
    """
    <style>
    /* Background Animation */
    html, .stApp {
        background: linear-gradient(270deg, #e8f5e9, #f1f8e9, #e0f7fa);
        background-size: 600% 600%;
        animation: gradientShift 18s ease infinite;
        font-family: 'Trebuchet MS', sans-serif;
    }

    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Headings */
    h1, h2, h3 {
        color: #2e7d32;
        text-align: center;
        font-weight: bold;
    }

    /* Menu Buttons */
    .stButton > button {
        width: 100%;
        background: #a5d6a7;
        color: black;
        border: none;
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: #66bb6a;
        color: white;
        transform: scale(1.05);
    }

    /* Info Box */
    .info-box {
        background: #f1f8e9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #66bb6a;
        margin: 10px 0;
        animation: fadeIn 1.5s ease;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ TITLE ------------------
st.markdown("<h1>🌱 KrishiAI - Smart Farming App</h1>", unsafe_allow_html=True)
st.markdown("### आपकी खेती में सहायक कृत्रिम बुद्धिमत्ता (AI for Farmers)")

# ------------------ SIDEBAR MENU ------------------
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio(
    "कृपया चुनें:",
    ["🏠 Home", "🌾 Farming Tips", "📰 Agriculture News & Events", "📊 Weather & Market Info"]
)

# ------------------ HOME ------------------
if menu == "🏠 Home":
    st.markdown("<div class='info-box'><h2>Welcome to KrishiAI!</h2></div>", unsafe_allow_html=True)
    st.write(
        "यह एक स्मार्ट एग्रीकल्चर AI ऐप है, जो किसानों को मदद करता है "
        "खेती, मौसम, मंडी भाव और सरकारी योजनाओं की जानकारी पाने में।"
    )

# ------------------ FARMING TIPS ------------------
elif menu == "🌾 Farming Tips":
    st.markdown("<h2>🌾 खेती के सुझाव</h2>", unsafe_allow_html=True)
    tips = [
        "समय पर बुवाई और कटाई करें।",
        "खेत में जल निकासी का सही प्रबंध रखें।",
        "जैविक खाद का प्रयोग बढ़ाएं।",
        "फसल चक्र का पालन करें।",
        "मौसम के अनुसार फसलें चुनें।"
    ]
    for t in tips:
        st.markdown(f"<div class='info-box'>✅ {t}</div>", unsafe_allow_html=True)

# ------------------ AGRICULTURE NEWS ------------------
elif menu == "📰 Agriculture News & Events":
    st.markdown("<h2>📰 कृषि समाचार और घटनाएँ</h2>", unsafe_allow_html=True)

    st.markdown("<div class='info-box'>🌧️ राजस्थान में मानसून के दौरान 193 लोगों की मौत की रिपोर्ट।</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>💰 PM Kisan की 21वीं किस्त नवंबर-दिसंबर 2025 में जारी होने की संभावना।</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>📉 GST दरों में कमी से किसानों को राहत।</div>", unsafe_allow_html=True)

    st.markdown("### 🌐 सरकारी पोर्टल्स के लिंक")
    st.markdown("[PM Kisan Samman Nidhi](https://pmkisan.gov.in/)")
    st.markdown("[eNAM - National Agriculture Market](https://www.enam.gov.in/)")
    st.markdown("[कृषि मंत्रालय - भारत सरकार](https://agriwelfare.gov.in/)")

# ------------------ WEATHER & MARKET INFO ------------------
elif menu == "📊 Weather & Market Info":
    st.markdown("<h2>📊 मौसम और मंडी जानकारी</h2>", unsafe_allow_html=True)

    st.markdown("<div class='info-box'>☀️ आज का मौसम: 32°C, हल्की बारिश की संभावना</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>🌾 गेहूँ: ₹2200 / क्विंटल</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>🌽 मक्का: ₹1850 / क्विंटल</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>🥥 सरसों: ₹5500 / क्विंटल</div>", unsafe_allow_html=True)

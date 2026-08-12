import os
import pickle
import requests
import numpy as np
import pandas as pd
import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Gaming Optimization System",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LOAD RECOMMENDED ACTION RULES
# =========================================================

try:
    with open("recommended_action_rules.pkl", "rb") as file:
        recommended_action_rules = pickle.load(file)
except Exception:
    # Fallback rule matrix mapped to project requirements
    recommended_action_rules = {
        ("Casual", "High"): "Retention Campaign",
        ("Casual", "High Risk"): "Retention Campaign",
        ("Casual", "Low"): "Improve Engagement",
        ("Casual", "Low Risk"): "Improve Engagement",
        ("Moderate", "High"): "Retention Campaign",
        ("Moderate", "High Risk"): "Retention Campaign",
        ("Moderate", "Low"): "Maintain Difficulty",
        ("Moderate", "Low Risk"): "Maintain Difficulty",
        ("Hardcore", "High"): "Retention Campaign",
        ("Hardcore", "High Risk"): "Retention Campaign",
        ("Hardcore", "Low"): "Increase Difficulty",
        ("Hardcore", "Low Risk"): "Increase Difficulty"
    }


# =========================================================
# PROFESSIONAL DARK VIOLET THEME & CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background: #16002B;
}

[data-testid="stAppViewContainer"] {
    background: #16002B;
}

[data-testid="stMain"] {
    background: #16002B;
}

header[data-testid="stHeader"] {
    background: #16002B;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #210B38;
    border-right: 1px solid #4A2A68;
}

section[data-testid="stSidebar"] * {
    color: #E9D5FF;
}

/* Main content container */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Headings */
h1 {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    white-space: nowrap !important;
}

h2 {
    color: #E9D5FF !important;
    font-weight: 600 !important;
}

h3 {
    color: #D8B4FE !important;
}

/* Text */
p, li {
    color: #D6C7E8 !important;
    line-height: 1.7;
}

/* Input labels */
label {
    color: #E9D5FF !important;
    font-weight: 500 !important;
}

/* Number & Text Inputs */
div[data-baseweb="input"] {
    background-color: #28143F !important;
    border: 1px solid #6D28D9 !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] input {
    background-color: #28143F !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Select boxes (Input Container & Selected Text) */
div[data-baseweb="select"] {
    background-color: #28143F !important;
    border-radius: 8px !important;
}

div[data-baseweb="select"] > div {
    background-color: #28143F !important;
    border: 1px solid #6D28D9 !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
}

div[data-baseweb="select"] * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Dropdown Menu Overlay / Popover */
div[data-baseweb="popover"], div[data-baseweb="popover"] > div {
    background-color: #28143F !important;
    border-radius: 8px !important;
}

ul[data-baseweb="menu"], [data-baseweb="menu"] {
    background-color: #28143F !important;
}

li[data-baseweb="option"], [data-baseweb="option"] {
    background-color: #28143F !important;
    color: #FFFFFF !important;
}

li[data-baseweb="option"]:hover, [data-baseweb="option"]:hover {
    background-color: #5B21B6 !important;
    color: #FFFFFF !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: #7C3AED !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.75rem 1rem !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    background: #8B5CF6 !important;
}

/* Metric cards formatting */
div[data-testid="stMetric"] {
    background: #28143F !important;
    border: 1px solid #4A2A68 !important;
    border-radius: 14px !important;
    padding: 16px 20px !important;
    min-height: 110px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
}

div[data-testid="stMetricLabel"] {
    color: #CDB5E8 !important;
    font-size: 14px !important;
}

div[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 22px !important;
    white-space: normal !important;
    word-break: break-word !important;
}

/* Custom Output Box for Action */
.action-box {
    background: #28143F;
    border: 1px solid #7C3AED;
    border-radius: 14px;
    padding: 16px 20px;
    min-height: 110px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.action-label {
    color: #CDB5E8;
    font-size: 14px;
    margin-bottom: 4px;
}

.action-value {
    color: #F3E8FF;
    font-size: 20px;
    font-weight: 700;
    line-height: 1.2;
}

/* Dividers */
hr {
    border-color: #4A2A68 !important;
}

/* Custom Cards */
.overview-card {
    background: #28143F;
    border: 1px solid #4A2A68;
    border-radius: 16px;
    padding: 22px;
    min-height: 190px;
    margin-bottom: 15px;
}

.hero-card {
    background: linear-gradient(135deg, #28143F, #321650);
    border: 1px solid #5B347A;
    border-radius: 18px;
    padding: 30px;
}

.business-card {
    background: linear-gradient(135deg, #28143F, #351653);
    border: 1px solid #5B347A;
    border-radius: 18px;
    padding: 30px;
}

.detail-box {
    background: #230E38;
    border: 1px solid #4D286E;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

.disclaimer-box {
    background: rgba(124, 58, 237, 0.12);
    border: 1px solid #6D28D9;
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 20px;
    font-size: 14px;
    color: #E9D5FF;
}

.rule-badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 13px;
}

.badge-high { background: #581C25; color: #FCA5A5; border: 1px solid #991B1B; }
.badge-low { background: #14532D; color: #86EFAC; border: 1px solid #166534; }
.badge-action { background: #4C1D95; color: #DDD6FE; border: 1px solid #6D28D9; }

.footer-text {
    text-align: center;
    color: #A78BFA;
    font-size: 15px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎮 Gaming AI")

st.sidebar.markdown("### 📌 Navigation")

page = st.sidebar.radio(
    "Select a page",
    [
        "🏠 Overview",
        "📋 Project Details & ML",
        "🔮 Prediction System"
    ]
)


# =========================================================
# OVERVIEW PAGE
# =========================================================

if page == "🏠 Overview":

    st.title("🎮 AI-Based Dynamic Difficulty & Retention Engine")
    st.write("")

    # -----------------------------------------------------
    # INTRODUCTION + IMAGE
    # -----------------------------------------------------

    intro_col, image_col = st.columns([1.4, 1], gap="large")

    with intro_col:
        st.markdown(
            """
            <div class="hero-card">
            <p style="font-size:17px; line-height:1.8;">
            In today’s competitive gaming industry, keeping players engaged is a major challenge. 
            Players have different levels of experience, activity, and interaction with a game, 
            so a single gameplay approach may not provide an enjoyable experience for everyone. 
            At the same time, reduced engagement can increase the likelihood of players leaving.
            </p>
            <p style="font-size:17px; line-height:1.8;">
            The <span style="color:#C084FC; font-weight:600;">AI-Based Dynamic Difficulty & Retention Engine</span> 
            addresses this challenge by using player data to understand individual player behavior, 
            categorize players based on their gaming activity, and identify those who may be at risk of churn. 
            Based on these insights, the system provides suitable actions to help maintain an engaging and balanced gaming experience.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with image_col:
        image_path = r"C:\Users\LENOVO\Desktop\data pics\gaming.jpg"
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.warning("🖼️ Gaming visual asset not found. Add image to view hero graphic.")

    st.divider()

    # -----------------------------------------------------
    # ACTIONABLE INSIGHTS
    # -----------------------------------------------------

    st.subheader("🎯 From Player Data to Actionable Insights")

    st.write(
        "Rather than treating every player identically, "
        "the engine resolves three core dimensions:"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="overview-card">
            <h3>👤 Player Categorization</h3>
            <p>
            Segments players based on weekly playtime into:
            <span style="color:#C084FC; font-weight:600;">Casual (&lt;10 hrs)</span>, 
            <span style="color:#C084FC; font-weight:600;">Moderate (10–20 hrs)</span>, or 
            <span style="color:#C084FC; font-weight:600;">Hardcore (&gt;20 hrs)</span>.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="overview-card">
            <h3>📈 Progression & Engagement</h3>
            <p>
            Evaluates achievement velocity, session frequencies, and match completion rates to assess participation health.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="overview-card">
            <h3>⚠️ Churn Risk</h3>
            <p>
            Detects bottlenecked players and early churn indicators to automatically execute targeted retention actions.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # -----------------------------------------------------
    # BUSINESS VALUE
    # -----------------------------------------------------

    st.subheader("💼 Business Value")

    st.markdown(
        """
        <div class="business-card">
        <p style="font-size:17px;">
        The project transforms raw gameplay metrics into <span style="color:#C084FC; font-weight:600;">actionable business intelligence</span>,
        empowering gaming studios to substitute static rules with data-driven dynamic game balancing.
        </p>

        <p style="font-size:17px;">
        Instead of uniform gameplay curves, studios deploy <span style="color:#C084FC; font-weight:600;">personalized player retention workflows</span>,
        proactively re-engaging churn-prone players while offering optimal challenges to hardcore gamers.
        </p>

        <p style="font-size:17px;">
        Ultimately, this AI engine boosts long-term LTV (Lifetime Value), reduces churn rate, and optimizes in-game monetization strategies.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # FOOTER
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="footer-text">
        🎮 Adaptive Balancing &nbsp; • &nbsp; 📊 Dynamic Analytics &nbsp; • &nbsp; 💡 Data-Driven Rules &nbsp; • &nbsp; 🚀 Churn Prevention
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# PROJECT DETAILS & ML APPROACH PAGE
# =========================================================

elif page == "📋 Project Details & ML":

    st.title("📋 Project Details & AI Architecture")
    st.write("An end-to-end technical overview of data engineering, machine learning modeling, and decision intelligence logic.")

    st.divider()

    # -----------------------------------------------------
    # 1. DATA OVERVIEW & 2. PREPROCESSING
    # -----------------------------------------------------

    col_a, col_b = st.columns(2, gap="medium")

    with col_a:
        st.markdown(
            """
            <div class="detail-box">
            <h3>1. 📥 Dataset Overview</h3>
            <p><span style="color:#C084FC; font-weight:600;">Source:</span> Kaggle — <i>Online Gaming Behavior Insight</i></p>
            <ul>
                <li><span style="color:#E9D5FF; font-weight:600;">Dataset Shape:</span> 40,034 rows × 15 columns (PlayerID dropped during training)</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Data Quality:</span> 0 missing values; 0 duplicate records</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Demographics:</span> Age (15–49), Gender (Male: 23.9k, Female: 16.0k)</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Gameplay Features:</span> PlayTimeHours (0–24h), SessionsPerWeek (0–19), AvgSessionDuration (10–179 mins), PlayerLevel (1–99), Achievements (0–49)</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(
            """
            <div class="detail-box">
            <h3>2. 🧹 Data Preparation & Validation</h3>
            <p><span style="color:#C084FC; font-weight:600;">Quality Mitigation & Pipeline:</span> Automated checks prior to model deployment.</p>
            <ul>
                <li><span style="color:#E9D5FF; font-weight:600;">Outlier Handling:</span> Addressed extreme max anomaly in <code>ProgressionSpeed</code> via IQR clipping.</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Categorical Encoding:</span> One-Hot Encoding (OHE) on nominal variables (<code>Gender</code>, <code>GameGenre</code>, <code>GameDifficulty</code>).</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Feature Scaling:</span> Standardized continuous numeric metrics for scale-sensitive estimators.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # 3. EDA & 4. FEATURE ENGINEERING
    # -----------------------------------------------------

    col_c, col_d = st.columns(2, gap="medium")

    with col_c:
        st.markdown(
            """
            <div class="detail-box">
            <h3>3. 🔍 Exploratory Data Analysis</h3>
            <p><span style="color:#C084FC; font-weight:600;">Key Findings:</span> Behavioral trends across genre and difficulty modes.</p>
            <ul>
                <li><span style="color:#E9D5FF; font-weight:600;">Genre Balance:</span> Distributed across Sports, Action, Strategy, Simulation, and RPG (~8,000 players per genre).</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Difficulty Base:</span> Easy (20,015), Medium (12,011), Hard (8,008).</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Monetization & Engagement:</span> Engagement Levels categorized into Medium (19,374), High (10,336), and Low (10,324).</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_d:
        st.markdown(
            """
            <div class="detail-box">
            <h3>4. ⚙️ Feature Engineering & Segmentation</h3>
            <ul>
                <li><span style="color:#E9D5FF; font-weight:600;">Churn Risk Definition:</span> Churn risk was calculated using sessions per week, playtime hours and achievements unlocked.</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Player Category Rule:</span> Derived from <code>PlayTimeHours</code> (&lt;10 Casual, 10–20 Moderate, &gt;20 Hardcore).</li>
                <li><span style="color:#E9D5FF; font-weight:600;">Recommended Action Logic:</span> Recommended action was calculated using player category and churn risk.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # -----------------------------------------------------
    # 5. TARGET CREATION
    # -----------------------------------------------------

    st.subheader("5. 🎯 Multi-Output Machine Learning Architecture")
    st.write("The system relies on coordinated multi-target classification layers combined with a deterministic decision matrix:")

    col_t1, col_t2, col_t3 = st.columns(3)

    with col_t1:
        st.markdown(
            """
            <div class="overview-card">
            <h3>📊 Player Category</h3>
            <p><span style="color:#C084FC; font-weight:600;">Type:</span> Multi-class Classification</p>
            <p>Predicts behavioral archetypes (Casual, Moderate, Hardcore) to tailor UI and challenge pacing.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_t2:
        st.markdown(
            """
            <div class="overview-card">
            <h3>⚠️ Churn Risk</h3>
            <p><span style="color:#C084FC; font-weight:600;">Type:</span> Binary Classification</p>
            <p>Identifies players exhibiting elevated churn risks (High Risk vs. Low Risk) based on engagement thresholds.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_t3:
        st.markdown(
            """
            <div class="overview-card">
            <h3>💡 Recommended Action</h3>
            <p><span style="color:#C084FC; font-weight:600;">Type:</span> Decision Intelligence Matrix</p>
            <p>Maps predicted <code>(PlayerCategory, ChurnRisk)</code> combinations directly into operational retention workflows.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # -----------------------------------------------------
    # 6. MODEL DEVELOPMENT
    # -----------------------------------------------------

    st.subheader("6. 🤖 Model Development & Selection")

    st.markdown(
        """
        <div class="detail-box">
        <h4>Algorithm Selection & Architecture</h4>
        <p>Evaluated ensemble algorithms across multi-output targets using Stratified 5-Fold Cross-Validation.</p>
        <ul>
            <li><span style="color:#E9D5FF; font-weight:600;">Player Category Target:</span> <code>Random Forest Classifier</code> utilized for reliable multi-class separation across playtime distributions.</li>
            <li><span style="color:#E9D5FF; font-weight:600;">Churn Risk Target:</span> <code>XGBoost Classifier</code> trained on feature interactions across activity frequency, achievement velocity, and total playtime.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # -----------------------------------------------------
    # 7. RECOMMENDED ACTION MATRIX
    # -----------------------------------------------------

    st.subheader("7. 💡 Decision Rule Matrix (6 Combinations)")

    matrix_data = [
        ("Casual", "High Risk", "Retention Campaign", "Trigger re-engagement push notifications, free gift bundles, and easier starter quests to lower churn risk."),
        ("Casual", "Low Risk", "Improve Engagement", "Introduce beginner-friendly events, guided tutorials, and cosmetic progression rewards."),
        ("Moderate", "High Risk", "Retention Campaign", "Offer limited-time battle passes, social guild invitations, and targeted in-game discounts."),
        ("Moderate", "Low Risk", "Maintain Difficulty", "Maintain existing progression pacing and dynamic difficulty settings."),
        ("Hardcore", "High Risk", "Retention Campaign", "Provide high-tier VIP rewards, exclusive leaderboard access, and priority support."),
        ("Hardcore", "Low Risk", "Increase Difficulty", "Unlock nightmare difficulties, end-game raid encounters, and competitive ladder seasons.")
    ]

    for cat, risk, act, desc in matrix_data:
        r_badge = "badge-high" if "High" in risk else "badge-low"
        st.markdown(
            f"""
            <div style="background:#28143F; border:1px solid #4A2A68; border-radius:10px; padding:15px; margin-bottom:10px;">
                <span class="rule-badge badge-action">👤 {cat}</span>
                <span style="color:#A78BFA; margin:0 8px;">+</span>
                <span class="rule-badge {r_badge}">⚠️ {risk}</span>
                <span style="color:#A78BFA; margin:0 8px;">➔</span>
                <span style="color:#FFFFFF; font-size:16px; font-weight:600;">💡 {act}</span>
                <p style="margin-top:8px; margin-bottom:0px; font-size:14px; color:#D6C7E8;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PREDICTION SYSTEM PAGE
# =========================================================

elif page == "🔮 Prediction System":

    st.title("🔮 Player Prediction System")

    # Top Disclaimer Box
    st.markdown(
        """
        <div class="disclaimer-box">
            <b>Disclaimer:</b> This application provides AI-generated predictions for informational purposes only. Predictions are not guaranteed facts or outcomes. Please independently verify all outputs before making critical decisions.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # -----------------------------------------------------
    # INPUTS (EVENLY ALIGNED 5/5 SPLIT)
    # -----------------------------------------------------

    st.subheader("👤 Player Profile")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=15, max_value=50, value=25)
        gender = st.selectbox("👤 Gender", ["Male", "Female"])
        game_genre = st.selectbox("🎮 Game Genre", ["Action", "RPG", "Simulation", "Sports", "Strategy"])
        game_difficulty = st.selectbox("🎯 Game Difficulty", ["Easy", "Medium", "Hard"])
        purchases = st.selectbox("🛍️ In-Game Purchases Made?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

    with col2:
        playtime_hours = st.number_input("⏱️ Total Playtime (Hours)", min_value=0.0, max_value=24.0, value=12.0)
        sessions = st.number_input("📅 Sessions Per Week", min_value=0, max_value=20, value=5)
        session_duration = st.number_input("⏳ Avg Session Duration (Mins)", min_value=10, max_value=180, value=45)
        player_level = st.number_input("🏆 Player Level", min_value=1, max_value=99, value=15)
        achievements = st.number_input("🏅 Achievements Unlocked", min_value=0, max_value=50, value=10)

    st.divider()

    # -----------------------------------------------------
    # PREDICTION EXECUTION
    # -----------------------------------------------------

    if st.button("Predict", type="primary"):

        payload = {
            "Age": age,
            "Gender": gender,
            "GameGenre": game_genre,
            "PlayTimeHours": playtime_hours,
            "InGamePurchases": purchases,
            "GameDifficulty": game_difficulty,
            "SessionsPerWeek": sessions,
            "AvgSessionDurationMinutes": session_duration,
            "PlayerLevel": player_level,
            "AchievementsUnlocked": achievements
        }

        try:
            with st.spinner("🔄 Communicating with FastAPI Prediction Microservice..."):
                response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=5)

            if response.status_code == 200:
                result = response.json()
                st.success("✅ Inference completed successfully!")

                player_category = result.get("PlayerCategory", "Casual")
                churn_risk = result.get("ChurnRisk", "Low Risk")
                action = recommended_action_rules.get((player_category, churn_risk), "Maintain Difficulty")

                st.subheader("📊 Model Output & Recommendations")

                col_res1, col_res2, col_res3 = st.columns(3)
                with col_res1:
                    st.metric("👤 Player Category", player_category)
                with col_res2:
                    st.metric("⚠️ Churn Risk", churn_risk)
                with col_res3:
                    st.markdown(
                        f"""
                        <div class="action-box">
                            <div class="action-label">💡 Recommended Action</div>
                            <div class="action-value">{action}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:
                st.error(f"❌ API returned status code {response.status_code}: {response.text}")

        except requests.exceptions.ConnectionError:
            # Local Offline Fallback Mode
            if playtime_hours < 10:
                simulated_cat = "Casual"
            elif 10 <= playtime_hours <= 20:
                simulated_cat = "Moderate"
            else:
                simulated_cat = "Hardcore"

            # Local Churn Risk Evaluation Fallback
            churn_condition = (sessions < 2) and (playtime_hours < 1.5) and (achievements < 20)
            simulated_churn = "High Risk" if churn_condition else "Low Risk"

            simulated_action = recommended_action_rules.get((simulated_cat, simulated_churn), "Maintain Difficulty")

            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("👤 Player Category", simulated_cat)
            with col_res2:
                st.metric("⚠️ Churn Risk", simulated_churn)
            with col_res3:
                st.markdown(
                    f"""
                    <div class="action-box">
                        <div class="action-label">💡 Recommended Action</div>
                        <div class="action-value">{simulated_action}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error(f"⚠️ An unexpected evaluation error occurred: {e}")
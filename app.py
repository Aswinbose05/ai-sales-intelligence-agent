import streamlit as st
import pandas as pd

from src.ranking.scoring_agent import ScoringAgent


st.set_page_config(
    page_title="AI Sales Intelligence",
    page_icon="🤖",
    layout="wide"
)

scorer = ScoringAgent()

ranked = scorer.rank_companies()

# =========================
# Sidebar
# =========================

st.sidebar.title("🤖 AI Sales Intelligence")

page = st.sidebar.radio(

    "Navigation",

    [
        "Dashboard",
        "Rankings",
        "Company Details",
        "Reports"
    ]
)

# =========================
# Dashboard
# =========================

if page == "Dashboard":

    st.title("🤖 AI Sales Intelligence Dashboard")

    total_companies = len(ranked)

    total_signals = sum(len(x["signals"]) for x in ranked)

    highest_score = max(x["score"] for x in ranked)

    c1, c2, c3 = st.columns(3)

    c1.metric("Companies", total_companies)

    c2.metric("Signals", total_signals)

    c3.metric("Highest Score", highest_score)

    st.divider()

    df = pd.DataFrame(ranked)

    df["signals"] = df["signals"].apply(
        lambda x: ", ".join(x)
    )

    st.dataframe(df, use_container_width=True)

# =========================
# Rankings
# =========================

elif page == "Rankings":

    st.title("🏆 Company Rankings")

    df = pd.DataFrame(ranked)

    df["signals"] = df["signals"].apply(
        lambda x: ", ".join(x)
    )

    st.dataframe(df, use_container_width=True)

# =========================
# Company Details
# =========================

elif page == "Company Details":

    st.title("🏢 Company Details")

    company = st.selectbox(

        "Choose Company",

        [x["company"] for x in ranked]

    )

    info = scorer.get_company_details(company)

    score = next(
        x["score"]
        for x in ranked
        if x["company"] == company
    )

    confidence = next(
        x["confidence"]
        for x in ranked
        if x["company"] == company
    )

    st.metric("Intent Score", score)

    st.metric("Confidence", confidence)

    st.subheader("Signals")

    for item in info:

        st.success(item["signal"])

        st.write("Evidence:")

        st.info(item["evidence"])

        st.write("---")

# =========================
# Reports
# =========================

elif page == "Reports":

    st.title("📊 Reports")

    df = pd.DataFrame(ranked)

    df["signals"] = df["signals"].apply(
        lambda x: ", ".join(x)
    )

    st.download_button(

        "⬇ Download Ranking CSV",

        df.to_csv(index=False),

        file_name="ranked_companies.csv",

        mime="text/csv"

    )

    st.dataframe(df)

scorer.close()
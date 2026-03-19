import streamlit as st
import pandas as pd
import urllib.parse

# --- UI CONFIG ---
st.set_page_config(page_title="SmartFetcher | Universal Hub", layout="wide", page_icon="🌐")

# Professional Lead Analyst Styling
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; background-color: #004a99; color: white; height: 3.5em; font-weight: bold; border-radius: 8px; }
    .stDataFrame { border: 1px solid #e6e9ef; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 SmartFetcher Universal")
st.write("#### Global Opportunity Aggregator")

# --- SEARCH ENGINE ---
col1, col2 = st.columns([3, 1])

with col1:
    user_query = st.text_input("Search for any Role, Skill, or Project:", placeholder="e.g. Oracle Financials, Solar Engineer, IGCSE Tutor...")
with col2:
    platform = st.selectbox("Source Platform", ["All Platforms", "Upwork", "LinkedIn", "Indeed", "Freelancer"])

# --- DIRECT LINK GENERATOR ---
def get_universal_links(query, site):
    encoded = urllib.parse.quote(query)
    
    sources = [
        {"Source": "Upwork", "Target": f"{query} Gigs", "Link": f"https://www.upwork.com/nx/search/jobs/?q={encoded}&sort=recency"},
        {"Source": "LinkedIn", "Target": f"{query} Roles", "Link": f"https://www.linkedin.com/jobs/search/?keywords={encoded}"},
        {"Source": "Indeed", "Target": f"Remote {query} Jobs", "Link": f"https://www.indeed.com/jobs?q={encoded}&l=Remote"},
        {"Source": "Freelancer", "Target": f"{query} Projects", "Link": f"https://www.freelancer.com/jobs/?keyword={encoded}"}
    ]
    
    if site == "All Platforms":
        return pd.DataFrame(sources)
    return pd.DataFrame([s for s in sources if s["Source"] == site])

# --- EXECUTION ---
if st.button("🚀 FETCH DIRECT OPPORTUNITIES"):
    if user_query:
        with st.spinner(f"Routing to global nodes for '{user_query}'..."):
            results = get_universal_links(user_query, platform)
            
            # Display using LinkColumn for one-click access
            st.data_editor(
                results,
                column_config={
                    "Link": st.column_config.LinkColumn("Action", display_text="Open Opportunity ↗️"),
                    "Source": st.column_config.TextColumn("Platform", width="medium"),
                },
                use_container_width=True,
                hide_index=True,
            )
            st.toast(f"Links generated for {user_query}")
    else:
        st.error("Please enter a search term.")

st.divider()
st.caption("SmartFetcher Project | Phase 2 Deployment Active")

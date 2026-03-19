import streamlit as st
import pandas as pd
from datetime import datetime

# --- UI CONFIG ---
st.set_page_config(page_title="SmartFetcher | Global Aggregator", layout="wide")

# Custom Styling for the Tables
st.markdown("""
    <style>
    .portal-header { background-color: #f1f3f4; padding: 10px; border-radius: 5px; margin-bottom: 10px; font-weight: bold; }
    .job-count { color: #1a73e8; font-size: 1.2em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 SmartFetcher Universal Aggregator")

# --- USER INPUT ---
user_query = st.text_input("Enter Search Criteria:", placeholder="e.g. Oracle SOX Auditor, Solar Energy Consultant...")

# --- DATA ENGINE (PHASE 3: MOCK -> LIVE) ---
def fetch_portal_data(portal_name, query):
    # This represents the structure we will get from the APIs
    # Columns: Name of JOB, Name of Company, Job details, Posted On, Part Time/Full Time
    mock_data = [
        {"Name of JOB": f"Senior {query}", "Name of Company": "Global Corp", "Job details": "Expert level required...", "Posted on": "2026-03-18", "Type": "Full Time", "Link": "#"},
        {"Name of JOB": f"Junior {query}", "Name of Company": "Startup Inc", "Job details": "Great for early career...", "Posted on": "2026-03-19", "Type": "Part Time", "Link": "#"},
        {"Name of JOB": f"{query} Consultant", "Name of Company": "Advisory LLP", "Job details": "Remote project based...", "Posted on": "2026-03-17", "Type": "Contract", "Link": "#"},
        {"Name of JOB": f"Lead {query}", "Name of Company": "Tech Giants", "Job details": "Leading a team of 5...", "Posted on": "2026-03-19", "Type": "Full Time", "Link": "#"},
        {"Name of JOB": f"Specialist: {query}", "Name of Company": "Boutique Firm", "Job details": "Specific niche focus...", "Posted on": "2026-03-15", "Type": "Full Time", "Link": "#"},
    ]
    return 120, pd.DataFrame(mock_data) # Returns (Count, Top 5 DF)

# --- EXECUTION ---
if st.button("🚀 EXECUTE GLOBAL SEARCH"):
    if user_query:
        portals = ["Upwork", "LinkedIn", "Indeed", "Freelancer"]
        
        for portal in portals:
            count, df = fetch_portal_data(portal, user_query)
            
            # --- PORTAL HEADER & COUNT ---
            st.markdown(f"""
                <div class="portal-header">
                    {portal} Portal | <span class="job-count">{count}+ Jobs Found</span>
                </div>
            """, unsafe_allow_html=True)
            
            # --- TOP 5 TABLE ---
            st.write(f"Showing Top 5 results for: **{user_query}**")
            
            # Convert all object/complex columns to strings to prevent type incompatibility
            df = df.copy()
            for col in df.columns:
                if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
                    df[col] = df[col].astype(str)
        
            st.data_editor(
                df,
                column_config={
                    "Link": st.column_config.LinkColumn("Apply", display_text="View ↗️"),
                    "Posted on": st.column_config.DateColumn("Date"),
                    "Job details": st.column_config.TextColumn("Description", width="large"),
                },
                use_container_width=True,
                hide_index=True,
                key=f"table_{portal}"
            )
            st.divider()
    else:
        st.warning("Please enter a search criteria to start the fetch.")

st.caption("© 2026 SmartFetcher | Phase 3 UI Deployment")

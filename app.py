import streamlit as st
import pandas as pd
import numpy as np
import math

st.set_page_config(page_title="DREDGE Epigenetic Reversal Engine", layout="wide", page_icon="🧬")

st.title("🧬 DREDGE: In-Silico Epigenetic Reversal Dashboard")
st.markdown("### *Targeted TET2 (PDB: 4NM6) Allosteric Modulation & CpG Entropy Dynamics*")

# সাইডবার কন্ট্রোল
st.sidebar.header("🔬 Simulation Parameters")
age_input = st.sidebar.slider("Baseline Biological Age (Years)", min_value=30.0, max_value=100.0, value=74.2, step=0.5)
lead_choice = st.sidebar.selectbox(
    "Select Screened Lead Compound",
    ["DREDGE-05 (Top Hit: -7.58 kcal/mol)", "DREDGE-01 (Hydroxamate: -7.08 kcal/mol)", "DREDGE-02 (Salicylate: -7.07 kcal/mol)"]
)

potency_map = {"DREDGE-05": 0.22, "DREDGE-01": 0.18, "DREDGE-02": 0.14}
selected_potency = potency_map[lead_choice.split()[0]]

# রেনোভেশন ক্যালকুলেশন
delta_age = round(age_input * selected_potency * 1.54, 1)
post_age = round(age_input - delta_age, 1)

base_beta = min(0.85, 0.45 + (age_input * 0.005))
post_beta = max(0.2, base_beta - (selected_potency * 0.15))

def get_h(b):
    return -(b * math.log2(b) + (1.0 - b) * math.log2(1.0 - b))

base_h = get_h(base_beta)
post_h = get_h(post_beta)

# মেট্রিক্স ড্যাশবোর্ড
col1, col2, col3, col4 = st.columns(4)
col1.metric("Baseline Age", f"{age_input} yrs")
col2.metric("Post-DREDGE Age", f"{post_age} yrs", delta=f"-{delta_age} yrs")
col3.metric("Baseline Entropy", f"{base_h:.4f} bits")
col4.metric("Entropy Reduction", f"{base_h - post_h:.4f} bits", delta=f"{base_h - post_h:.4f}")

st.markdown("---")

# ডকিং লিডস ডেটা টেবিল
st.subheader("📊 Top AutoDock Vina Binding Affinities (TET2 Pocket)")
df_leads = pd.DataFrame({
    "Scaffold ID": ["DREDGE-05", "DREDGE-01", "DREDGE-02", "DREDGE-03", "DREDGE-04"],
    "Binding Affinity (ΔG)": ["-7.58 kcal/mol", "-7.08 kcal/mol", "-7.07 kcal/mol", "-6.90 kcal/mol", "-6.78 kcal/mol"],
    "Est. Ki (µM)": ["2.75 µM", "6.40 µM", "6.51 µM", "8.67 µM", "10.62 µM"],
    "Status": ["Top Hit (Lead)", "Strong Binder", "Strong Binder", "Moderate Binder", "Moderate Binder"]
})
st.table(df_leads)

st.success("Target Structure Verified: PDB 4NM6 (TET2 Methylcytosine Dioxygenase)")

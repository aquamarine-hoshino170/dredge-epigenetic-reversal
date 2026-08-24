import sys

try:
    import streamlit as st
except ImportError:
    print("\n[!] Streamlit is required to launch the interactive UI.")
    print("[*] Install it using: pip install 'aquamarine-dredge[ui]' or pip install streamlit\n")
    sys.exit(1)

st.set_page_config(page_title="DREDGE Epigenetic Reversal Engine", layout="wide")
st.title("🧬 Aquamarine DREDGE: In-Silico TET2 Modulation")
st.write("Welcome to the interactive interface for Epigenetic Entropy Reversal.")

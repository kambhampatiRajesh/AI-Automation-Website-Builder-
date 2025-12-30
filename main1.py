import streamlit as st
import os
import zipfile
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(
    page_title="AI Automation Website Builder",
    page_icon="🤖",
    layout="wide"
)

# UI Styling (only for Streamlit app, not website output)
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 30px;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    color: white;
}
.subtitle {
    text-align: center;
    color: #cbd5f5;
    margin-bottom: 30px;
}
.stTextArea textarea {
    background-color: white !important;
    font-size: 16px;
    border-radius: 8px;
}
.stButton>button {
    background-color: #38bdf8 !important;
    color: black !important;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 10px;
    font-weight: bold;
}
.stDownloadButton>button {
    background-color: #22c55e !important;
    color: black !important;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>AI Automation Website Creation</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Describe your website — AI will build it</div>", unsafe_allow_html=True)

prompt = st.text_area("📌 Paste your website prompt below:", height=300)

if st.button("Generate Website"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Creating your website using AI..."):
            
            system_message = """
You are an expert frontend web developer.

Create a PROFESSIONAL, MODERN, VISUALLY RICH frontend website.

MANDATORY RULES:
- Do NOT generate plain HTML
- Use modern professional color themes (NOT purple gradient)
- Use flat design (NO curves, NO waves, NO circles)
- Use cards with shadows
- Use buttons instead of links
- Fully responsive layout
- Clean typography using Google Fonts
- Smooth hover effects

Generate HTML, CSS, and JavaScript.

STRICT OUTPUT FORMAT:

--html--
[HTML CODE]
--html--

--css--
[CSS CODE]
--css--

--js--
[JAVASCRIPT CODE]
--js--
"""

            messages = [
                ("system", system_message),
                ("user", prompt)
            ]

            model = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash-lite",
                temperature=0.6
            )

            response = model.invoke(messages)
            content = response.content

            try:
                html_code = content.split("--html--")[1].split("--html--")[0].strip()
                css_code = content.split("--css--")[1].split("--css--")[0].strip()
                js_code = content.split("--js--")[1].split("--js--")[0].strip()

                with open("index.html", "w", encoding="utf-8") as f:
                    f.write(html_code)

                with open("style.css", "w", encoding="utf-8") as f:
                    f.write(css_code)

                with open("script.js", "w", encoding="utf-8") as f:
                    f.write(js_code)

                with zipfile.ZipFile("website.zip", "w") as zipf:
                    zipf.write("index.html")
                    zipf.write("style.css")
                    zipf.write("script.js")

                st.success("✅ Website generated successfully!")

                st.download_button(
                    "⬇️ Download Website ZIP",
                    data=open("website.zip", "rb"),
                    file_name="website.zip"
                )

            except:
                st.error("AI output format error. Please generate again.")
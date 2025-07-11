import streamlit as st

st.set_page_config(page_title="Flan Caramel – Video AI Tool", layout="centered")

st.title("🎬 Flan Caramel – Video AI Agent")
st.subheader("Prototype: klantanalyse, videostrategie en script/storyboard")

# Input
url = st.text_input("🌐 Website van de klant:", "https://www.academiclabs.com")
video_type = st.selectbox("🎯 Kies een videotype:", [
    "Explainer Video",
    "Testimonial",
    "Productdemo",
    "Employer Branding",
    "Brand Awareness"
])
cta = st.text_input("📣 Call-to-Action:", "Discover how we can help you connect with the right researchers")

if st.button("🔍 Genereer AI-output"):

    # Analyse (placeholder op basis van Academic Labs)
    st.markdown("## 📊 Analyse")
    st.markdown(f"""
    **Marketingdoelstellingen:**  
    - Leadgeneratie in biotech/farma  
    - Thought leadership binnen academische innovatie  
    - Branding als R&D-partner

    **Tone of Voice:**  
    Professioneel, toegankelijk, helder

    **Huisstijl:**  
    Blauw (#005C97), wit, tech visuals  
    """)

    # Strategie
    st.markdown("## 🎥 Videostrategie")
    st.markdown(f"""
    **Videotype:** {video_type}  
    **Duur:** 60–90 sec  
    **Distributiekanalen:** LinkedIn, YouTube  
    **Stijl:** Visueel, professioneel, helder  
    **Call-to-Action:** {cta}
    """)

    # Script
    st.markdown("## ✍️ Script (voice-over)")
    script = f"""
[INTRO – LOGO & MUZIEK]  
"Innovation doesn’t happen in isolation. It happens when ideas connect."

[SCÈNE 1 – PROBLEEM]  
"Companies in biotech, pharma, and tech often struggle to find the right academic experts to collaborate with."

[SCÈNE 2 – DE OPLOSSING]  
"{url} is the matchmaking platform between industry and research. We help you find, evaluate, and contact academic partners – faster."

[SCÈNE 3 – WERKING]  
"With intelligent search and up-to-date profiles, you’ll discover exactly who to talk to – in minutes."

[SCÈNE 4 – USP]  
"Save time, reduce risk, and unlock your R&D potential with trusted academic partners."

[SCÈNE 5 – CTA]  
"{cta}"
"""
    st.code(script, language="markdown")

    # Storyboard
    st.markdown("## 🧾 Storyboard")
    st.markdown("""
| SCÈNE       | BEELD                         | VOICE-OVER                                             | DUUR |
|-------------|-------------------------------|--------------------------------------------------------|------|
| Intro       | Logo + muziek                 | Innovation doesn’t happen in isolation...             | 4s   |
| Probleem    | Zoekende bedrijven            | ...struggle to find the right academic experts...     | 8s   |
| Oplossing   | Platform in actie             | ...the matchmaking platform between industry...       | 10s  |
| Werking     | Zoekopdracht + matching       | With intelligent search...                            | 10s  |
| USP         | Resultaten, impact            | Save time, reduce risk...                             | 8s   |
| CTA         | Logo + tagline                | Your research partner network...                      | 6s   |
""")

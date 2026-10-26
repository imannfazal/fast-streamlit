import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Student Predictor",
    page_icon="■",
    layout="centered"
)

st.title("■ Student Pass / Fail Predictor")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider("Study Hours Per Day", 0.0, 10.0, 4.0, 0.5)

with col2:
    prev_score = st.slider("Previous Exam Score", 0.0, 100.0, 60.0, 1.0)

st.markdown("---")

if st.button("■ Predict Result", use_container_width=True):
    res = requests.post(
        f"{API_URL}/predict",
        json={"study_hours": study_hours, "prev_score": prev_score}
    )

    if res.status_code == 200:
        r = res.json()

        if r["prediction"] == 1:
            st.success(f"■ Result: **{r['result_label']}**")
        else:
            st.error(f"■ Result: **{r['result_label']}**")

        st.metric("Confidence", f"{r['confidence']*100:.1f}%")

        with st.expander("Raw API response"):
            st.json(r)

    else:
        st.error("API not reachable — is FastAPI running?")

st.markdown("---")

c1, c2 = st.columns(2)

c1.metric("Study Hours", f"{study_hours} hrs/day")
c2.metric("Previous Score", f"{prev_score}/100")
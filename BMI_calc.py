import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")
st.markdown(
    """
    <h1 style="display:inline-flex; align-items: center;">
    BMI Calculator
    <img src="https://cdn-icons-png.flaticon.com/512/10481/10481308.png" width="60" style="vertical-align: middle; margin-left: 10px;">
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown("Calculate your Body Mass Index (BMI) to assess your health status.")

# --- Weight Input ---
weight_unit = st.selectbox("Select weight unit:", ["Kilograms", "Grams"])
if weight_unit == "Kilograms":
    weight_input = st.text_input("Enter weight in Kilograms (kg):", placeholder="e.g. 70")
elif weight_unit == "Grams":
    weight_input = st.text_input("Enter weight in Grams (g):", placeholder="e.g. 70000")

# --- Height Input ---
height_unit = st.selectbox("Select height unit:", ["Meters", "Centimeters", "Feet"])
if height_unit == "Meters":
    height_input = st.text_input("Enter height in Meters (m):", placeholder="e.g. 1.75")
elif height_unit == "Centimeters":
    height_input = st.text_input("Enter height in Centimeters (cm):", placeholder="e.g. 175")
elif height_unit == "Feet":
    height_input = st.text_input("Enter height in Feet (ft):", placeholder="e.g. 5.7")

# --- BMI Calculation ---
if st.button("Calculate BMI"):
    if weight_input and height_input:
        try:
            weight = float(weight_input)
            height = float(height_input)

            # Convert units
            if weight_unit == "Grams":
                weight = weight / 1000
            if height_unit == "Centimeters":
                height = height / 100
            elif height_unit == "Feet":
                height = height * 0.3048

            bmi = round(weight / (height ** 2), 2)

            st.write(f"**Weight in kg:** {weight:.2f}")
            st.write(f"**Height in meters:** {height:.2f}")
            st.success(f"Your BMI is: {bmi} kg/m²")

            # Category
            if bmi < 18.5:
                st.warning("⚠️ You are underweight. Consider a balanced diet to gain weight.")
            elif bmi < 25:
                st.success("✅ You have a normal weight. Keep up the good work!")
            elif bmi < 30:
                st.error("⚠️ You are overweight. Try regular exercise and healthy eating.")
            else:
                st.error("❗ You are obese. It is advisable to consult a doctor for health guidance.")
        except ValueError:
            st.error("Please enter valid numeric values for weight and height.")
    else:
        st.warning("Please fill in both weight and height fields.")

 # Footer
st.markdown("---")
st.markdown("<center>© 2025 BMI calculator Pvt. Ltd. | Powered by Amaan Ahmad</center>", unsafe_allow_html=True)



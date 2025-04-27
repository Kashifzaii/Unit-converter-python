import streamlit as st

# Title and description with some styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌎Super Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Converts Length, Weight, and Time Instantly</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px;'>Welcome! Select a category, enter a value, and get the converted result in real-time.</p>", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

# Select category with custom background color and styling
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"], index=0)

# Select conversion type based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

# Get value input from user with some added styling
value = st.number_input("Enter the value to convert", min_value=0.0, step=0.1, format="%.2f", label_visibility="collapsed")

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    return None  # If no valid conversion is found

# Add a custom button style
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        width: 200px;
        margin-top: 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# Convert button with custom styling
if st.button("Convert"):
    result = convert_units(category, value, unit)

    # Display the result with success or error message
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion! Please select a valid option.")

# Footer with custom text
st.markdown("""
    <p style="text-align: center; color: gray; font-size: 14px;">Unit Converter App - Powered by Streamlit</p>
""", unsafe_allow_html=True)


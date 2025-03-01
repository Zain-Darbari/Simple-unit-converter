import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f4f4;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 18px;
        }
        .stSelectbox, .stNumberInput {
            background-color: white;
            color: black;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Simple Unit Converter</h1>", unsafe_allow_html=True)

def length_converter(value, from_unit, to_unit):
    conversion_factors = {'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084, 'inches': 39.3701}
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {'grams': 1, 'kilograms': 0.001, 'pounds': 0.00220462, 'ounces': 0.035274}
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == 'Celsius': return value * 9/5 + 32 if to_unit == 'Fahrenheit' else value + 273.15
    if from_unit == 'Fahrenheit': return (value - 32) * 5/9 if to_unit == 'Celsius' else (value - 32) * 5/9 + 273.15
    if from_unit == 'Kelvin': return value - 273.15 if to_unit == 'Celsius' else (value - 273.15) * 9/5 + 32

option = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if option == "Length":
    units = ['meters', 'kilometers', 'miles', 'feet', 'inches']
    value = st.number_input("Enter value", value=0.0)
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    if st.button("Convert"):
        st.success(f"{value} {from_unit} = {length_converter(value, from_unit, to_unit)} {to_unit}")

elif option == "Weight":
    units = ['grams', 'kilograms', 'pounds', 'ounces']
    value = st.number_input("Enter value", value=0.0)
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    if st.button("Convert"):
        st.success(f"{value} {from_unit} = {weight_converter(value, from_unit, to_unit)} {to_unit}")

elif option == "Temperature":
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    value = st.number_input("Enter value", value=0.0)
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    if st.button("Convert"):
        st.success(f"{value} {from_unit} = {temperature_converter(value, from_unit, to_unit):.2f} {to_unit}")

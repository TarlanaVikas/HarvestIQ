import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title='HarvestIQ',
    page_icon='🌾',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.markdown('''
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --harvest-green: #6fca9b;
        --harvest-dark: #e8f0eb;
        --harvest-gold: #e1a642;
        --harvest-cream: #111a18;
        --harvest-muted: #a8bbb2;
        --harvest-panel: #1b2925;
        --harvest-panel-light: #243732;
    }

    .stApp {
        background: radial-gradient(circle at 85% 0%, #213d33 0%, transparent 32%),
                    linear-gradient(135deg, #101816 0%, #16231f 58%, #0d1412 100%);
        color: var(--harvest-dark);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid='stHeader'] {
        background: transparent;
    }

    [data-testid='stToolbar'] {
        color: var(--harvest-dark);
    }

    [data-testid='stAppViewContainer'],
    [data-testid='stMainBlockContainer'] {
        background: transparent;
    }

    [data-testid='stSidebar'] {
        background: #0b1210;
        border-right: 1px solid rgba(216, 155, 61, 0.35);
    }

    [data-testid='stSidebar'] * {
        color: #e8f0eb;
    }

    [data-testid='stSidebar'] .stSlider [data-baseweb='slider'] div,
    [data-testid='stSidebar'] .stSelectbox [data-baseweb='select'] > div {
        border-color: rgba(232, 240, 235, 0.28);
    }

    [data-testid='stSidebar'] .stSelectbox [data-baseweb='select'] > div {
        background: #ffffff;
    }

    [data-testid='stSidebar'] .stSelectbox [data-baseweb='select'] span,
    [data-testid='stSidebar'] .stSelectbox [data-baseweb='select'] input {
        color: #000000 !important;
    }

    [data-testid='stSidebar'] .stSelectbox [data-baseweb='select'] * {
        color: #000000 !important;
    }

    [data-testid='stSidebar'] .stSelectbox [data-baseweb='select'] input::placeholder {
        color: #000000 !important;
        opacity: 1;
    }

    [data-testid='stSidebar'] .stSlider [data-testid='stTickBar'] span,
    [data-testid='stSidebar'] .stSlider [data-testid='stSliderValue'] {
        color: #e8f0eb !important;
    }

    [data-baseweb='popover'],
    [data-baseweb='popover'] [role='listbox'],
    [data-baseweb='popover'] [role='option'] {
        background: #ffffff !important;
        color: #000000 !important;
    }

    [data-baseweb='popover'] [role='option'] span {
        color: #000000 !important;
    }

    [data-baseweb='popover'] [role='option']:hover {
        background: #e8f0eb !important;
    }

    [data-testid='stSidebar'] button {
        background: var(--harvest-gold);
        border: 0;
        color: #17211d;
        font-weight: 700;
        min-height: 2.8rem;
    }

    [data-testid='stSidebar'] button:hover {
        background: #e8b45c;
        color: #17211d;
    }

    h1, h2, h3, p, label, [data-testid='stMarkdownContainer'] {
        color: var(--harvest-dark);
    }

    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif;
        letter-spacing: 0;
    }

    .brand-kicker {
        color: #8ad8ae;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.16rem;
        margin-bottom: 0.35rem;
        text-transform: uppercase;
    }

    .brand-title {
        color: var(--harvest-dark);
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4.8rem);
        font-weight: 700;
        line-height: 0.98;
        margin: 0;
    }

    .brand-copy {
        color: var(--harvest-muted);
        font-size: 1.05rem;
        margin: 1rem 0 2rem;
        max-width: 46rem;
    }

    [data-testid='stMetric'] {
        background: rgba(27, 41, 37, 0.88);
        border: 1px solid rgba(111, 202, 155, 0.22);
        border-radius: 0.75rem;
        padding: 1rem;
    }

    [data-testid='stMetricValue'],
    [data-testid='stMetricLabel'] {
        color: var(--harvest-dark) !important;
    }

    .section-rule {
        border-top: 2px solid rgba(111, 202, 155, 0.22);
        margin: 2rem 0 1.5rem;
    }
</style>
''', unsafe_allow_html=True)

st.markdown("<div class='brand-kicker'>Agricultural intelligence platform</div>", unsafe_allow_html=True)
st.markdown("<h1 class='brand-title'>HarvestIQ</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='brand-copy'>Explore crop performance and make data-informed yield predictions across India's agricultural landscape.</p>",
    unsafe_allow_html=True
)

st.markdown("""
Welcome to the Crop Yield Prediction App! 
This tool uses a machine learning model to forecast agricultural output based on key factors. 
**Use the sidebar** on the left to input values and see the predicted yield.
""")

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the dataset to get the list of crops, seasons, and states for the dropdowns
df = pd.read_csv('crop_yield.csv')
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()


# --- Streamlit App ---

st.markdown("<div class='section-rule'></div>", unsafe_allow_html=True)
st.subheader('Yield prediction workspace')

# --- User Input in a Sidebar ---
st.sidebar.header('Input Features')

# Dropdowns for categorical features
crop = st.sidebar.selectbox('Crop', sorted(df['crop'].unique()))
season = st.sidebar.selectbox('Season', sorted(df['season'].unique()))
state = st.sidebar.selectbox('State', sorted(df['state'].unique()))

# Sliders for numerical features
crop_year = st.sidebar.slider('Crop Year', 1997, 2020, 2015)
area = st.sidebar.slider('Area (Hectares)', float(df['area'].min()), float(df['area'].max()), float(df['area'].mean()))
annual_rainfall = st.sidebar.slider('Annual Rainfall (mm)', float(df['annual_rainfall'].min()), float(df['annual_rainfall'].max()), float(df['annual_rainfall'].mean()))
fertilizer = st.sidebar.slider('Fertilizer (tonnes)', float(df['fertilizer'].min()), float(df['fertilizer'].max()), float(df['fertilizer'].mean()))
pesticide = st.sidebar.slider('Pesticide (tonnes)', float(df['pesticide'].min()), float(df['pesticide'].max()), float(df['pesticide'].mean()))


# --- Prediction ---
if st.sidebar.button('Predict Yield'):
    # Create a dataframe from user inputs
    input_data = pd.DataFrame({
        'crop': [crop],
        'crop_year': [crop_year],
        'season': [season],
        'state': [state],
        'area': [area],
        'annual_rainfall': [annual_rainfall],
        'fertilizer': [fertilizer],
        'pesticide': [pesticide]
    })

    # One-hot encode the categorical features
    # This should match the encoding used during model training
    input_data = pd.get_dummies(input_data, columns=['crop', 'season', 'state'])
    
    # Align the columns of the input data with the training data
    # Get the column names from the training data (X_train)
    # You would need to save these column names from your notebook
    # For now, we will create a placeholder. 
    # Replace this with the actual columns from your training data.
    train_cols = model.feature_names_ # Get columns from CatBoost
    input_data = input_data.reindex(columns=train_cols, fill_value=0)


    # Make prediction
    prediction = model.predict(input_data)

    st.subheader('Predicted Crop Yield')
    st.write(f'The predicted crop yield is **{prediction[0]:.2f} tonnes per hectare**.')


# --- Adding Visualizations to Streamlit app ---
st.header("HarvestIQ insights")

# Example of embedding a plot from your EDA
st.subheader("Average Yield Over Time")
avg_yield = df.groupby('crop_year')['yield'].mean()
st.line_chart(avg_yield)

# You can add more plots here, like the correlation heatmap or feature importance plot.
# For matplotlib/seaborn plots, you can use st.pyplot()

# correlation heatmap
st.subheader("Correlation Heatmap of Numerical Features")
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 

# This is the key line: it selects ONLY the number columns for the heatmap
numeric_df = df.select_dtypes(include=np.number)

fig, ax = plt.subplots(figsize=(10, 8))
# Notice we are now using numeric_df.corr() instead of df.corr()
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# --- Adding Visualizations to Streamlit app ---
st.header("HarvestIQ insights")

# (Keep your existing line chart and heatmap code here...)


# --- Feature Importance Plot ---
st.subheader("What Matters Most for Crop Yields?")

# Check if the model has the 'feature_importances_' attribute
if hasattr(model, 'feature_importances_'):
    # Create a dataframe for feature importances
    # The FIX is here: we use model.feature_names_
    feature_imp = pd.DataFrame(sorted(zip(model.feature_importances_, model.feature_names_)), columns=['Value','Feature'])

    # Create the plot
    fig_imp, ax_imp = plt.subplots(figsize=(10, 6))
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value", ascending=False), ax=ax_imp)
    ax_imp.set_title('Model Feature Importance')
    ax_imp.set_xlabel('Importance')
    ax_imp.set_ylabel('Features')
    st.pyplot(fig_imp)

    st.markdown("""
    This chart shows the most influential factors in our model's predictions. The factors at the top are the most important drivers of crop yield in this dataset.
    """)
else:
    st.write("The loaded model does not support feature importance.")
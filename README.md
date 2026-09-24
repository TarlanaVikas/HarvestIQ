![HarvestIQ](https://capsule-render.vercel.app/api?type=waving\&color=0:14532D,45:166534,100:22C55E\&height=210\&section=header\&text=HarvestIQ\&fontSize=52\&fontColor=FFFFFF\&animation=fadeIn\&fontAlignY=38)

<p align="center">
  <strong>Predict • Analyze • Visualize • Understand</strong>
</p>

<p align="center">
  A machine learning-based agricultural analytics platform for
  <br/>
  <strong>Crop Yield Prediction • Data Analysis • Geospatial Visualization</strong>
</p>

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Application-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CatBoost-ML-FFCC00?style=flat-square"/>
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat-square"/>
  <img src="https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=flat-square"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/GeoJSON-Geospatial-68B684?style=flat-square"/>
</p>

---

## ◈ The Platform

**HarvestIQ** is a machine learning-based agricultural analytics platform designed to analyze historical crop data, predict crop yield, and visualize agricultural information through an interactive web application.

The platform combines **machine learning, data analysis, and geospatial visualization** to provide an accessible interface for exploring crop yield patterns.

```text
                         HARVESTIQ
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
     CROP DATA          ML MODEL          GEO DATA
          │                  │                  │
          ▼                  ▼                  ▼
     DATA ANALYSIS      PREDICTION       MAP VISUALIZATION
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                    AGRICULTURAL INSIGHTS
```

---

# ✦ Platform Highlights

<table>
<tr>
<td width="50%">

### 🌾 Crop Yield Prediction

Predict crop yield using agricultural and environmental input parameters through a trained machine learning model.

</td>
<td width="50%">

### 📊 Data Visualization

Explore crop and agricultural data through interactive visualizations and analytical charts.

</td>
</tr>

<tr>
<td>

### 🗺️ Geospatial Visualization

Visualize crop-related information across Indian states using GeoJSON-based geographic data.

</td>
<td>

### 🤖 Machine Learning

Uses a pre-trained machine learning model to generate crop yield predictions without retraining during application execution.

</td>
</tr>

<tr>
<td>

### 📁 Historical Dataset

Analyze historical crop yield and agricultural information stored in a structured CSV dataset.

</td>
<td>

### 🖥️ Interactive Interface

A Streamlit-powered interface provides a simple way to interact with predictions and visualizations.

</td>
</tr>
</table>

---

# 🚀 Core Features

## 01 — Crop Yield Prediction

The prediction module allows users to provide agricultural parameters and obtain an estimated crop yield.

```text
Agricultural Inputs
        │
        ▼
   Input Processing
        │
        ▼
  Trained ML Model
     model.pkl
        │
        ▼
  Yield Prediction
```

Features include:

* Crop selection
* Agricultural input parameters
* Model-based prediction
* Instant prediction results
* Pre-trained model integration

---

## 02 — Agricultural Data Analysis

HarvestIQ uses historical agricultural data for exploratory analysis and visualization.

Key areas include:

* Crop-wise analysis
* State-wise analysis
* Agricultural input analysis
* Yield relationships
* Historical crop data exploration

---

## 03 — Geospatial Visualization

The platform includes geographic data for visualizing agricultural information across India.

```text
India Agricultural Data
          │
          ▼
    State Information
          │
          ▼
       GeoJSON
          │
          ▼
 Interactive Crop Map
          │
          ▼
Geospatial Visualization
```

The project includes:

* `india_states.geojson`
* `india_crop_map.html`
* State boundary data
* Geospatial visualization resources

---

## 04 — Machine Learning Pipeline

The model development workflow follows a standard machine learning process.

```text
Historical Crop Dataset
          │
          ▼
   Data Exploration
          │
          ▼
 Data Preprocessing
          │
          ▼
 Feature Selection
          │
          ▼
 Model Development
          │
          ▼
 Model Evaluation
          │
          ▼
    Trained Model
          │
          ▼
      model.pkl
          │
          ▼
 Streamlit Prediction
```

The project notebook contains the model development and data analysis workflow.

---

# 🧠 Machine Learning

The project uses regression-based machine learning techniques for crop yield prediction.

### Model Development

The notebook explores machine learning approaches including:

* CatBoost
* Random Forest
* XGBoost
* Scikit-learn utilities

The final trained model is stored as:

```text
model.pkl
```

This allows the deployed application to load the model directly instead of retraining every time the application starts.

---

# 📊 Data & Visualization

The project works with historical crop yield data stored in:

```text
crop_yield.csv
```

The dataset contains agricultural information that can be used to analyze relationships between crop production, environmental conditions, and agricultural inputs.

Visualization technologies include:

* Matplotlib
* Seaborn
* Streamlit visualizations
* HTML-based geospatial visualization
* GeoJSON geographic data

---

# 🗺️ Geospatial Mapping

HarvestIQ includes an interactive geographic visualization of Indian agricultural data.

### Geographic Resources

| File                               | Purpose                           |
| ---------------------------------- | --------------------------------- |
| `india_states.geojson`             | Indian state boundary information |
| `india_crop_map.html`              | Interactive crop map              |
| `ne_10m_admin_1_states_provinces/` | Geographic boundary dataset       |

These resources allow agricultural information to be represented geographically at the state level.

---

# 🧩 Technical Architecture

```text
┌───────────────────────────────────────────────┐
│                   USER LAYER                  │
│                                               │
│       Agricultural Data & Input Parameters    │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                 STREAMLIT UI                  │
│                                               │
│      Input • Prediction • Visualization       │
└───────────────────────┬───────────────────────┘
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
       Data Layer   Model Layer   Map Layer
            │           │           │
            ▼           ▼           ▼
      crop_yield.csv  model.pkl  GeoJSON
            │           │           │
            └───────────┼───────────┘
                        ▼
             Agricultural Insights
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
    Yield Prediction            Data Visualization
                                      │
                                      ▼
                              Geospatial Mapping
```

---

# 🛠️ Technology Stack

| Technology           | Role                                  |
| -------------------- | ------------------------------------- |
| **Python**           | Core programming language             |
| **Streamlit**        | Interactive web application           |
| **Pandas**           | Data processing and analysis          |
| **Scikit-learn**     | Machine learning                      |
| **CatBoost**         | Gradient boosting model               |
| **XGBoost**          | Machine learning experimentation      |
| **Random Forest**    | Regression experimentation            |
| **Matplotlib**       | Data visualization                    |
| **Seaborn**          | Statistical visualization             |
| **Jupyter Notebook** | Model development and experimentation |
| **Pickle**           | Trained model serialization           |
| **GeoJSON**          | Geographic data representation        |
| **HTML**             | Interactive map visualization         |

---

# 📁 Project Structure

```text
HarvestIQ/
│
├── ne_10m_admin_1_states_provinces/
│   └── Geographic boundary dataset

├── app.py
│   └── Streamlit application
│
├── code.ipynb
│   └── Data analysis and model development
│
├── crop_yield.csv
│   └── Crop yield dataset
│
├── india_crop_map.html
│   └── Interactive crop map
│
├── india_states.geojson
│   └── Indian state geographic data
│
├── model.pkl
│   └── Pre-trained ML model
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
```

---


# 🎯 Application Workflow

```text
Launch HarvestIQ
       │
       ▼
Enter Agricultural Parameters
       │
       ▼
Process Input Data
       │
       ▼
Load model.pkl
       │
       ▼
Generate Yield Prediction
       │
       ▼
Display Prediction
       │
       ▼
Explore Agricultural Data
       │
       ▼
Explore Geospatial Visualization
```

---


# 📌 Use Cases

HarvestIQ can be used for:

* Crop yield prediction
* Agricultural data analysis
* Machine learning education
* Agricultural visualization
* State-wise crop analysis
* Geospatial agricultural exploration
* Demonstrating ML model deployment

---

# 🔮 Future Enhancements

Potential improvements include:

* Real-time weather API integration
* Soil-quality parameters
* Additional crop features
* Advanced model optimization
* Time-series crop yield forecasting
* Crop-specific prediction models
* Interactive state-level dashboards
* Explainable AI using SHAP
* Real-time agricultural datasets
* Cloud-based model deployment

---

# 🤝 Contributing

Contributions are welcome.

```text
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Commit your changes
6. Submit a pull request
```


---

<p align="center">

### 🌾 HarvestIQ

<strong>Turning agricultural data into predictive insights.</strong>

<br/><br/>

Predict → Analyze → Visualize → Understand

<br/><br/>

⭐ If you find HarvestIQ useful, consider starring the repository!

</p>

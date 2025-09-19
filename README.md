# 🛍️ Sales Data Analysis - ABC Retail  

This project analyzes the **Sales Dataset** of **ABC Retail** to uncover insights into customer behavior, sales trends, and operational performance.  
The ultimate goal is to **optimize revenue, improve marketing strategies, and identify growth opportunities**.  

---

## 📂 Dataset  

The dataset contains both raw and engineered features:  

- **Order ID**: Unique identifier for each order  
- **Product**: Name of the product purchased  
- **Quantity Ordered**: Number of units sold  
- **Price Each**: Price per unit  
- **Order Date**: Timestamp of the order  
- **Purchase Address**: Customer shipping address  
- **Engineered Features**: Month, Sales, City, Hour, Weekday  

---

## 🔎 Exploratory Data Analysis (EDA)  

### 1. Univariate Analysis  
- Distribution of Sales  
- Orders by Month  
- Orders by Day of Week  

### 2. Bivariate Analysis  
- Total Sales by Month  
- Top 10 Best-Selling Products  
- Sales by City  
- Sales by Hour  

### 3. Multivariate Analysis  
- Sales by Month and City  
- Sales by Hour  

---

## 📊 Key Insights  

- **Peak Sales Hours**: Most purchases happen between **10 AM – 1 PM**.  
- **High-Performing Months**: **December** records the highest sales due to holiday shopping.  
- **City Insights**: **San Francisco and Los Angeles** contribute the most to overall revenue.  

---

## 🛠️ Tools & Technologies  

- **Python**: Data manipulation & visualization  
- **Pandas, Numpy**: Data wrangling  
- **Matplotlib, Seaborn**: Visualization  
- **Jupyter Notebook**: Interactive analysis  
- **Scikit-learn**: preprocessing, model evaluation
- **Statsmodels**: SARIMA
- **Keras/Tensorflow**: LSTM
- **Plotly**: (interactive chart)


---

## 📁 Project Structure  

```bash
Sales_Analysis/
│── data/             # Raw dataset
│── notebooks/        # Jupyter notebooks (EDA, Forecasting, etc.)
│── results/          # Exported plots & metrics
│── dashboard/        # Power BI or Streamlit dashboard
│── requirements.txt  # Python dependencies
└── README.md         # Project documentation

# How to Run
1. Clone this repository:
git clone https://github.com/your-username/Sales_EDA_Dashboard.git
cd Sales_EDA_Dashboard

2. Install dependencies
pip install -r requirements.txt

3. Open Jupyter Notebook
jupyter notebook

# Results
- Time series forecasting models have been implemented and evaluated, including:
  - **SARIMA(7)** and **SARIMA(30)**: capture trend and seasonality reasonably well but limited in modeling nonlinear patterns.
  - **LSTM (look_back=7)**: tends to predict around short-term averages, struggling with seasonal fluctuations.
  - **LSTM (look_back=30)**: shows better ability to follow long-term patterns compared to look_back=7, but still produces smoothed forecasts.
  - **Hybrid SARIMA + LSTM (Residual Learning)**: designed to combine SARIMA’s strength in linear trend/seasonality and LSTM’s ability to model nonlinear effects.  

- Comparative analysis (test set metrics):
  | Model                  | MAE       | RMSE      | MAPE   |
  |-------------------------|-----------|-----------|--------|
  | SARIMA                  | 16,521.6  | 19,369.2  | 14.0 % |
  | LSTM (autoregressive)   | 16,068.6  | 19,621.7  | 12.2 % |
  | Hybrid (SARIMA + LSTM)  | 16,624.8  | 19,408.0  | 13.9 % |

- Findings:
  - **SARIMA**: strong for capturing seasonality and trend.  
  - **LSTM**: outperforms SARIMA on MAPE, better at nonlinear patterns with longer look_back.  
  - **Hybrid SARIMA+LSTM**: did not outperform standalone models, since SARIMA residuals resembled white noise (no meaningful signal left for LSTM to learn).  

- Exported plots and comparison metrics are stored in the `results/` folder for further reference.

# Bussiness insight
- ABC Retail can increase staffing and marketing promotions during 10 AM – 1 PM to capture peak sales.
- Targeted campaigns in San Francisco & Los Angeles can maximize ROI since these cities dominate revenue.
- Holiday seasons, especially December, should be prioritized with inventory planning and bundled offers.
- More accurate forecasting models will allow ABC Retail to plan inventory and marketing campaigns with higher confidence.

# 💼 Business Value
Developed a sales forecasting system for retail, enabling **30-day ahead demand prediction** with ~14% MAPE.  
This system can help reduce stockouts and overstocking, allowing ABC Retail to save inventory costs, improve campaign planning, and optimize staffing levels.


# Next Steps
- **Focus on LSTM autoregressive**, as it achieved the best forecasting accuracy in this dataset.  
- Explore **ensemble averaging** between SARIMA and LSTM forecasts to reduce variance.  
- Optimize **look_back parameters (60–90 days)** and add **time-based features** (month, day of week, holidays).  
- Consider testing additional models (e.g., Prophet, XGBoost) for robustness.  
“Optimize look_back parameters (e.g., 60–90 days) and add time-based features (month, day of week, holidays).”

# Author
HaNguyenMinhTam - Data Analyst Enthusiast
- Email: hnmt@gmail.com
- Github: https://github.com/HaNguyenMinhTam




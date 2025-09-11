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

- Comparative analysis shows that:
  - **SARIMA** performs better at modeling seasonality and linear trends.
  - **LSTM** provides flexibility for nonlinear relationships but requires longer look_back windows and additional time-based features.
  - Both models have limitations when used independently, motivating exploration of hybrid approaches.

- Exported plots and comparison metrics are stored in the `results/` folder for further reference.

# Bussiness insight
- ABC Retail can increase staffing and marketing promotions during 10 AM – 1 PM to capture peak sales.
- Targeted campaigns in San Francisco & Los Angeles can maximize ROI since these cities dominate revenue.
- Holiday seasons, especially December, should be prioritized with inventory planning and bundled offers.
- More accurate forecasting models will allow ABC Retail to plan inventory and marketing campaigns with higher confidence.


# Next Steps 
“Explore hybrid models combining SARIMA and LSTM to leverage both linear and nonlinear patterns.”

“Optimize look_back parameters (e.g., 60–90 days) and add time-based features (month, day of week, holidays).”

# Author
HaNguyenMinhTam - Data Analyst Enthusiast
- Email: hnmt@gmail.com
- Github: https://github.com/HaNguyenMinhTam




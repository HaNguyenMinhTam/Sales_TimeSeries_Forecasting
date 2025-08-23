# Sales Data Analysis - ABC Retail
This project analyzes the Sales Dataset of ABC Retail to gain insights into customer behavior, sales trends, and operational performance.
The goal is to help the business optimize revenue, improve marketing strategies, and identify growth opportunities.

# Dataset
The Dataset includes:
- Order ID: Unique ID for each order
- Product: Name of the product purchased
- Quantity Ordered: Number of units sold
- Price Each: Price per unit
- Order Date: Timestamp of the order
- Purchase Address: Customer's shipping address
- Month, Sales, City, Hour, Weekday: Engineered features for analysis

# Exploratory Data Analysis (EDA)
The analysis is divided into 3 parts:
1. Univariate Analysis
- Distribution of Sales
- Number of Orders by Month
- Number of Orders by Day of Week

2. Bivariate Analysis
- Total Sales by Month
- Top 10 best-selling Products
- Sales by City
- Sales by Hour

3. Multivariate Analysis
- Sales by Month and City
- Sales by Hour

# Key insights
- Peak Sales Time: Most purchase happen between 10-13 PM.
- High Performing Months: December shows the highest sales due to holiday shopping.
- City Insight: San Francisco and Los Angeles contributes the most to overall revenue.

# Tools & Technologies
- Python: Data manipulation & visualization
- Pandas, Numpy: Data wrangling
- Matplotlib, Seaborn: Visualization
- Jupyter Notebook: Interactive analysis

# Project Structure
Sales_Analysis/
    - data/             # Raw dataset
    - notebooks/        # Jupyter notebooks (EDA.ipynb)
    - Dashboard/        # Saved Dashboard
    - README.md         # Project Documentation
    - requirements.txt  # Python dependencies

# How to Run
1. Clone this repository:
git clone https://github.com/your-username/Sales_EDA_Dashboard.git

2. Install dependencies
pip install -r requirements.txt

3. Open Jupyter Notebook
jupyter notebook

# Next Steps 
- Build time series forecasting model to predict sales.
- Develop a dashboard (Streamlit/Power BI) for interactive reporting.

# Author
HaNguyenMinhTam - Data Analyst Enthusiast
- Email: hnmt@gmail.com
- Github.




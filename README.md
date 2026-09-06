# Cart2Insights: Decoding E-Commerce Performance

## Project Overview

Cart2Insights is an e-commerce analytics project that analyzes customers, orders, products, sellers, payments, deliveries, and customer reviews to identify important business trends and performance patterns.

## Objectives

- Understand the structure and relationships of e-commerce datasets
- Perform data quality analysis and cleaning
- Store and analyze data using SQL
- Engineer useful business features
- Perform exploratory data analysis
- Conduct statistical hypothesis testing
- Build an interactive Streamlit dashboard
- Generate actionable business insights

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- SQLite
- SQL
- Streamlit
- GitHub

## Project Structure

Cart2Insights/

├── data/

│   ├── raw/

│   └── cleaned/

├── notebooks/

│   ├── 01_data_understanding.ipynb

│   ├── 02_data_quality_analysis.ipynb

│   ├── 03_data_cleaning.ipynb

│   ├── 04_sql_analysis.ipynb

│   ├── 05_feature_engineering.ipynb

│   ├── 06_eda.ipynb

│   └── 07_statistical_analysis.ipynb

├── streamlit/

│   ├── app.py

│   ├── database.py

│   ├── queries.py

│   └── utils.py

├── cart2insights.db

└── README.md

## Analysis Performed

### Data Understanding

The project analyzes nine related e-commerce datasets covering customers, orders, order items, payments, reviews, products, sellers, geolocation, and product category translation.

### Data Cleaning

The datasets were checked for:

- Missing values
- Duplicate records
- Invalid numerical values
- Incorrect data types
- Date and time formatting
- Categorical inconsistencies
- Primary-key uniqueness
- Foreign-key integrity

### Feature Engineering

Important analytical features include:

- Total order value
- Delivery days
- Delivery delay
- Customer order count
- Customer total spending
- Customer average order value
- Repeat customer indicator
- Seller order count
- Seller revenue
- Product sales
- Product units sold

### Exploratory Data Analysis

The project includes:

- Order status distribution
- Review score distribution
- Delivery time distribution
- Monthly order trends
- Monthly sales trends
- Payment method analysis
- Customer spending analysis
- Product category sales
- Delivery delay and review analysis
- Correlation analysis

### Statistical Analysis

Three statistical tests are performed:

1. Independent two-sample t-test
2. One-way ANOVA
3. Chi-square test

The tests include hypotheses, test statistics, p-values, decisions, and business interpretations.

### Streamlit Dashboard

The dashboard provides:

- Overall business metrics
- Order status analysis
- Monthly sales trends
- Payment method analysis
- Product category performance
- Seller performance
- Review score distribution

## How to Run

Install the required packages:

pip install pandas numpy matplotlib scipy streamlit

Run the dashboard:

streamlit run streamlit/app.py

## Business Insights

The analysis is used to identify patterns in sales, customer behavior, seller performance, delivery performance, payment methods, and customer satisfaction.

## Conclusion

Cart2Insights combines Python, SQL, exploratory analysis, statistical testing, and interactive visualization to transform e-commerce data into meaningful business insights and recommendations.
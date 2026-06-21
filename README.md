# Customer Segmentation Analysis using K-Means Clustering

## Project Overview

This project was developed as part of the **Oasis Infobyte Data Analytics Internship**.

The objective of this project is to segment customers into different groups based on their demographic and behavioral information using the **K-Means Clustering** algorithm. Customer segmentation helps businesses understand different customer groups and create targeted marketing strategies.

---

## Objectives

* Perform data exploration and cleaning.
* Visualize customer data.
* Encode categorical features.
* Scale numerical features.
* Determine the optimal number of clusters using the Elbow Method.
* Apply K-Means Clustering.
* Analyze customer segments and generate business insights.

---

## Dataset

The dataset contains customer demographic and behavioral information, including:

* Customer ID
* Age
* Gender
* Marital Status
* Education Level
* Occupation
* Income Level
* Policy Type
* Coverage Amount
* Premium Amount
* Customer Preferences
* Preferred Communication Channel
* Preferred Contact Time
* Preferred Language

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## Project Structure

```text
Customer-Segmentation/
│
├── data/
│   ├── data.csv
│   └── customer_segmented_data.csv
│
├── images/
│   ├── age_distribution.png
│   ├── gender_distribution.png
│   ├── education_distribution.png
│   ├── premium_distribution.png
│   ├── policy_distribution.png
│   ├── elbow_method.png
│   ├── cluster_distribution.png
│   └── customer_segments.png
│
├── report/
│   └── Customer_Segmentation_Report.pdf
│
├── src/
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Workflow

1. Load Dataset
2. Data Exploration
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Label Encoding
6. Feature Scaling
7. Elbow Method
8. K-Means Clustering
9. Cluster Analysis
10. Business Insights

---

## Data Exploration

The following steps were performed:

* Displayed first and last records
* Checked dataset shape
* Examined column names
* Verified data types
* Generated statistical summary
* Identified missing values
* Checked duplicate records
* Counted unique values

---

## Data Cleaning

The dataset was cleaned by:

* Handling missing values
* Removing duplicate records
* Standardizing column names
* Removing unnecessary spaces
* Verifying data types

---

## Data Visualization

The following visualizations were created:

* Age Distribution (Histogram)
* Gender Distribution (Bar Chart)
* Education Level Distribution (Bar Chart)
* Policy Type Distribution (Pie Chart)
* Premium Amount Distribution (Histogram)
* Average Premium by Age (Line Chart)
* Elbow Method Graph
* Cluster Distribution Chart

---

## Machine Learning

### Algorithm Used

* K-Means Clustering

### Feature Engineering

* Encoded categorical columns using LabelEncoder.

### Feature Scaling

* Standardized features using StandardScaler.

### Optimal Number of Clusters

The Elbow Method was used to determine the optimal number of clusters.

**Selected Number of Clusters (K): 4**

---

## Cluster Analysis

The K-Means algorithm divided customers into **4 different clusters** based on their characteristics.

Each cluster represents customers with similar demographic and behavioral attributes, enabling businesses to:

* Identify similar customer groups
* Understand purchasing behavior
* Design targeted marketing campaigns
* Improve customer engagement
* Support business decision-making

---

## Business Benefits

Customer segmentation can help organizations:

* Personalize marketing campaigns
* Improve customer satisfaction
* Increase customer retention
* Identify high-value customer groups
* Optimize product recommendations
* Enhance business strategies

---

## Results

* Successfully cleaned and explored the dataset.
* Performed customer data visualization.
* Determined the optimal number of clusters using the Elbow Method.
* Applied K-Means Clustering to segment customers.
* Generated customer groups for business analysis.

---

## Future Enhancements

* Compare multiple clustering algorithms (Hierarchical Clustering, DBSCAN).
* Build an interactive dashboard using Power BI or Tableau.
* Deploy the project as a web application.
* Perform customer lifetime value prediction.

---

## Requirements

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## Author

**Pratham Zope**

BE Computer Engineering Student

Government Engineering College, Modasa

---

## License

This project was created for educational purposes as part of the Oasis Infobyte Data Analytics Internship.

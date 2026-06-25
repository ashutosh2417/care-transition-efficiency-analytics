# 📊 Care Transition Efficiency & Placement Outcome Analytics

## 📌 Project Overview

This project analyzes the **Care Transition Efficiency** of the **Unaccompanied Alien Children (UAC) Program** by examining the movement of children through the care pipeline from **Customs and Border Protection (CBP)** custody to **Health and Human Services (HHS)** care and finally to **Sponsor Placement**.

The project focuses on measuring operational efficiency, identifying process bottlenecks, monitoring backlog accumulation, and evaluating placement outcomes through Business Analytics techniques.

An interactive **Streamlit Dashboard** has been developed to visualize Key Performance Indicators (KPIs), trends, and operational performance.

---

# 🎯 Business Problem

Traditional reporting primarily tracks the number of children in custody but does not measure the efficiency of transitions across the care pipeline.

This project addresses important operational questions such as:

* How efficiently are children transferred from CBP to HHS?
* Are sponsor placements keeping pace with new arrivals?
* Where do operational bottlenecks occur?
* How stable are placement outcomes over time?

---

# 🎯 Project Objectives

## Primary Objectives

* Measure Transfer Efficiency (CBP → HHS)
* Evaluate Discharge Effectiveness
* Detect Operational Bottlenecks
* Measure Pipeline Throughput

## Secondary Objectives

* Improve Case Management
* Support Faster Reunification
* Enhance Operational Monitoring
* Provide Data-Driven Insights

---

# 📂 Dataset Information

The dataset contains daily operational records of the UAC Program.

| Column                                         | Description           |
| ---------------------------------------------- | --------------------- |
| Date                                           | Reporting Date        |
| Children apprehended and placed in CBP custody | Daily Intake          |
| Children in CBP Custody                        | Active CBP Population |
| Children transferred out of CBP custody        | Daily Transfers       |
| Children in HHS Care                           | Active HHS Population |
| Children discharged from HHS Care              | Sponsor Placements    |

---

# 📊 Key Performance Indicators (KPIs)

The following KPIs were developed:

* Transfer Efficiency Ratio
* Discharge Effectiveness Index
* Pipeline Throughput Rate
* CBP Backlog
* HHS Backlog
* Outcome Stability Score

---

# 📈 Dashboard Features

The Streamlit Dashboard includes:

* Interactive Date Filter
* KPI Cards
* Daily Trend Analysis
* Transfer Efficiency Analysis
* Discharge Effectiveness Monitoring
* CBP Backlog Analysis
* HHS Backlog Analysis
* Outcome Stability Trend
* Interactive Charts using Plotly

---

# 📁 Project Structure

```text
Care_Transition_Project
│
├── dashboard
│   └── app.py
│
├── data
│   └── uac.csv
│
├── images
│
├── output
│
├── reports
│
├── screenshots
│
├── analysis.py
├── dashboard.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly
* Streamlit
* VS Code

---

# 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/care-transition-efficiency-analytics.git
```

### 2. Open the Project Folder

```bash
cd care-transition-efficiency-analytics
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
cd dashboard
streamlit run app.py
```

The dashboard will open automatically in your web browser.

---



# 📊 Project Outcomes

The project successfully:

* Calculated operational KPIs
* Identified care pipeline bottlenecks
* Measured transfer and discharge efficiency
* Visualized operational trends
* Developed an interactive dashboard for decision-making

---

# 💡 Recommendations

* Improve coordination between CBP and HHS.
* Reduce delays in sponsor placement.
* Implement automated KPI monitoring.
* Introduce real-time operational alerts.
* Expand dashboard-based performance tracking.

---

# 🔮 Future Scope

Future enhancements may include:

* Machine Learning for delay prediction
* Real-time data integration
* Cloud database support
* Automated notification system
* Predictive analytics dashboard

---

# 📄 Project Report

The detailed research report and executive summary will be available in the **reports** folder.

---

# 🌐 Live Demo

**Streamlit Dashboard:**

https://care-transition-efficiency-analytics-5xjtyazjcmt3pvevy7iocp.streamlit.app/


# 👨‍💻 Author

**Ashutosh Sharma **

MBA (Business Analytics)

Amity University Online

Internship Project 

LinkedIn: https://linkedin.com/in/ashutoshsharma0214

---

# ⭐ If you found this project useful, please consider giving it a star on GitHub.
# care-transition-efficiency-analytics
An end-to-end Business Analytics project analyzing care transition efficiency, placement outcomes, and operational bottlenecks using Python, Streamlit, and interactive dashboards.

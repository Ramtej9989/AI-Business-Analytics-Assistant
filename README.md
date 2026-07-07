# AI Business Analytics Assistant 📊🤖

An intelligent full-stack data analytics platform that helps users upload datasets, automatically analyze data quality, explore statistical patterns, generate AI-powered business insights, recommend visualizations, and ask natural-language questions about their data.

## 🌐 Live Demo

AI Business Analytics Assistant
https://ai-business-analytics-assistant.vercel.app

## 🚀 Overview

The AI Business Analytics Assistant simplifies the data analysis workflow by combining automated exploratory data analysis, data quality assessment, visualization recommendations, and AI-generated insights in a single platform.

Users can upload a CSV or Excel dataset and instantly receive structured analytical results without manually writing data analysis code.

The platform also includes an **Ask Your Data** feature that allows users to ask questions about their dataset using natural language.

## ✨ Features

### 📂 Dataset Upload

* Upload CSV, XLSX, and XLS datasets
* Automatic dataset loading and validation
* Detect rows, columns, and dataset structure
* Preview uploaded dataset information

### 🔍 Automated Data Analysis

* Automatic column type detection
* Exploratory Data Analysis (EDA)
* Statistical summaries
* Missing value detection
* Duplicate row analysis
* Unique value analysis

### 🧹 Data Quality Analysis

* Dataset quality scoring
* Missing data analysis
* Duplicate detection
* Column-level quality checks
* Automated cleaning recommendations

### 🔗 Correlation Analysis

* Detect relationships between numerical columns
* Identify strong positive correlations
* Identify strong negative correlations
* Generate correlation insights

### 📊 Smart Chart Recommendations

Automatically recommends suitable visualizations based on dataset column types and analytical patterns.

Supported chart recommendations include:

* Bar Charts
* Line Charts
* Scatter Plots
* Histograms
* Pie Charts
* Correlation Heatmaps

### 🤖 AI-Powered Business Insights

The platform analyzes dataset statistics and analytical results to generate meaningful business insights.

AI insights may include:

* Business trends
* Data quality observations
* Important correlations
* Potential risks
* Growth opportunities
* Actionable recommendations

### 💬 Ask Your Data

Users can ask natural-language questions about their uploaded dataset.

Example questions:

* What is the average customer age?
* Which category has the highest sales?
* What is the total revenue?
* Which customers have the highest churn risk?
* Show the top-performing categories.

The system interprets the question, performs the required dataset analysis, and returns an easy-to-understand answer.

### 🕘 Analysis History

* Store uploaded dataset metadata
* Save analysis results
* Save AI-generated insights
* View previous dataset analyses

### 📱 Responsive Design

The user interface is designed to support:

* Mobile devices
* Tablets
* Laptops
* Desktop screens

## 🛠️ Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* CSS
* Responsive Web Design

### Backend

* Python
* FastAPI
* Pandas
* NumPy
* SQLAlchemy

### Database

* PostgreSQL

### Data Analysis

* Pandas
* NumPy
* Statistical Analysis
* Exploratory Data Analysis

### AI Integration

* AI-powered insight generation
* Natural-language dataset questioning
* Dynamic dataset query processing

### Deployment

* Vercel — Frontend
* Cloud-hosted Backend API

## 🏗️ Project Architecture

```text
AI-Business-Analytics-Assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   └── package.json
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ramtej9989/AI-Business-Analytics-Assistant.git
```

```bash
cd AI-Business-Analytics-Assistant
```

## Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
python3 -m uvicorn app.main:app --reload
```

The backend API will run at:

```text
http://127.0.0.1:8000
```

## Frontend Setup

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

Open the application at:

```text
http://localhost:3000
```

## 🔄 Application Workflow

```text
Upload Dataset
      ↓
Dataset Validation
      ↓
Column Type Detection
      ↓
Data Quality Analysis
      ↓
Exploratory Data Analysis
      ↓
Correlation Analysis
      ↓
Cleaning Recommendations
      ↓
Smart Chart Recommendations
      ↓
AI Business Insights
      ↓
Ask Your Data
```

## 🎯 Project Goal

The goal of this project is to make data analytics more accessible by reducing the need for manual data exploration and repetitive analysis code.

The platform combines **Data Science, Backend Development, Frontend Development, and AI** to provide an automated analytics experience for users working with structured datasets.

## 🔮 Future Improvements

* Interactive chart generation
* Advanced AI analytics assistant
* Automated data cleaning
* PDF analytics report generation
* Dashboard customization
* User authentication
* Multiple dataset comparison
* Predictive analytics and machine learning models

## 👨‍💻 Author

**Rama Satya Teja Bonthu**

AI & Data Science Graduate

GitHub: https://github.com/Ramtej9989

LinkedIn: https://www.linkedin.com/in/bonthu-rama-satya-teja

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Contributions, suggestions, and feedback are welcome.

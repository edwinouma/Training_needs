import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st

# Set the working directory and load the dataset
os.chdir('C:/WORK/PERSONAL/EDWIN/Personal/Aga-Kan Foundation')
df = pd.read_excel("TrainingNeeds.xlsx")

# Define Likert scale categories
response_categories = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']


# Function to calculate frequencies and percentages for Likert scale variables
def calculate_likert_percentages(column):
    value_counts = df[column].value_counts(normalize=True) * 100
    value_counts = value_counts.reindex(range(1, 6), fill_value=0)  # Ensure alignment with Likert scale order
    return value_counts


# Function to create bar charts with Likert scale labels
def create_likert_bar_chart(data, title):
    fig = go.Figure(
        data=[
            go.Bar(
                x=response_categories,  # Use Likert scale labels
                y=data,
                text=data.round(1),
                textposition='auto',
                marker=dict(color='orange')
            )
        ],
        layout=go.Layout(
            title=title,
            xaxis=dict(title='Response Categories'),
            yaxis=dict(title='Percentage (%)', range=[0, 100])
        )
    )
    return fig


# Streamlit app layout
st.title("Training Needs Analysis Dashboard")
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Select Section",
    ["Demographics", "General Knowledge", "Effective Communication", "Managing Adverse Events", "Specific Issues"]
)

# Analyze Demographics Section
if section == "Demographics":
    st.header("Demographics Analysis")
    variables = ['Institution', 'Gender', 'Age', 'Role', 'Level']

    for var in variables:
        summary = df[var].value_counts(normalize=True) * 100
        st.subheader(var)
        if var in ['Gender', 'Level']:
            st.plotly_chart(
                go.Figure(
                    data=[go.Pie(labels=summary.index, values=summary)],
                    layout=go.Layout(title=var)
                )
            )
        else:
            st.bar_chart(summary)

# Analyze General Knowledge Section
if section == "General Knowledge":
    st.header("General Knowledge and Understanding of Quality Improvement")
    likert_columns = ['Q1b', 'Q2b', 'Q3b', 'Q4b', 'Q5b', 'Q6b', 'Q7b', 'Q8b', 'Q9b', 'Q10b', 'Q11b']
    likert_labels = {
        'Q1b': 'Six Dimensions of QI well understood',
        'Q2b': 'The key principles well understood',
        'Q3b': 'Key stakeholders and their roles are well known and appreciated',
        'Q4b': 'Faculty, residents/registrars and clinical rotation students have skills to analyze and prioritize QI',
        'Q5b': 'Faculty, residents/registrars, clinical rotation students have knowledge to identify performance indicators',
        'Q6b': 'Faculty competency development need for QI integration has been assessed and identified',
        'Q7b': 'There is a strategy for Capacity building of the requisite faculty competency',
        'Q8b': 'There is adequate ongoing coaching and mentoring on QI',
        'Q9b': 'Leadership and management provides conducive environment and support for QI',
        'Q10b': 'There is adequate Understanding of the complexities of health systems',
        'Q11b': 'There is adequate provision of Continuity of care'
    }

    for col in likert_columns:
        st.subheader(likert_labels[col])
        percentages = calculate_likert_percentages(col)
        st.plotly_chart(create_likert_bar_chart(percentages, likert_labels[col]))

# Analyze Effective Communication Section
if section == "Effective Communication":
    st.header("Effective Communication")
    likert_columns = ['Q1c', 'Q2c', 'Q3c', 'Q4c', 'Q5c']
    likert_labels = {
        'Q1c': 'Patients and carers are involved fully as partners in health care',
        'Q2c': 'Health Care Risks are adequately Communicated to patients by health workers',
        'Q3c': 'There is adequate and honest Communication with patients after an adverse event (open disclosure)',
        'Q4c': 'Informed consent of patient/client is always obtained when necessary',
        'Q5c': 'Students are taught and guided to be culturally respectful and knowledgeable (Cultural Competence)'
    }

    for col in likert_columns:
        st.subheader(likert_labels[col])
        percentages = calculate_likert_percentages(col)
        st.plotly_chart(create_likert_bar_chart(percentages, likert_labels[col]))

# Analyze Managing Adverse Events Section
if section == "Managing Adverse Events":
    st.header("Identifying, Preventing, and Managing Adverse Events")
    likert_columns = ['Q1d', 'Q2d', 'Q3d', 'Q4d', 'Q5d']
    likert_labels = {
        'Q1d': 'Students / HCW are taught how to recognize, report and manage adverse events and near misses.',
        'Q2d': 'Students are taught principles and practical applications in Managing Clinical Care Risks',
        'Q3d': 'Students/ HCW have adequate Understanding of health-care errors',
        'Q4d': 'Students/ HCW know how to Manage complaints in health care settings',
        'Q5d': 'There is an anonymous/confidential system of reporting medical errors'
    }

    for col in likert_columns:
        st.subheader(likert_labels[col])
        percentages = calculate_likert_percentages(col)
        st.plotly_chart(create_likert_bar_chart(percentages, likert_labels[col]))

# Analyze Specific Issues Section
if section == "Specific Issues":
    st.header("Specific Issues")
    likert_columns = ['Q1i', 'Q2i', 'Q3i', 'Q4i', 'Q5i', 'Q6i', 'Q7i', 'Q8i', 'Q9i', 'Q10i', 'Q11i', 'Q12i', 'Q13i']
    likert_labels = {
        'Q1i': 'Students/HCW know and understand how to Prevent or avoid wrong site, wrong procedure and wrong patient treatment',
        'Q2i': 'Students/HCW have adequate understanding of Medication safety',
        'Q3i': 'Students/HCW have adequate understanding and practice of Infection prevention and control',
        'Q4i': 'Clinical treatment and care in practicum facilities is Patient-centered',
        'Q5i': 'Patients in practicum facilities always receive treatment and care without harmful delays',
        'Q6i': 'The treatment and care in practicum facilities is Efficient',
        'Q7i': 'The treatment and care in practicum facilities is Equitable',
        'Q8i': 'The institution has a committee or unit in charge of quality standards of curriculum',
        'Q9i': 'The vision and mission of the institution include statements about quality of curriculum',
        'Q10i': 'The current strategic plan includes quality improvement objectives',
        'Q11i': 'The clinical placements facilities and resources are adequate',
        'Q12i': 'The organization includes statements on quality improvement and patient safety',
        'Q13i': 'Faculty/Facility leadership are trained on quality improvement concepts'
    }

    for col in likert_columns:
        st.subheader(likert_labels[col])
        percentages = calculate_likert_percentages(col)
        st.plotly_chart(create_likert_bar_chart(percentages, likert_labels[col]))

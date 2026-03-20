"""import pandas as pd

# Load dataset
data = pd.read_csv("jobs_dataset.csv")

# Ask user skill
user_skill = input("Enter your skill: ")

# Find matching jobs
results = data[data['skills'].str.contains(user_skill, case=False)]

# Show results
if len(results) > 0:
    print("\nRecommended Jobs:")
    for job in results['job_title']:
        print(job)
else:
    print("No jobs found for this skill")"""

import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Smart Job Recommendation System")

st.title("💼 Smart Job Recommendation System")
st.write("Enter your skills and get the best job recommendations")

# Load dataset
data = pd.read_csv("jobs_dataset.csv")

# User input
user_skills = st.text_input("Enter your skills (comma separated)")

if st.button("🔍 Recommend Jobs"):

    skills = user_skills.split(",")
    recommended_jobs = []

    for index, row in data.iterrows():
        job_skills = row['skills'].lower()

        for skill in skills:
            if skill.strip().lower() in job_skills:
                recommended_jobs.append(row)

    recommended_jobs = pd.DataFrame(recommended_jobs).drop_duplicates()

    if len(recommended_jobs) > 0:
        st.success("Jobs Found ✅")
        st.dataframe(recommended_jobs)
    else:
        st.error("No matching jobs found")
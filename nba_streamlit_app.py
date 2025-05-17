
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page title
st.title("🏀 NBA Players Stats Explorer")

st.markdown("""
This app allows you to explore historical NBA player data.
It includes height, weight, birth information, and college details.
""")

# Load dataset
file_url = "https://drive.google.com/uc?id=1qdhannFsde9m6nSZP-uy_WhO17F92bGn"
df = pd.read_csv(file_url)

# Clean the dataset
df = df.drop(columns=['Unnamed: 0'])
df = df.dropna(subset=['height', 'weight', 'born'])
df['birth_decade'] = (df['born'] // 10 * 10).astype(int)

# Sidebar filters
st.sidebar.header("Filter Options")
decade_filter = st.sidebar.selectbox("Choose Birth Decade", sorted(df['birth_decade'].unique()))
filtered_df = df[df['birth_decade'] == decade_filter]

# Show data
if st.checkbox("🔍 Show raw data"):
    st.dataframe(filtered_df)

# Plot: Height distribution
st.subheader("📏 Height Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df['height'], kde=True, ax=ax1)
ax1.set_title(f'Height Distribution – Born in {decade_filter}s')
st.pyplot(fig1)

# Plot: Average height/weight per decade (entire dataset)
st.subheader("📊 Average Height and Weight by Birth Decade")
avg_stats = df.groupby('birth_decade')[['height', 'weight']].mean()
fig2, ax2 = plt.subplots()
avg_stats.plot(kind='bar', ax=ax2)
ax2.set_title("Average Height and Weight per Decade")
ax2.set_ylabel("Average")
st.pyplot(fig2)

# Plot: Top colleges
st.subheader("🎓 Top 10 Colleges by Number of NBA Players")
top_colleges = df['collage'].value_counts().dropna().head(10)
fig3, ax3 = plt.subplots()
top_colleges.plot(kind='bar', ax=ax3)
ax3.set_title("Top 10 Colleges")
ax3.set_ylabel("Number of Players")
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("Created for the Midterm Project – Introduction to Data Science, Reichman University 2025.")

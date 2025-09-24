import os
import pandas as pd

# get the directory of the current script
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "metadata.csv")

# Load metadata.csv
df = pd.read_csv(file_path, low_memory=False)

print(df.shape)      # rows and columns
print(df.info())     # column names + data types
df.head(5)           # preview first rows
df.isnull().sum().sort_values(ascending=False).head(10)
df.describe()

#Data Cleaning
#Handling missing data
missing = df.isnull().mean().sort_values(ascending=False)
missing.head(10)
# Drop columns with >70% missing values
df_clean = df.dropna(thresh=len(df)*0.3, axis=1)

# Fill important text columns
df_clean = df_clean.copy()   # make a true copy first
df_clean['journal'] = df_clean['journal'].fillna('Unknown')
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean['year'] = df_clean['publish_time'].dt.year
df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').apply(lambda x: len(x.split()))

#Part 3: Data Visualization
import matplotlib.pyplot as plt
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean['year'] = df_clean['publish_time'].dt.year
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.title('CORD-19 Publications by Year')
plt.show()

#Top Journals
top_journals = df_clean['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
top_journals.plot(kind='bar', color='teal')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Journal')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Frequent Words In title
from collections import Counter
import re

all_words = ' '.join(df_clean['title'].dropna()).lower()
words = re.findall(r'\b[a-z]{4,}\b', all_words)  # words ≥4 letters
common_words = Counter(words).most_common(20)
print(common_words)

# Word Clouds
from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Words in Titles')
plt.show()

# Distribution by Source
df_clean['source_x'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Paper Counts by Source')
plt.ylabel('')
plt.show()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata interactively")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Widgets
year_range = st.slider("Select year range:", 2015, 2023, (2019, 2021))
filtered = df[df['year'].between(year_range[0], year_range[1])]

st.write(f"Total papers in range: {filtered.shape[0]}")
st.dataframe(filtered.head(20))

# Plot publications over time
counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(counts.index, counts.values, color='purple')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Word cloud of titles
all_words = ' '.join(filtered['title'].dropna()).lower()
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)



"""
## 🧾 Client Order – CSV Integration (Language Popularity)

**Client:** A Regional Tech Hub Coordinator.  
**Project:** Analysis of programming languages used by a small developer focus group.  
**Goal:** Extract data from a `.csv` file and create a sorted horizontal bar chart.

### 📊 Data Preparation
First, create a file named `dev_data.csv` in your working directory and paste this inside:

```csv
Responder_id,LanguagesWorkedWith
1,Python;JavaScript
2,Python;SQL;C++
3,Java;C++
4,Python;JavaScript;SQL
5,Java;C++
6,Python;C++
7,JavaScript;HTML/CSS
8,Python;JavaScript;Java
9,Python;C++
10,JavaScript;SQL;Python
```

### 📈 Requirements

1. **CSV Parsing**:
   - Use the standard `csv` module to open and read `dev_data.csv`.
   - Use `collections.Counter` to track the language frequencies.
   - **Crucial Logic**: Because the `LanguagesWorkedWith` column contains multiple values separated by a semicolon (`;`), you must use `.split(';')` on each row before updating your counter.

2. **Sorting**:
   - Use the `.most_common()` method from your Counter to get the data.
   - Ensure the languages are sorted so the **most popular** is at the top of the chart.

3. **Horizontal Chart (`barh`)**:
   - Color: Use a professional blue like `'#3a7ca5'`.
   - Style: Use `'fivethirtyeight'`.

4. **Labels and Title**:
   - X-axis: `"Number of People"`.
   - Y-axis: `"Programming Languages"`.
   - Title: `"Top Languages in Focus Group"`.

5. **Save**: Save the figure as `language_analysis.png`.

### ✅ Deliverable

Submit the Python script that processes the CSV and generates the chart. 

*Tip: If you get stuck on how to handle the semicolon split within the CSV loop, just think of it as a string you need to break into a list first.* **You are the developer. Complete this order.** 🐇
"""

import matplotlib.pyplot as plt
import csv
from collections import Counter


plt.style.use("fivethirtyeight")

languages = []
with open("dev_data.csv") as f:
    csv_reader = csv.DictReader(f)
    
    for row in csv_reader:
        languages.append(row["LanguagesWorkedWith"].split(";"))

c = Counter()  
for language in languages:
    c.update(language)

type = []
count = []

for item in c.most_common():
    type.append(item[0])
    count.append(item[1])

#print(c.most_common())
#most common returns a list of tuples

#use reverse to get from top to bottom
type.reverse()
count.reverse()

fig, ax = plt.subplots()

bar = ax.barh(type, count, color = "#3a7ca5" )
ax.set_xlabel("Number of people")
ax.set_ylabel("Programing Languages")
ax.bar_label(bar, padding = 3)
ax.set_title("Top Languages in Focus Group")

plt.tight_layout()
plt.savefig("language_analysis.png")
plt.show()

"""
We can do like this also:

with open("dev_data.csv") as f:
    csv_reader = csv.DictReader(f)
    
    c = Couter()
    for row in csv_reader:
        c.update(row["LanguagesWorkedWith"].split(";"))

# 1. Get the most common data
data = c.most_common()

# 2. Unpack them into two lists
# (This is a clever Python trick using zip)
languages, popularity = zip(*data)

# 3. Reverse them so the highest value is at the top of the barh chart
languages = list(languages)
languages.reverse()

popularity = list(popularity)
popularity.reverse()

# 4. Plot
ax.barh(languages, popularity)

"""
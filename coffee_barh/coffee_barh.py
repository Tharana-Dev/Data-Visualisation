"""

### 🧾 Client Order – The "Barh" Introduction

Since you don't know `barh` yet, let's do a **warm-up order** using simple lists before we even touch the CSV. This will make you comfortable with the "flip."

**Client:** A Coffee Shop Owner.  
**Project:** Visualize which coffee flavors are the most popular this week.  
**Goal:** Create a **horizontal** bar chart so the long flavor names are easy to read.

#### 📊 Data (Use these lists)
```python
flavors = ['Vanilla Latte', 'Caramel Macchiato', 'Hazelnut Praline', 'Dark Chocolate Mocha', 'Pumpkin Spice']
votes = [45, 38, 20, 52, 30]
```

#### 📈 Requirements
1.  **Horizontal Chart**: Use `plt.barh()`.
    - Set the flavors on the **Y-axis**.
    - Set the votes as the **width**.
    - Color: `'#8B4513'` (a coffee brown).
2.  **Labels and Title**:
    - X-axis: `"Number of Orders"`.
    - Y-axis: `"Coffee Flavor"`.
    - Title: `"Weekly Flavor Popularity"`.
3.  **Style**: Use `plt.style.use('ggplot')`.
4.  **Save**: Save as `coffee_popularity.png`.
5.  **Display**: Use the `fig, ax = plt.subplots()` approach.

#### ✅ Deliverable
Write the script to produce this chart. Once you see how the flavors sit neatly on the left side, you'll see why `barh` is so useful!

"""

import matplotlib.pyplot as plt

plt.style.use("ggplot")
fig, ax = plt.subplots()

flavors = ['Vanilla Latte', 'Caramel Macchiato', 'Hazelnut Praline', 'Dark Chocolate Mocha', 'Pumpkin Spice']
votes = [45, 38, 20, 52, 30]

bar = ax.barh(flavors, votes, color = "#8B4513")

ax.set_xlabel("Number of Oders")
ax.set_ylabel("Coffe Flavour")
ax.set_title("Weekly Flavour Popularity")
ax.bar_label(bar, padding=3)

plt.tight_layout()
plt.savefig("coffee_popularity.png")
plt.show()
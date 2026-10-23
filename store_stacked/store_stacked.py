"""
## 🧾 Client Order – Stacked CSV Analysis (Monthly Sales)

**Client:** A Hardware Store Owner.  
**Project:** Compare the sales of **Tools** vs. **Materials** over the first three months of the year.  
**Goal:** Create a **Stacked Vertical Bar Chart** where each month has one bar, and that bar is divided into two segments.

### 📊 Data (Create this as `store_data.csv`)

```csv
Month,Tools,Materials
Jan,120,80
Feb,150,90
Mar,170,110
```

### 📈 Requirements

1.  **CSV Loading**:
    * Use the `csv` module (DictReader is easiest here).
    * Extract the `Month` column into a list.
    * Extract `Tools` and `Materials` into two separate lists. **(Note: Remember to convert the values to `int()` because CSV reads everything as strings!)**

2.  **Stacked Bar Chart (`bar`)**:
    * This is a **Vertical** chart, so use `ax.bar()`.
    * **Segment 1 (Bottom):** Plot the `Tools` data. Color: `'#2c3e50'` (Midnight Blue).
    * **Segment 2 (Top):** Plot the `Materials` data *on top* of the tools. Use the `bottom` parameter: `ax.bar(months, materials, bottom=tools)`. Color: `'#95a5a6'` (Concrete Gray).

3.  **Labels and Title**:
    * Y-axis: `"Units Sold"`.
    * X-axis: `"Month"`.
    * Title: `"Monthly Sales: Tools vs Materials"`.
    * Add a **Legend** to identify which segment is which.

4.  **Styling**:
    * Use the `ggplot` style.
    * Use `ax.bar_label` for **both** segments so the client can see the exact numbers.

5.  **Save**: Save the figure as `stacked_sales.png`.

---

### 💡 The "Builder's" Challenge: The `bottom` Parameter
When you make a stacked chart, Matplotlib needs to know where the second bar should start. If you don't tell it, the bars will just overlap each other.



**Logic:**
`ax.bar(x, bottom_layer)`
`ax.bar(x, top_layer, bottom=bottom_layer)`

**Give this a shot!** This combines your CSV skills with the "Layering" logic of Matplotlib. If you can do this, you're ready for almost any manual data task. 🐇
"""

import csv
import matplotlib.pyplot as plt


plt.style.use("ggplot")

months = []
tools = []
materials = []
with open("store_data.csv") as f:
    csv = csv.DictReader(f)
    for row in csv:
        months.append(row["Month"])
        tools.append(int(row["Tools"]))
        materials.append(int(row["Materials"]))

#print(months)
#print(tools)
#print(materials)

fig, ax = plt.subplots()

b1 = ax.bar(months, tools, label = "Tools", color = "#2c3e50")
b2 = ax.bar(months, materials, bottom=tools, label = "Materials", color ="#95a5a6" )

ax.bar_label(b1, label_type='center', color='white', fontsize=9)
ax.bar_label(b2, label_type='center', color='white', fontsize=9)

ax.set_xlabel("Months")
ax.set_ylabel("Uniths Sold")
ax.set_title("Monthly Sales: Tools vs Materials")
ax.legend()

plt.tight_layout()
plt.savefig("stacked_sales.png")
plt.show()

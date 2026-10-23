"""
## 🧾 Client Order – The Pandas "Cleaning" Mission

In the real world, data isn't always nice and neat. Sometimes the client gives you a file where columns have extra spaces or you need to calculate new values on the fly. 

**Client:** A German Logistics Company.  
**Project:** Fuel Consumption Analysis.  
**Goal:** Use Pandas to calculate "Total Cost" and visualize it.

### 📊 Data (Create as `fuel_data.csv`)
*Copy this exactly—note the extra spaces in the headers!*

```csv
Vehicle , Liters , Price_Per_Liter 
Truck_A , 150 , 1.20
Truck_B , 200 , 1.15
Van_C , 80 , 1.30
Van_D , 95 , 1.25
```

### 📈 Requirements

1.  **Pandas Data Engineering**:
    * Load the data.
    * **Fix Headers:** Use `df.columns = df.columns.str.strip()` to remove those annoying extra spaces in the column names.
    * **Calculate:** Create a new column called `Total_Cost` by multiplying `Liters` * `Price_Per_Liter`. 
    * *Hint: `df['Total_Cost'] = df['Liters'] * df['Price_Per_Liter']`*

2.  **Horizontal Plotting (`barh`)**:
    * Y-axis: `Vehicle`.
    * Width (X-axis): `Total_Cost`.
    * Color: `'#f1c40f'` (Sunflower Yellow).

3.  **Labels and Title**:
    * X-axis: `"Total Fuel Cost (€)"`.
    * Y-axis: `"Vehicle ID"`.
    * Title: `"Logistics Fuel Expense Report"`.

4.  **Styling**:
    * Use `fivethirtyeight`.
    * Add value labels with a **Euro (€)** symbol if you can! (e.g., `ax.bar_label(b1, labels=[f'€{x:.2f}' for x in df['Total_Cost']])`)

### ✅ Deliverable
Submit the Python script. This order tests your ability to **modify** data inside a DataFrame, not just read it.

**Show me how you handle the "Data Engineering" side of things, Tharana!** 🐇
"""

import pandas as pd
import matplotlib.pyplot as plt

plt .style.use("fivethirtyeight")

df =pd.read_csv("fuel_data.csv")
df.columns = df.columns.str.strip()

df["Total_Cost"] = df["Liters"] * df["Price_Per_Liter"]

b1 = plt.barh(df["Vehicle"], df["Total_Cost"], color="#f1c40f")
labels=[f'€{x:.2f}' for x in df['Total_Cost']]
plt.bar_label(b1, labels=labels, padding=3, fontsize=10)


plt.xlabel("Total Fuel Cost (€)")
plt.ylabel("Vehicle ID")
plt.title('Logistics Fuel Expense Report')

plt.tight_layout()
plt.savefig("Fuel Data.png")
plt.show()
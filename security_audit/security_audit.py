"""
## 🧾 Client Order – The "Pandas" Gateway (Cyber Analysis)

**Client:** A Cybersecurity firm in Munich.  
**Project:** Analyzing server login attempts to identify peak "attack" times.  
**Goal:** Transition to **Pandas** to handle data. This is where your code goes from "15 lines" to "5 lines."

### 📊 Data (Create as `login_data.csv`)

```csv
Hour,Successful,Failed
00:00,120,5
04:00,30,2
08:00,450,25
12:00,600,10
16:00,550,45
20:00,300,15
```

### 📈 Requirements

1.  **The Pandas Shortcut**:
    * `import pandas as pd`.
    * Load with `df = pd.read_csv('login_data.csv')`.
    * *Notice: You don't need to create empty lists or loops anymore.*

2.  **Plotting from the DataFrame**:
    * Layer 1 (Bottom): `Successful`. Color: `'#27ae60'` (Emerald).
    * Layer 2 (Top): `Failed`. Color: `'#c0392b'` (Pomegranate).
    * `bottom` should simply be `df['Successful']`.

3.  **Labels and Title**:
    * Y-axis: `"Attempt Count"`.
    * X-axis: `"Time of Day (24h)"`.
    * Title: `"Server Login Security Audit"`.
    * Add a **Legend**.

4.  **Styling**:
    * Use `fivethirtyeight`.
    * Save as `security_audit.png`.

### ✅ Deliverable
Submit the Python script. **Observe how much easier it is to access data using `df['ColumnName']` instead of manual list appending.** You're moving into the big leagues now. **Complete the order.** 🐇
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv("login_data.csv")
time = df['Hour']
layer1 = df["Successful"]
layer2 = df["Failed"]


l1 = plt.bar(time, layer1, label = "Successful", color = "#27ae60")
l2 = plt.bar(time, layer2, bottom=layer1, label = "Failed", color ="#c0392b")

plt.bar_label(l1, label_type="center",fontsize = 10)
plt.bar_label(l2, label_type="center", color = "white", fontsize = 10)

plt.xlabel("Time of Day (24h)")
plt.ylabel("Attempt Count")
plt.title("Server Login Security Audit")
plt.legend()

plt.tight_layout()
plt.savefig("security_audit.png")
plt.show()

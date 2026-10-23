"""
## 🧾 Client Order – The "Multi-Stack" Challenge

**Client:** A Gym Chain Manager.  
**Project:** Track attendance across three different workout types.  
**Goal:** Create a **Stacked Bar Chart** with **three layers** (Cardio, Strength, and Yoga). This is the "Final Boss" of manual stacking.
 
### 📊 Data (Create as `gym_data.csv`)

```csv
Day,Cardio,Strength,Yoga
Mon,50,40,20
Tue,45,55,25
Wed,60,30,35
Thu,40,60,15
Fri,70,50,40
```

### 📈 Requirements

1.  **CSV Loading**:
    * Extract `Day`, `Cardio`, `Strength`, and `Yoga` into four separate lists (remember to convert numbers to `int`).

2.  **Triple Stack Logic**:
    * **Layer 1 (Bottom):** Cardio. Color: `'#e67e22'` (Carrot Orange).
    * **Layer 2 (Middle):** Strength. This must sit on top of Cardio. Color: `'#2980b9'` (Belize Hole Blue).
    * **Layer 3 (Top):** Yoga. This must sit on top of **both** Cardio and Strength combined. 
    * *Hint: For the 3rd layer, `bottom` should be a new list where you add Cardio + Strength values together.*

3.  **Labels and Title**:
    * Y-axis: `"Number of Members"`.
    * X-axis: `"Day of the Week"`.
    * Title: `"Daily Gym Attendance by Activity"`.
    * Add a **Legend**.

4.  **Styling**:
    * Use `fivethirtyeight` style.
    * Add centered labels to all three segments.

### ✅ Deliverable
Show me how you handle stacking **three** items instead of two. 


**You got this, Tharana. Show me that Builder logic.** 🐇
"""

import matplotlib.pyplot as plt
import csv

plt.style.use("fivethirtyeight")

with open("gym_data.csv") as f:
    days, cardio, strength, yoga = [], [], [], []
    
    reader = csv.DictReader(f)

    for row in reader:
        days.append(row['Day'])
        cardio.append(int(row['Cardio']))
        strength.append(int(row['Strength']))
        yoga.append(int(row['Yoga']))

bottom1 = cardio
bottom2 = [s + c for s,c in zip(cardio, strength)]

b1 = plt.bar(days,cardio, label = "Cardio", color ="#e67e22" )
b2 = plt.bar(days,strength,bottom=bottom1, label = "Strength", color ="#2980b9") 
b3 = plt.bar(days, yoga, bottom=bottom2, label = "Yoga", color = "#ff0000" )

plt.bar_label(b1, label_type="center", color = "black", fontsize = 9)
plt.bar_label(b2, label_type="center", color = "black", fontsize = 9)
plt.bar_label(b3, label_type="center", color = "black", fontsize = 9)

plt.xlabel("Day of the Week")
plt.ylabel("Number of Members")
plt.title("Daily Gym Attendance by Activity")
plt.legend()

plt.tight_layout()
plt.savefig("gym data.png")
plt.show()
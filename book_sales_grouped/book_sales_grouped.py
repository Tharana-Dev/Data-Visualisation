import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

months = ["Jan", "Feb", "Mar", "Apr"]
fiction = [120, 135, 110, 170]
non_fiction = [90, 95, 100, 110]

x = np.arange(len(months))
width = 0.2
space = 0.02

# Highlight highest Fiction bar
max_fiction_idx = np.argmax(fiction)
bars1 = plt.bar(x - (width + space)/2, fiction, width, label='Fiction', color='blue')
bars1[max_fiction_idx].set_color('red')

non_fict_maxidx = np.argmax(non_fiction)
bars2 = plt.bar(x + (width + space)/2, non_fiction, width, label='Non‑Fiction', color='orange')
bars2[non_fict_maxidx].set_color('yellow')


# Add value labels
plt.bar_label(bars1, padding=3)
plt.bar_label(bars2, padding=3)

# Customisation
plt.text(x[max_fiction_idx] - (width + space)/2, fiction[max_fiction_idx]*0.5,
         "P\nE\nA\nK", ha='center', color="white", fontsize=25)

plt.text(x[non_fict_maxidx] + (width + space)/2, non_fiction[non_fict_maxidx]*0.2,
        "P\nE\nA\nK", ha='center', color="black", fontsize=25)

plt.xticks(x, months)
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.title("Monthly Book Sales by Genre (January - April)", pad=15)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("grouped_book_sales_done.png", dpi = 150)
plt.show()

# Insight
print(f"Highest Fiction sales: {months[max_fiction_idx]} ({fiction[max_fiction_idx]} units)")
print(f"Highest Non Fiction sales: {months[non_fict_maxidx]} ({non_fiction[non_fict_maxidx]} units)")

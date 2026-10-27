import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Electronics": [25000, 30000, 28000, 35000, 40000, 45000],
    "Clothing": [15000, 18000, 16000, 20000, 22000, 25000],
    "Furniture": [10000, 12000, 14000, 13000, 16000, 18000],
    "Profit": [8000, 10000, 9000, 12000, 15000, 17000]
}

df = pd.DataFrame(data)
df["Total_sales"]= df["Electronics"] + df["Clothing"] + df["Furniture"]
# Calculate monthly sales growth percentage
df["Sales_Growth_%"] = df["Total_sales"].pct_change() * 100

print("\nMonthly Sales Growth:")
print(df[["Month", "Total_sales", "Sales_Growth_%"]].to_string(index=False))
total=df["Total_sales"].sum()

electronics_total = df["Electronics"].sum()
clothing_total = df["Clothing"].sum()
furniture_total = df["Furniture"].sum()



print(df)
print("Total Sales:", total)

print("Electronics:", electronics_total)
print("Clothing:", clothing_total)
print("Furniture:", furniture_total)
#figure 1
plt.figure(1)
colors=["red","blue","green","orange","purple","cyan"]
#creating bar chart for monthly total sales
bars=plt.bar(df["Month"],df["Total_sales"],color=colors,edgecolor="black")
plt.bar_label(bars,label_type="edge",fontsize=10)

plt.xlabel("Month",fontsize=12,fontweight="bold")
plt.ylabel("Total Sales (₹)",fontsize=12,fontweight="bold")
plt.title("Monthly Total Sales Analysis",fontsize=14,fontweight="bold")

plt.tight_layout()

# figure 2
plt.figure(2)
categories=["electronics","clothing","furniture"]
categories_total=[electronics_total,clothing_total,furniture_total]
colors=["lightpink","lightgreen","lightblue"]
#creating bar chart for category-wise sales
bars=plt.bar(categories,categories_total,edgecolor="black",color=colors)
plt.bar_label(bars,label_type="edge",color="black",fontsize=10,fontweight="bold")
plt.xlabel("Categories",fontsize=12,fontweight="bold")
plt.ylabel("Total Sales (₹)",fontsize=12,fontweight="bold")
plt.title("Category-wise Sales Analysis",fontsize=14,fontweight="bold")
plt.tight_layout()

#monthly profit analysis
#figure 3 
plt.figure(3)
#creating line chart for monthly profit analysis
bars=plt.bar(df["Month"],df["Profit"],color="saddlebrown",edgecolor="black")
plt.bar_label(bars,label_type="edge",fontsize=10)
plt.xlabel("Month",fontsize=12,fontweight="bold")
plt.ylabel("Profit (₹)",fontsize=12,fontweight="bold")
plt.title("Monthly Profit Analysis",fontsize=14,fontweight="bold")  
plt.tight_layout()


# Sales vs Profit Comparison

plt.figure(4)

plt.plot(df["Month"], df["Total_sales"], marker="o", label="Total Sales")
plt.plot(df["Month"], df["Profit"], marker="s", label="Profit")

plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.title("Monthly Sales vs Profit Comparison")

plt.legend()
plt.grid(True)

plt.tight_layout()

# Figure 5: Monthly Sales Growth Analysis

plt.figure(5)

growth = df["Sales_Growth_%"]

bars = plt.bar(
    df["Month"],
    growth,
    color=["gray", "green", "red", "green", "green", "green"],
    edgecolor="black"
)

plt.bar_label(bars, fmt="%.2f%%", padding=3)

plt.axhline(y=0, color="black", linewidth=1)

plt.xlabel("Month", fontsize=12, fontweight="bold")
plt.ylabel("Sales Growth (%)", fontsize=12, fontweight="bold")
plt.title("Monthly Sales Growth Analysis", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.show()

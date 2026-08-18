import matplotlib.pyplot as plt
import numpy as np
import os

# Create docs/images directory
os.makedirs('docs/images', exist_ok=True)

print("Creating dashboard images...")

# Executive Overview - Simple version
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle('Executive Overview Dashboard', fontsize=16, fontweight='bold')

# KPIs
kpis = ['Revenue\n£10.6M', 'Orders\n19,960', 'AOV\n£533', 'Customers\n4,338', 'Repeat Rate\n65.6%']
colors = ['#1E3A8A', '#14B8A6', '#F97316', '#8B5CF6', '#10B981']
for i, kpi in enumerate(kpis):
    if i < 5:
        row = i // 3
        col = i % 3
        axes[row, col].set_facecolor(colors[i])
        axes[row, col].text(0.5, 0.5, kpi, ha='center', va='center', fontsize=12, color='white', fontweight='bold')
        axes[row, col].axis('off')
axes[1, 1].axis('off')
axes[1, 2].axis('off')

# Monthly trend
months = ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
revenue = [150, 420, 520, 580, 620, 680, 720, 780, 850, 950, 1100, 1504]
axes[0, 2].plot(revenue, marker='o', linewidth=2, color='#1E3A8A')
axes[0, 2].set_title('Monthly Revenue')
axes[0, 2].grid(True, alpha=0.3)

# Countries
countries = ['UK', 'DE', 'FR', 'NL', 'ES']
country_rev = [9002, 420, 380, 290, 180]
axes[1, 0].barh(countries, country_rev, color='#14B8A6')
axes[1, 0].set_title('Top Countries')
axes[1, 0].invert_yaxis()

# Products
products = ['DOTCOM', 'HEART', 'CAKE', 'BIRD', 'GARLAND']
product_rev = [206, 120, 98, 87, 76]
axes[1, 1].barh(products, product_rev, color='#F97316')
axes[1, 1].set_title('Top Products')
axes[1, 1].invert_yaxis()

# Orders vs Revenue
orders = [280, 1450, 1680, 1820, 1950, 2100, 2250, 2380, 2520, 2680, 2850, 2769]
x = np.arange(12)
axes[1, 2].bar(x, orders, color='#8B5CF6', alpha=0.7, label='Orders')
axes[1, 2].plot(x, revenue, 'o-', color='#1E3A8A', linewidth=2, label='Revenue')
axes[1, 2].set_title('Orders vs Revenue')
axes[1, 2].legend()
axes[1, 2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('docs/images/dashboard_executive_overview.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Created: docs/images/dashboard_executive_overview.png")

# Customer Intelligence
fig, axes = plt.subplots(2, 2, figsize=(16, 9))
fig.suptitle('Customer Intelligence Dashboard', fontsize=16, fontweight='bold')

# Customer KPIs
ckpis = ['Customers\n4,338', 'Repeat\n2,845', 'One-time\n1,493', 'Repeat Rate\n65.6%']
for i, kpi in enumerate(ckpis):
    row = i // 2
    col = i % 2
    axes[row, col].set_facecolor(colors[i])
    axes[row, col].text(0.5, 0.5, kpi, ha='center', va='center', fontsize=14, color='white', fontweight='bold')
    axes[row, col].axis('off')

# RFM Donut
rfm_segments = ['Champions', 'Loyal', 'At-risk', 'Other', 'Cannot lose', 'Potential', 'Lost', 'New']
rfm_customers = [941, 457, 663, 490, 248, 405, 824, 310]
axes[0, 1].pie(rfm_customers, labels=rfm_segments, autopct='%1.1f%%', colors=colors, startangle=90)
axes[0, 1].set_title('RFM Segments')

# Revenue by Segment
rfm_revenue = [5.74, 0.90, 0.83, 0.57, 0.33, 0.19, 0.19, 0.14]
axes[1, 0].barh(rfm_segments, rfm_revenue, color=colors)
axes[1, 0].set_title('Revenue by Segment (£M)')
axes[1, 0].invert_yaxis()
axes[1, 0].grid(True, alpha=0.3, axis='x')

# Top Customers
top_cust = ['14646', '13360', '16098', '12431', '14911']
top_rev = [280, 186, 154, 142, 138]
axes[1, 1].barh(top_cust, top_rev, color='#10B981')
axes[1, 1].set_title('Top Customers (£K)')
axes[1, 1].invert_yaxis()

plt.tight_layout()
plt.savefig('docs/images/dashboard_customer_intelligence.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Created: docs/images/dashboard_customer_intelligence.png")

print("\n✅ Both images created successfully!")
print("Files:")
print("  - docs/images/dashboard_executive_overview.png")
print("  - docs/images/dashboard_customer_intelligence.png")

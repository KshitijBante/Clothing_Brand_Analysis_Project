sales_c['sale_date'] = pd.to_datetime(sales['sale_date'])

# Extract just the date part (no time)
sales_c['Day'] = sales_c['sale_date'].dt.day_name()

day_revenue = sales_c.groupby('Day')['total_amount'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(day_revenue['Day'], day_revenue['total_amount'], marker='o', color='teal')
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

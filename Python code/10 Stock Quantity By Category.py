product_gp = product_stock.groupby('category')['stock_quantity'].sum().reset_index()
product_gp =product_gp.sort_values(by='stock_quantity',ascending=False)

product_stock['product_name'].value_counts()

product_gp = product_stock.groupby('category')['stock_quantity'].sum().reset_index()
product_gp =product_gp.sort_values(by='stock_quantity',ascending=False)
# Plot
prst = sns.barplot(data=product_gp, x='category', y='stock_quantity', color='green')
prst.bar_label(prst.containers[0])

plt.title('Stock Quantity By Category')
plt.show()
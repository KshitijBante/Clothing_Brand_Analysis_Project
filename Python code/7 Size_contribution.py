full_sales = sales_c.merge(items_c, on='sale_id', how='left') \
                  .merge(product_c, on='product_id', how='left')

size_by_revenue=full_sales.groupby('size')['total_amount'].sum().reset_index()

plt.figure(figsize=(5,4))
plt.pie(size_by_revenue['total_amount'],labels=size_by_revenue['size'],autopct='%1.1f%%')
plt.title('Size distribution by revenue')
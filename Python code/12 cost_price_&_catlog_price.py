plt.figure(figsize=(10,6))
sns.displot(product_c['cost_price'],bins=30,kde=30,color='green')
plt.title('Distribution Of Product Cost Price')
plt.show()

plt.figure(figsize=(7,7))
plt.title('cost price vs catalog price')
sns.scatterplot(data=product_c,x='catalog_price',y='cost_price')
plt.show()
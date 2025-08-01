#Distribution of Original Price and Unit Price

sns.displot(items_c['original_price'],bins=30,color='blue',kde=True)
plt.title('Distribution of Original Price')
plt.figure(figsize=(10,6))

plt.show()

sns.displot(items_c['unit_price'],bins=30,color='darkblue',kde=True)
plt.title('Distribution of Unit price')

plt.figure(figure=(10,6))
plt.show()
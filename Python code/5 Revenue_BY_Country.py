plt.figure(figsize=(10,6))
c=sns.barplot(data=revenue_by_country,y='country',x='total_amount',hue='country',palette='viridis')
c.bar_label(c.containers[0],fmt='%.0f')
c.bar_label(c.containers[1],fmt='%.0f')
c.bar_label(c.containers[2],fmt='%.0f')
c.bar_label(c.containers[3],fmt='%.0f')
c.bar_label(c.containers[4],fmt='%.0f')
c.bar_label(c.containers[5],fmt='%.0f')
plt.title('Revenue By Country')
plt.tight_layout()
plt.show()


customer_by_country = customer_c['country'].value_counts().reset_index()
customer_by_country.columns=['country','customer_count']

plt.pie(customer_by_country['customer_count'],
        labels=customer_by_country['country'],
        autopct='%1.1f%%')

plt.title('Customer by country')
plt.figure(figsize=(4,4))
plt.show()
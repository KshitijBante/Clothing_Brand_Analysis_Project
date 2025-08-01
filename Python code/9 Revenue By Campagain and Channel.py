#Revenue By Campagain and Channel

p=sns.barplot(data=full_sales,x='channel_campaigns',y='total_amount',errorbar=None)
p.bar_label(p.containers[0],fmt='%.0f')
plt.title('Revenue by channel campaign')
plt.show()

er=sns.barplot(data=sales_c,x='channel',y='total_amount',color='green',errorbar=None)
plt.title('Revenue By Channel')
er.bar_label(er.containers[0])
plt.figure(figsize=(10,6))
plt.show()
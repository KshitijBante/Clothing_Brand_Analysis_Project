#customers By Most Revenue

merge_df = pd.merge(sales,customer,on="customer_id",how="inner")
Revenue_by_age= merge_df.groupby('age_range')['total_amount'].sum().reset_index()
Revenue_by_age=Revenue_by_age.sort_values(by='total_amount',ascending=False)

#Barchart

br=sns.barplot(data=Revenue_by_age,x='age_range',y='total_amount')
br.bar_label(br.containers[0])
plt.title('Total Revenue by age_category')
plt.figure(figsize=(10,6))
plt.tight_layout()
plt.show()

plt.figure(figsize=(5,5))
plt.pie(Revenue_by_age["total_amount"],
        labels=Revenue_by_age["age_range"],
        autopct='%1.1f%%',  # Show percentage
        startangle=140,
        colors=plt.cm.Paired.colors)
#Pie Chart
plt.title("Revenue Distribution by Age Range")
plt.axis("equal")  
plt.tight_layout()
plt.show()
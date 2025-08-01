cmp['start_date']=pd.to_datetime(cmp['start_date'])
cmp['end_date']=pd.to_datetime(cmp['end_date'])

def clean_discount(x):
    try:
        return float(str(x).replace('%','').strip())
    except Exception as e:
        return np.nan
cmp['discount_value']= cmp['discount_value'].apply(clean_discount)
print(cmp)

customer.dtypes

customer_c['signup_date']=pd.to_datetime(customer_c['signup_date'])

sales_c.dtypes

sales_c['sale_date']=pd.to_datetime(sales_c['sale_date'])

items_c=items.copy()
items_c.dtypes
items_c['discount_percent']=items_c['discount_percent'].apply(clean_discount)

items_c['sale_date']=pd.to_datetime(items_c['sale_date'])
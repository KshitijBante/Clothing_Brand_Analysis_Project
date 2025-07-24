# Clothing_Brand_Analysis_Project By using Python, SQL and Power Bi
# Project Overview:
This Project aims to analyze sales, customer behavior, and product
performance of a fashion retail store using multiple data sources. The analysis helps in identifying sales trends, understanding the impact of marketing campaigns, monitoring inventory, and providing actionable insights for business growth.

# Objectives:
* Analyze sales Performance and customer demographics.
* Evaluate the impact of discounts and marketing campaigns on revenue.
* Identify top-performing products and categories.
* Monitor stock levels and highlight low-stock products.
* Build interactive dashboards for business decision-making.

# Data Model
Defining an effective datastructure in dashboard is important, incorporating star schema model gives an efficent design
and makes data refresh faster. The image below tables used in the process


![image alt](https://github.com/KshitijBante/Clothing_Brand_Analysis_Project/blob/3eebb5a388df7ef237fa83015d0ecda56ccddb9d/data%20model.png)


# Tables that use in Data Model
- **clean_customers**	: Info about customers

- **clean_products**   :	Product catalog	product_id

- **clean_sales**	: Sales transactions	sale_id, customer_id

- **clean_campaigns**:	Marketing campaigns	campaign_id

- **dataset_fashion_store_channels**:	Sales channels (App, E-commerce)	channel

- **clean_stock** :	Inventory per product per country
 
- **Items Table** : Contains detailed records of each product sold in every transaction, including quantity and price-related information.

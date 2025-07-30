create database clothing_brand;
use clothing_brand;

CREATE TABLE Clean_camp(
`campaign_id` int ,
`campaign_name` varchar(40),
`start_date` date,
`end_date` date,
`channel` varchar(40),
`discount_type` varchar(40),
`discount_value` int);

select * from clean_camp;
alter table Clean_camp add constraint
 primary key(`campaign_id`);

set session sql_upates=1;

alter table clean_camp add constraint fk_channel
foreign key(`channel`)
references `store_channel`(`channel`);

set session sql_mode= '';
load data infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/archive (1)/clean_campaign.csv"
into table Clean_camp
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;


CREATE TABLE `clean_customer`(
customer_id int ,
country varchar(50),
age_range varchar(30),
signup_date varchar(40));



alter table `clean_customer`
add constraint primary key(customer_id);


load data infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/archive (1)/clean_customer.csv"
into table `clean_customer`
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

select * from `clean_customer`;

create table `store_channel`
(
`channel` varchar(50),
`Description` varchar(80));

alter table `store_channel`
add constraint primary key(`channel`);
desc `store_channel`;

load data infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/archive (1)/dataset_fashion_store_channels.csv"
into table `store_channel`
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

select * from `store_channel`;

alter table `store_channel`
add constraint primary key(`channel`);


create table stock
(
country varchar(45),
product_id int,
stock_quantity int);

load data infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/archive (1)/clean_stock.csv"
into table stock
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

select * from stock;

create table `items`(
item_id int,
sale_id int,
product_id int,
quantity int,
original_price int,
unit_price int,
discount_applied int,
discount_percent int,
discounted int,
item_total int,
sale_date varchar(70),
`channel` varchar(80),
`channel_campaigns` varchar(70));

alter table `items`
add constraint
primary key(item_id);

load data infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/archive (1)/clean_items.csv"
into table `items`
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

select * from `items`;

create table product(
product_id int,
product_name varchar(110),
category  varchar(60),
brand varchar(70),
color varchar(80),
size varchar(70),
catlog_price int,
cost_price int,
gender varchar(10));

alter table product
add constraint primary key(product_id);

load data infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/archive (1)/clean_product.csv"
into table product
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

select * from product;

create table sales(
sale_id int,
`channel` varchar(70),
discounted int,
total_amount int,
sale_date varchar(80),
customer_id int,
country varchar(70));

alter table sales
add constraint primary key(sale_id);


load data infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/archive (1)/clean_sales.csv"
into table sales
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

select * from sales;
-- what is total revenue from sales ?

select sum(total_amount) as revenue
from sales;

select * from sales;
-- Revenue by category

select `channel`, 
sum(total_amount) as revenue
from sales
group by `channel`;

-- Revenue by country

select country,
sum(total_amount) as revenue
from sales
group by country
order by revenue desc;

-- top 10 seling product by quantity

select  p.product_name, 
sum(i.quantity) as sum_of_quantity
from
items i 
join product p on i.product_id=p.product_id
group by p.product_name
order by sum_of_quantity desc
limit 10;

select * from clean_customer;

select c.age_range, 
sum(s.total_amount) as total_revenue
from
clean_customer c 
join sales s on c.customer_id=s.customer_id
group by c.age_range
order by total_revenue desc;

-- our most revenue gerated by 26 to 35 age range .

-- Do Discounts Increase Sales?

select * from sales;
select discounted, 
sum(total_amount)
from sales
group by discounted;

-- stock alterts (product with stock less than 20)


SELECT p.product_name, sum(st.stock_quantity) as total_stocks
FROM stock st
JOIN product p ON st.product_id = p.product_id
WHERE st.stock_quantity < 20
group by p.product_name
order by sum(st.stock_quantity);
 
 
--  contries with most number of customers
select country, count(*) as number_of_customers from 
`clean_customer`
group by country
order by number_of_customers desc;

-- which age-range should our targeted audiance ?

select * from `clean_customer`;

select age_range,count(*) as number_of_customers
from `clean_customer`
group by age_range
order by number_of_customers desc;







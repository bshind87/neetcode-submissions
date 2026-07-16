-- Write your query below
select name from customers where id not in (select customer_id as id from orders)
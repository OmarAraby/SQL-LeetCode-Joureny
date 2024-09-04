-- Write your PostgreSQL query statement below
select p.product_name , s.year,s.price
from sales as s ,product as p 
where s.product_id = p.product_id


-- using join
-- select p.product_name , s.year,s.price
-- from sales as s left outer join product as p 
-- on (s.product_id = p.product_id)

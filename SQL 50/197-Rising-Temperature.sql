-- Write your PostgreSQL query statement below
-- select id 
-- from weather w1
-- where temperature > (
--     select temperature
--     from weather w2
--     where w2.recordDate = w1.recordDate - interval '1 DAY'
-- );


--------- using join 

select w1.id 
from weather w1 
inner join weather w2
    on w1.recordDate = w2.recordDate + interval '1 DAY'
where W1.temperature > W2.temperature;
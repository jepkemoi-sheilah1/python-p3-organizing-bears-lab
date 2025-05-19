select_all_female_bears_return_name_and_age = """

  
    SELECT 
       bears.name,
         bears.age
FROM bears
WHERE sex = 'F';
"""
select_all_bears_names_and_orders_in_alphabetical_order = """
    

SELECT
         bears.name,
            bears.order
FROM bears
ORDER BY bears.name;
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
   
SELECT
        name
         
FROM bears
ORDER BY name;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """

SELECT
         bears.name,
            bears.age
FROM bears
WHERE alive = 1
ORDER BY bears.age;
"""

select_oldest_bear_and_returns_name_and_age = """
SELECT
         bears.name,
            bears.age
FROM bears
WHERE  name IS NOT NULL
ORDER BY bears.age DESC
LIMIT 1;
  

"""
select_youngest_bear_and_returns_name_and_age = """
SELECT
         bears.name,
            bears.age
FROM bears
WHERE age = (SELECT MIN(age) FROM bears);


"""
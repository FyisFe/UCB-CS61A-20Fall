.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) as average_price
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) as lowest_price
  FROM inventory
  GROUP BY item;

CREATE TABLE best_type AS
  SELECT category, name
  FROM products
  GROUP BY category
  HAVING MIN(MSRP/rating);

CREATE TABLE shopping_list AS
  SELECT b.name, l.store
  FROM best_type as b, lowest_prices as l
  WHERE b.name = l.item;

CREATE TABLE total_bandwidth AS
  SELECT SUM(stores.Mbs)
  FROM shopping_list, stores 
  WHERE shopping_list.store = stores.store;
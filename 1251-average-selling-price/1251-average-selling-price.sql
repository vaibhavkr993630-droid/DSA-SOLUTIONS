# Write your MySQL query statement below
SELECT joint.product_id,
      IFNULL( ROUND(SUM(p*u)/SUM(u) , 2), 0 ) As average_price
FROM(
    SELECT Prices.product_id, Prices.price As p, UnitsSold.units As u
    FROM Prices
    LEFT JOIN UnitsSold 
    ON Prices.product_id=UnitsSold.product_id 
    AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
    ) As joint
GROUP BY joint.product_id

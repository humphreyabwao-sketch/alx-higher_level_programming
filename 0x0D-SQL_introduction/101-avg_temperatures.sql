-- 101-avg_temperatures.sql

-- Connect to the hbtn_0c_0 database
USE hbtn_0c_0;

-- Calculate the average temperature (Fahrenheit) by city and order the results in descending order
SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

-- 1-create_table.sql

-- Connect to the hbtn_0c_0 database
USE hbtn_0c_0;

-- Create the first_table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

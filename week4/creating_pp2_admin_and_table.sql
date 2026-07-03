CREATE USER pp2_admin WITH PASSWORD 'pp2_admin';
CREATE DATABASE car_manufactures;
GRANT ALL PRIVILEGES ON DATABASE car_manufactures TO pp2_admin;

CREATE SCHEMA week4;
CREATE TABLE example_table (my_string VARCHAR(20) NOT NULL);
GRANT ALL PRIVILEGES ON SCHEMA public TO pp2_admin;
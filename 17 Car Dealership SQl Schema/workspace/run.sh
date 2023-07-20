# Install MySQL server
wget https://dev.mysql.com/get/mysql-apt-config_0.8.17-1_all.deb
dpkg -i mysql-apt-config_0.8.17-1_all.deb
apt-get update
apt-get install mysql-server

# Start MySQL server
service mysql start

# Login to MySQL
mysql -u root -p

# Create a new database
CREATE DATABASE dealership;

# Use the new database
USE dealership;

# Run the SQL schema
SOURCE schema.sql;

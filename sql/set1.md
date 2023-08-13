**Problem 1:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.


- **Answer** : 
 CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(50)
);


**Problem 2:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.

- **Answer** :  
INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
(1, 'Raman', 'Raman@example.com', 'new-york', '123-456-7890'),
(2, 'Rahul', 'Rahul@example.com', 'canada', '987-654-3210'),
(3, 'kuldeep ', 'kuldeep@example.com', 'england', '555-123-4567'),
(4, 'aman ', 'aman@example.com', 'france', '789-456-1230'),
(5, 'karan ', 'karan@example.com', 'germany', '333-777-9999'); 


**Problem 3:**

- **Prerequisite**: Understand basic data fetching in SQL / MongoDB
- **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

- **Answer** :  select * from customers 

**Problem 4:**

- **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
- **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.

- **Answer** : select customers.name as name , customers.email as email from customers


**Problem 5:**

- **Prerequisite**: Understand basic WHERE clause in SQL / MongoDB's find method
- **Problem**: Write a query to fetch the customer with the **`id`** of 3.
- **Answer** : select * from customers where customers.id = 3


**Problem 6:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all customers whose **`name`** starts with 'A'.
- **Answer** : select * from customers where customers.name like 'A%'

**Problem 7:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.
- **Answer** :  select * from customers order by name DESC


**Problem 8:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.
- **Answer** :  UPDATE customers SET address = 'russia' WHERE id = 4;


**Problem 9:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 3 customers when ordered by **`id`** in ascending order.
- **Answer** :  select * from customers order by id asc limit 3



**Problem 10:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the customer with **`id`** 2.
- **Answer** : delete from customers where id = 2

**Problem 11:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of customers.
- **Answer** : select COUNT(*) FROM customers

**Problem 12:**

- **Prerequisite**: Understand how to skip rows / documents in SQL / MongoDB
- **Problem**: Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.
- **Answer** : SELECT * FROM customers ORDER BY id asc limit 4 offset 2


**Problem 13:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is greater than 2 and **`name`** starts with 'B'.
- **Answer** :  select * from customers where id > 2 and name like 'B%'


**Problem 14:**

- **Prerequisite**: Understand how to use OR conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is less than 3 or **`name`** ends with 's'.
- **Answer** : select * from customers where id < 3 and name like '%s'


**Problem 15:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all customers where the **`phone_number`** field is not set or is null.
- **Answer** :  SELECT * FROM customers WHERE phone_number IS NULL OR phone_number = '' 


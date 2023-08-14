**Problem 16:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Restaurants`** table / collection with the fields defined above.
- **Answer** : 
    CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);


**Problem 17:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.
- **Answer** :  
INSERT INTO Restaurants (id, name, cuisine_type, location, average_rating, delivery_available)
VALUES
(1, 'Pasta Palace', 'Italian', 'New York', 3.5, true),
(2, 'Spice Garden', 'Indian', 'London', 4.2, true),
(3, 'Sushi Haven', 'Japanese', 'Tokyo', 4.7, true),
(4, 'Burger Joint', 'American', 'Los Angeles', 4.0, true),
(5, 'Mama Mia Pizzeria', 'Italian', 'Rome', 3.6, true);


**Problem 18:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.
- **Answer** : SELECT * FROM restaurants order by average_rating desc


**Problem 19:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.
- **Answer** : SELECT * FROM restaurants where delivery_available is True and average_rating > 4


**Problem 20:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.
- **Answer** :  SELECT * FROM restaurants WHERE cuisine_type IS NULL OR cuisine_type = '';


**Problem 21:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.

- **Answer** :SELECT COUNT(*) AS restaurant_count
FROM restaurants
WHERE delivery_available = 1;


**Problem 22:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.
- **Answer** : SELECT * FROM restaurants WHERE location LIKE '%New York%';


**Problem 23:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.

- **Answer** : SELECT AVG(average_rating) AS avg_rating FROM restaurants;


**Problem 24:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.
- **Answer** : SELECT * FROM restaurants ORDER BY average_rating DESC LIMIT 5;


**Problem 25:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the restaurant with **`id`** 3.

- **Answer** : DELETE FROM restaurants WHERE id = 3;

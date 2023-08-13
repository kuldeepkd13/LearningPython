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
- **Answer** : 
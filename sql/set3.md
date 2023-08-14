**Problem 26:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Rides`** table / collection with the fields defined above.

- **Answer** :   CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);

**Problem 27:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Rides`** table / collection with data of your choice.

- **Answer** :
INSERT INTO Rides (id, start_location, end_location, distance, fare, ride_time, driver_id)
VALUES
    (1, 'A', 'B', 10.5, 20.50, 15, 101),
    (2, 'B', 'C', 8.2, 15.75, 12, 102),
    (3, 'C', 'D', 5.0, 10.25, 8, 103),
    (4, 'D', 'E', 12.7, 25.00, 18, 101),
    (5, 'E', 'F', 7.8, 14.50, 11, 102);


**Problem 28:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all rides, ordered by **`fare`** in descending order.
- **Answer** : SELECT * FROM Rides ORDER BY fare DESC;


**Problem 29:**

- **Prerequisite**: Understand using math operations in SQL / MongoDB
- **Problem**: Write a query to calculate the total **`distance`** and total **`fare`** for all rides.
- **Answer** : SELECT SUM(distance) AS total_distance, SUM(fare) AS total_fare FROM Rides;


**Problem 30:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`ride_time`** of all rides.
- **Answer** : SELECT AVG(ride_time) AS avg_ride_time FROM Rides;


**Problem 31:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all rides whose **`start_location`** or **`end_location`** contains 'Downtown'.
- **Answer** :SELECT * FROM Rides WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';


**Problem 32:**

- **Prerequisite**: Understand how to use the COUNT function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to count the number of rides for a given **`driver_id`**.
- **Answer** : SELECT COUNT(*) AS ride_count FROM Rides WHERE driver_id = 101;


**Problem 33:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`fare`** of the ride with **`id`** 4.
- **Answer** : UPDATE Rides SET fare = 30.00 WHERE id = 4;



**Problem 34:**

- **Prerequisite**: Understand using GROUP BY in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the total **`fare`** for each **`driver_id`**.
- **Answer** : SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;


**Problem 35:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the ride with **`id`** 2.
- **Answer** : DELETE FROM Rides WHERE id = 2;

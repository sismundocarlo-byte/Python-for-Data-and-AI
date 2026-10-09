# SQL Learning Journal #2: Chinook Database

## 1. What I Learned
I leaned a lot of about SQL in this session we use DBeaver app, We open [Chinook.db](chinook.db) with Sqlite. And started doing queries from basic to advance.

First the basic and order of code. Simple but very important during the session in SQL this one of my most error often i didn't follow the correct order of code.

SELECT

FROM

WHERE

GROUP BY

HAVING

ORDER BY

LIMIT.

From that we go to harder queries like sub queries and CTE

## 2. A Query I Am Proud Of

```sql
## Q1 Who is the top 10 highest spending customer

WITH CustomerTotals AS 
(
    SELECT 
    	CustomerId, SUM(Total) AS TotalSpent
    FROM invoices
    GROUP BY CustomerId
)

SELECT c.FirstName || ' ' || c.LastName AS CustomerName,
       ct.TotalSpent
FROM customers c
JOIN CustomerTotals ct ON ct.CustomerId = c.CustomerId
ORDER BY ct.TotalSpent DESC
LIMIT 10;
```

I know it nothing complicated but it is the question exampled by the proctor in Sub queries topic and i did it in CTE in my own. And that why iam proud of it.

## 3. A Mistake or Struggle

Just Like what  i told before often i Code the wrong order and get a syntax error.

Second often mistake i make is inserting a comma to the last item in SELECT function.

Lastly although the code is working, But i don't use capitalize or indention for Functions and indention in variables so its hard to understand now iam practicing  using SELECT (Capitalize) and indention for readability of the code.


## 4. Connecting to the Real World

I think SQL is very relatable into real world because technology is already changing. Data base and data handling will become mainstream than manually inputting of data and recording.

Example: Just a simple Record of order in an online retail store. We might have a clustered of data or record of Purchase. But it is messy and cannot be understand at glance. So unless we apply and data handling, and SQL query to get the desired data else it will take a lot of time. From that queries we can get idea for future action or what possible problem we are dealing with.

## 5. Self-Assessment

| Topic | 1 | 2 | 3 | 4 | 5 |
|---|:-:|:-:|:-:|:-:|:-:|
| Basic SELECT, WHERE, ORDER BY | | | | | X |
| Aggregation (COUNT, SUM, AVG, GROUP BY, HAVING) | | | X | | |
| Subqueries | x | | | | |
| CTEs (WITH) and window functions | | x | | | |


My highest is basic SELECT because I got the early exercises right first try.

Aggregation is okay with me and comfortable using it just take note that we must create new name for the aggregated values.

Most of the time i cant understand sub queries but iam practicing and hopefully soon will master it.

CTE i like it better because in the beginning you can list all aggregated values and table you need to answer the question .

## 6. Goals and Next Steps

Currently I'm only comfortable using the basic of SQL but when it become complicated like Sub queries or CTE i become confuse often my code become error. So i need for practice to the point that just hearing the question i can already picture the code in my mind. So by the end of this booth camp i must already mastered SQL

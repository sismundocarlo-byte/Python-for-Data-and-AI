# SQL Learning Journal #2: Chinook Database

## 1. What I Learned

During this session, I learned a lot about SQL using DBeaver and the [Chinook database](chinook.db) with Sqlite. We started with basic queries and gradually moved to more advanced techniques. As we went through the exercises, I realized that SQL is not just about memorizing commands but also understanding how to organize them correctly and use them to get the information we need.

1. Understanding the Order of SQL Queries

One of the first things we covered was the basic structure and order of an SQL query:

SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT;

This is one of the areas where I often make mistakes, especially when I don't follow the correct order of clauses. Although it looks simple, understanding this structure is important because even a small mistake can cause a query to fail. I learned that practicing this order consistently will help me write queries more confidently.

2. Joining Different Tables

I also learned how to join different tables to retrieve related information from the database. This is useful when the data I need is spread across multiple tables. Instead of looking at each table separately, I can combine them using related columns and get a more complete result.

3. Aggregate Functions

We practiced using aggregate functions to perform calculations on data, such as counting records, calculating totals, and finding averages. These functions are useful when analyzing data because they help summarize large amounts of information into results that are easier to understand.

4. Subqueries and Common Table Expressions (CTEs)

As the session progressed, we moved on to more advanced queries, including subqueries and Common Table Expressions (CTEs).

Subqueries allow me to use the result of one query within another query, while CTEs help organize complex queries into smaller, more readable parts. These topics were more challenging, but they helped me understand how SQL can handle more complicated data problems.

My Takeaway

My biggest takeaway from this session is that understanding the logic and structure of a query is just as important as knowing the SQL commands. I still need more practice, particularly with the correct order of clauses and writing advanced queries, but I now have a better understanding of how to retrieve, combine, and analyze data using SQL.

I see these skills as an important foundation for my journey toward becoming a Data Analyst and eventually exploring Data Engineering. The more I practice, the more comfortable I expect to become working with databases and solving real-world data problems.

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

```sql
## Using comma in SELECT last Item my earlier codes when learning

SELECT c.FirstName, c.LastName, c.CustomerID,
FROM customers c
LIMIT 5;
```
```sql
## Wrong order of code

SELECT CustomerId, SUM(Total) AS TotalSpent
FROM invoices
WHERE SUM(Total) > 40
GROUP BY CustomerId;
```



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

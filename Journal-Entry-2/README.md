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

First, the CTE named CustomerTotals calculates the total amount spent by each customer using SUM(Total) and GROUP BY CustomerId. I gave the calculated value the name TotalSpent so I could refer to it easily in the main query.

Next, I joined the results with the customers table to get each customer's first and last name. I used ORDER BY with DESC to arrange customers from the highest total spending to the lowest, then LIMIT 10 to show only the top 10.

I know this is not the most complicated query, but I am proud of it because I was able to use a CTE instead of simply following the example. It helped me see how I can break a problem into smaller steps. In a real business, this kind of query could help identify high-value customers and support decisions about customer retention or promotions.

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

For me, SQL is very relatable to the real world because businesses already collect a lot of data, and managing it manually can become difficult as the amount of information grows.

For example, an online retail store may have thousands of purchase records. A business owner might want to know which products generate the most revenue or which customers purchase most frequently. SQL can help answer these questions without manually checking every transaction.

For product revenue, I could join the order details with the product table and use SUM() with GROUP BY to calculate the total sales for each product. For customer purchasing activity, I could group order records by customer and use COUNT() to determine how many orders each customer placed.

The results could help the business decide which products to promote, which items need more stock, and how to improve customer retention. This is one reason I want to improve my SQL skills as I work toward becoming a Data Analyst. I want to learn how to turn raw data into information that can actually help people make decisions.

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

Right now, I am comfortable with basic SQL, but I still get confused when queries become more complicated, especially with subqueries and CTEs. My goal is to reach a point where I can understand a question and have a clear idea of how to build the query instead of guessing which clause to use.

To improve, I will practice at least 10 SQL problems each week, focusing on joins, aggregation, subqueries, and CTEs. I will try to solve each problem on my own before checking my notes or looking at an example. I also want to explore window functions because they seem useful for more advanced data analysis.

By the end of this boot camp, I want to be confident enough to solve common SQL problems independently and use these skills in my Data Analyst portfolio projects.

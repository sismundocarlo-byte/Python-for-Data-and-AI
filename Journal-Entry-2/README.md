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
WITH customer_totals AS (
    SELECT c.CustomerId, c.SupportRepId,
           SUM(i.Total) AS TotalSpent
    FROM Customer c
    JOIN Invoice i ON i.CustomerId = c.CustomerId
    GROUP BY c.CustomerId
)
SELECT e.FirstName || ' ' || e.LastName AS SupportRep,
       COUNT(*) AS Customers,
       ROUND(AVG(ct.TotalSpent), 2) AS AvgSpent
FROM customer_totals ct
JOIN Employee e ON e.EmployeeId = ct.SupportRepId
GROUP BY e.EmployeeId
ORDER BY AvgSpent DESC;
```

The CTE runs first and works out how much each customer has spent in total. The main query then joins that result to Employee so each customer is tied to their support rep. GROUP BY collapses it to one row per rep, COUNT gives how many customers they handle, AVG gives the average spend per customer, and ORDER BY puts the best result on top.

The business question: which support reps look after the highest-value customers? A manager could use it to see who might need more customers, or whose approach is worth copying. Although I'm having a hard time following the queries during the class. and most of my classmate already know the answer but i practice after class and manage to do this query after a lot of practice.

## 3. A Mistake or Struggle

I wanted to count how many invoices each customer had, so I joined Invoice to InvoiceLine and wrote:

```sql
SELECT c.CustomerId, COUNT(i.InvoiceId) AS InvoiceCount
FROM Customer c
JOIN Invoice i ON i.CustomerId = c.CustomerId
JOIN InvoiceLine il ON il.InvoiceId = i.InvoiceId
GROUP BY c.CustomerId;
```

No error, but the counts were far too high. [Write the real numbers you saw, e.g. "a customer showed 38 invoices when they only had 7".]

The cause: each invoice has several lines, so joining InvoiceLine repeats the invoice once per line, and COUNT counted every repeat. Since it didn't error, I only caught it because the numbers looked wrong. The fix was `COUNT(DISTINCT i.InvoiceId)`, or just not joining InvoiceLine at all, since I didn't need it.

Takeaway: after any join, I now check the row count against what I expect before trusting an aggregate.

## 4. Connecting to the Real World

I think SQL is very relatable into real world because technology is already changing. Data base and data handling will become mainstream than manually inputting of data and recording.

Example: Just a simple Record of order in an online retail store. We might have a clustered of data or record of Purchase. But it is messy and cannot be understand at glance. So unless we apply and data handling, and SQL query to get the desired data else it will take a lot of time. From that queries we can get idea for future action or what possible problem we are dealing with.

## 5. Self-Assessment

| Topic | 1 | 2 | 3 | 4 | 5 |
|---|:-:|:-:|:-:|:-:|:-:|
| Basic SELECT, WHERE, ORDER BY | | | | | X |
| Aggregation (COUNT, SUM, AVG, GROUP BY, HAVING) | | | X | | |
| Subqueries | | x | | | |
| CTEs (WITH) and window functions | | | x | | |


My highest is basic SELECT because I got the early exercises right first try. Aggregation is strong too, though my duplicated-count mistake shows I still slip. My lowest is Subqueries, I try it but i just confuse but will practice again till i get it right. Subqueries and 3+ table joins sit at a 3 because I need my notes to get the join conditions right.

## 6. Goals and Next Steps

Currently I'm only comfortable using the basic of SQL but when it become complicated like Sub queries or CTE i become confuse often my code become error. So i need for practice to the point that just hearing the question i can already picture the code in my mind. So by the end of this booth camp i must already mastered SQL

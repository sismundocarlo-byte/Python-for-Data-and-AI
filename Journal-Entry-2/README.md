# SQL Learning Journal #2: Chinook Database

## 1. What I Learned
I leaned a lot of about SQL in this session we use DBeaver app, We open [Chinook.db](chinook.db) with Sqlite. And started doing queries from basic to advance.

**Aggregation and GROUP BY.** Without GROUP BY, SUM or COUNT squashes the whole table into one number. GROUP BY lets you get one number per category, like one total per customer. Every non-aggregated column in SELECT has to be in the GROUP BY, otherwise the database doesn't know what to show.

**WHERE vs HAVING.** WHERE filters rows before grouping, HAVING filters after. I only really got it once I tried to filter on a total and it wouldn't let me.

**CTEs.** A CTE is basically giving a subquery a name so you can read the query top to bottom. For me it made long queries way less scary because I could build and test one piece at a time.

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

The business question: which support reps look after the highest-value customers? A manager could use it to see who might need more customers, or whose approach is worth copying. [Mention what the top result was when you ran it.]

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

[Swap in an app or business you actually use.] Take a food delivery app like GrabFood. Two questions it could answer:

1. **Which restaurants earned the most last month?** Join Orders, OrderItems and Restaurants, then SUM with GROUP BY. Same shape as my support rep query.
2. **Which customers ordered once and never came back?** Orders grouped by customer with HAVING COUNT(*) = 1, or a subquery on last order date. This could drive promo vouchers.

SQL is still everywhere because most business data already lives in relational databases, and the language is close to plain English, so analysts and non-programmers can both pick it up.

## 5. Self-Assessment

| Topic | 1 | 2 | 3 | 4 | 5 |
|---|:-:|:-:|:-:|:-:|:-:|
| Basic SELECT, WHERE, ORDER BY | | | | | X |
| Aggregation (COUNT, SUM, AVG, GROUP BY, HAVING) | | | X | | |
| Joins (2 tables) | | | | X | |
| Joins (3 or more tables) | | | X | | |
| Subqueries | | x | | | |
| CTEs (WITH) and window functions | | | x | | |


My highest is basic SELECT because I got the early exercises right first try. Aggregation is strong too, though my duplicated-count mistake shows I still slip. My lowest is Subqueries, I try it but i just confuse but will practice again till i get it right. Subqueries and 3+ table joins sit at a 3 because I need my notes to get the join conditions right.

## 6. Goals and Next Steps

I want to get better at 3+ table joins by doing a few practice queries each week on Chinook, checking row counts each time. I'm curious about window functions, especially ranking.

**Goal:** by [the end of october], I'll write five new queries joining at least three tables and rewrite two of them with CTEs.

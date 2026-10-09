# SQL Learning Journal #2
### Reflecting on what I learned using SQL for the Chinook database

---

## Section 1: What I Learned

Honestly the biggest thing for me this module was understanding the order SQL actually runs things in, because it's not the order you write it. Once I got that, a lot of stuff clicked.

**WHERE vs HAVING:** WHERE filters individual rows *before* any grouping happens. HAVING filters the groups *after* GROUP BY and aggregation. So if you want only invoices over $5, that's WHERE. If you want only customers whose *total* is over $50, that's HAVING, because the total doesn't exist until the rows are grouped.

**JOINs:** I think of a join as lining up two tables on a shared key, like matching `Track.GenreId` to `Genre.GenreId` so I can see a genre name instead of a number. INNER JOIN only keeps rows that match on both sides, while LEFT JOIN keeps everything from the left table even when there's no match.

**Subqueries vs joins:** A subquery is a query that feeds its result into another query. I use one when I need a single value to compare against, like "tracks priced above the average price." A join is better when I need columns from both tables in the output.

I also covered sorting, CTEs, and INSERT/UPDATE/DELETE, but the three above are what I could actually explain to someone else.

---

## Section 2: A Query I Am Proud Of

```sql
SELECT g.Name AS Genre,
       SUM(il.UnitPrice * il.Quantity) AS Revenue
FROM Genre g
JOIN Track t ON t.GenreId = g.GenreId
JOIN InvoiceLine il ON il.TrackId = t.TrackId
GROUP BY g.Name
HAVING SUM(il.UnitPrice * il.Quantity) > 100
ORDER BY Revenue DESC;
```

Walking through it in the order the database processes it:

1. **FROM / JOIN:** starts with Genre, connects it to Track, then to InvoiceLine, so every sale can be traced back to a genre.
2. **GROUP BY:** bundles all those rows by genre name.
3. **SUM(...):** for each genre, multiplies price by quantity and adds it up.
4. **HAVING:** throws away genres with $100 or less in revenue.
5. **SELECT:** picks the columns to show.
6. **ORDER BY:** sorts the biggest earner first.

I'm proud of it because it was my first 3-table join that worked cleanly, and it answers a real question: *which genres actually make the store money?* A manager could use it to decide where to spend on licensing or promotions. Rock was way ahead of everything else.

---

## Section 3: A Mistake or Struggle

My first attempt at the query above looked like this:

```sql
SELECT g.Name, SUM(il.UnitPrice * il.Quantity) AS Revenue
FROM Genre g
JOIN Track t ON t.GenreId = g.GenreId
JOIN InvoiceLine il ON il.TrackId = t.TrackId
WHERE SUM(il.UnitPrice * il.Quantity) > 100
GROUP BY g.Name;
```

It threw this error: `misuse of aggregate function SUM()`

I stared at it for a while because the logic seemed fine to me. I was thinking "I just want genres over $100, so that's a filter, so WHERE." The problem is that WHERE runs before GROUP BY, so at that point there's no total to compare against yet. The condition belongs in HAVING.

I figured it out by going back to my notes on the order of execution and asking, "does the thing I'm filtering on exist yet at this step?" Next time, if my filter involves SUM, COUNT, or AVG, I'll default to HAVING and use WHERE only for raw column values. I also write GROUP BY right after FROM now so I don't forget it.

---

## Section 4: Connecting to the Real World

Think of Spotify or any music streaming app. Two questions it could answer with SQL:

1. **Which artists get the most plays this month?** This would join something like Artists, Albums, Tracks, and Plays, then use COUNT with GROUP BY and ORDER BY. It's basically the same shape as my genre revenue query.
2. **Which users haven't listened to anything in 30 days?** This could be a subquery or a LEFT JOIN between Users and Plays, looking for users with no recent plays. The company could use it to send win-back offers.

I think SQL is still everywhere because it's readable, it's standardized across most databases, and relational tables are a natural way to store business data. Nearly every company already has data sitting in a database, so analysts need a way to ask it questions directly.

---

## Section 5: Self-Assessment

| Topic | 1 | 2 | 3 | 4 | 5 |
|---|:-:|:-:|:-:|:-:|:-:|
| Basic SELECT, WHERE, ORDER BY | | | | | X |
| Aggregation (COUNT, SUM, AVG, GROUP BY, HAVING) | | | | X | |
| Joins (2 tables) | | | | | X |
| Joins (3 or more tables) | | | | X | |
| Subqueries | | | X | | |
| CTEs (WITH) and window functions | | X | | | |
| CREATE, INSERT, UPDATE, DELETE | | | | X | |

*Scale: 1 = I am lost, 3 = I can do it with notes or help, 5 = I could teach it.*

My highest ratings are basic SELECT/WHERE/ORDER BY and 2-table joins. I got those right on the first try in nearly every exercise. My lowest are CTEs/window functions and subqueries. I can write a simple subquery, but I still mix up when to use one vs a join, and I only just started on CTEs, so I still need my notes open every time.

---

## Section 6: Goals and Next Steps

The skill I want to strengthen is subqueries. To practice, I'll redo some of my join queries from this module as subqueries and compare which one reads better.

I'm curious about window functions, like ranking customers by spend without collapsing the rows the way GROUP BY does.

**Goal:** By next Friday, I'll rewrite three of my Chinook queries as CTEs and write one query using `ROW_NUMBER()` or `RANK()`.

Honestly the biggest thing for me this module was understanding the order SQL actually runs things in, because it’s not the order you write it. Once I got that, a lot of stuff clicked.

WHERE vs HAVING: WHERE filters individual rows before any grouping happens. HAVING filters the groups after GROUP BY and aggregation. So if you want only invoices over $5, that’s WHERE. If you want only customers whose total is over $50, that’s HAVING, because the total doesn’t exist until the rows are grouped.

JOINs: I think of a join as lining up two tables on a shared key, like matching Track.GenreId to Genre.GenreId so I can see a genre name instead of a number. INNER JOIN only keeps rows that match on both sides, while LEFT JOIN keeps everything from the left table even with no match.

Subqueries vs joins: A subquery is basically a query that feeds its result into another query. I use one when I need a single value to compare against, like “tracks priced above the average price.” A join is better when I need columns from both tables in the output.

I also covered sorting, CTEs, and INSERT/UPDATE/DELETE, but the three above are what I could actually explain to someone else.

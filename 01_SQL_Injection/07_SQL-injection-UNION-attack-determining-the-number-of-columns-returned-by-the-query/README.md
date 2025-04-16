# SQL injection attack, listing the database contents on Oracle

**Lab Url**: [https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)

![Lab Description](img/lab-description.png)

## Objective

The lab objective is to determine the number of columns returned by the query.

## Solution

We can use the below payload on the category parameter to determine the number of columns returned by the query.

```bash
/filter?category=Lifestyle'+union+select+null,null,null+from+information_schema.tables+--
```

Keep incrementing the number of `NULLs` starting from 1 until you get an `internal server error`. The number of `NULL` is the number of columns returned by the query.

![Lab Solved](img/lab-solved.png)

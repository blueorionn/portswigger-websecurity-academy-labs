# SQL injection attack, querying the database type and version on Oracle

**Lab Url**: [https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)

![Lab Description](img/lab-description.png)

## Objective

SQL injection attack, querying the database type and version on Oracle

## Analysis

The initial step is to understand how the vulnerable application works and gather information about the target system. The application showcases a product catalog with a product name and description. The navbar contains a feature to filter out products by category.

Let's append an apostrophe at the end of the query to observe if the application behaves differently. Hmm, the application returned an `internal server error` with a `500 status code`.

![internal Server Error](img/internal-server-error.png)

Using `ORDER BY` clauses, it was determined that the Query returns **two** columns.

```bash
/filter?category=Accessories'+ORDER+BY+2+--
```

We can craft a query to retrieve the **Oracle Database version** from the system view `v$version`.

```bash
/filter?category=Accessories'+UNION+SELECT+NULL,+banner+FROM+v$version--
```

![Oracle Version](img/oracle-version.png)

![Lab Solved](img/lab-solved.png)

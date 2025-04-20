# User role controlled by request parameter

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)

![Lab Description](img/lab-description.png)

## Analysis

The application showcases an image catalog with an image, a title, a price, a star rating, and a "View Details" button. Additionally, it has a `/my-account` page that redirects to the `/login` page. Log in to the application with the provided credentials on the lab description. Now try to access the admin panel at `/admin`.

You can observe that the application returns a `401 unauthorized code`.

![Admin Panel Unauthorized](img/admin-panel-unauthorized.png)

## Solution

To access the admin panel modify the cookie value `Admin` to `true`.

![Admin Panel Content](img/retrived-admin-panel.png)

The admin panel would look something like this.

![Admin Panel](img/admin-panel.png)

Now delete the user carlos to solve the lab.

![Lab Solved](img/lab-solved.png)

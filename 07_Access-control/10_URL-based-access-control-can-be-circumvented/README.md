# URL-based access control can be circumvented

**Lab Url**: [https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented](https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented)

![Lab Description](img/lab-description.png)

## Analysis

The initial step is to understand how the vulnerable application works and gather information about the target system. The application showcases an image catalog with an image, a title, a price, a star rating, and a "View Details" button that redirects to the product page.

If you try to visit the admin page, you will receive **`403 Forbidden`** status.

![Admin Forbidden](img/admin-forbidden.png)

The lab description states that the application supports the `X-Original-URL` header.

Even if you add the `X-Original-URL` header on the request tab and try to access the admin page, you will receive `403 Forbidden` Status.

![X Original URL Forbidden](img/x-original-url-forbidden.png)

To access the admin page, issue a `GET` request to a non-existent URL while setting the value of the `X-Original-URL` header to `/admin`.

![Admin Page](img/admin-panel.png)

## Solution

From the admin panel source code, you can retrieve the URL to delete the user `carlos`.

![Admin Panel](img/admin-panel.png)

Hmm, we got an error indicating that there is a Missing parameter `username`.

![Missing Username](img/missing-parameter.png)

To delete the user `carlos` change the `GET` request to `/?username=carlos` and X-Original-URL to `/admin/delete`.

![Carlos Deleted](img/user-deleted.png)

![Lab Solved](img/lab-solved.png)

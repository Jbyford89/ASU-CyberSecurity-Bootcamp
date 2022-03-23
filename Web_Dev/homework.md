## Week 14 Homework

---

### Questions 

#### HTTP Requests and Responses

Answer the following questions about the HTTP request and response process.

1. What type of architecture does the HTTP request and response process occur in?
  - _Client-server architecture, this is in the *Application Layer 7*_

2. What are the different parts of an HTTP request? 
  - _The Request Line is the first portion of the request._
    - _Then its the HTTP method used._
    - _The request URL._
    - _HTTP protocol version._

  - _Request Header, this is a header that can be used in a HTTP request to provide information about the requested context.__
  - _Request Body, data sent by the client to the API._

3. Which part of an HTTP request is optional?
  - _Request Body_

4. What are the three parts of an HTTP response?
  - _Status Line_
  - _Header_
  - _Body is optional_

5. Which number class of status codes represents errors?
  - _400 codes indicate client-side errors._
  - _500 codes indicate server-side errors._

6. What are the two most common request methods that a security professional will encounter?
  - _GET, request that asks for data from a server._
  - _POST, sends data to specified resource._

7. Which type of HTTP request method is used for sending data?
  - _POST_

8. Which part of an HTTP request contains the data being sent to the server?
  - _The request body._

9. In which part of an HTTP response does the browser receive the web code to generate and style a web page?
  - _The response body._

---

#### Using curl

Answer the following questions about `curl`:

10. What are the advantages of using `curl` over the browser?
  - You can use cURL for many beneficial things such as:
    - _Authentication_
    - _SSL connections._
    - _HTTP post requests._
    - _Proxy support._
    - _FTP uploads._
    - _Downloading files._

11. Which `curl` option is used to change the request method?
  - _You can use the `-X` or `--request` options._

12. Which `curl` option is used to set request headers?
  - _You can use the `-H` or `--header` options._

13. Which `curl` option is used to view the response header?
  - _You can use the `-i` or `--include` options._

14. Which request method might an attacker use to figure out which HTTP requests an HTTP server will accept?
  - _GET request because the attacker could request data from a server to figure out which HTTP request a server will accept as well as the error codes to see what pages are real or fake._

#### Sessions and Cookies

Recall that HTTP servers need to be able to recognize clients from one another. They do this through sessions and cookies.

Answer the following questions about sessions and cookies:

15. Which response header sends a cookie to the client?

    ```HTTP
    HTTP/1.1 200 OK
    Content-type: text/html
    Set-Cookie: cart=Bob
    ```
  - _The set-cookie will send the cookie to the client._


16. Which request header will continue the client's session?

    ```HTTP
    GET /cart HTTP/1.1
    Host: www.example.org
    Cookie: cart=Bob
    ```
  - _The cookie will continue and remember where the clients last place was in the session._

#### Example HTTP Requests and Responses

Look through the following example HTTP request and response and answer the following questions:

**HTTP Request**

```HTTP
POST /login.php HTTP/1.1
Host: example.com
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 34
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36

username=Barbara&password=password
```

17. What is the request method?
  - _POST_

18. Which header expresses the client's preference for an encrypted response?
  - _Upgrade-Insecure-Requests: 1_

19. Does the request have a user session associated with it?
  - _The session has not been established yet._

20. What kind of data is being sent from this request body?
  - _Login credntials were sent._

    ```bash
    username=bob
    password=password
    ```

**HTTP Response**

```HTTP
HTTP/1.1 200 OK
Date: Mon, 16 Mar 2020 17:05:43 GMT
Last-Modified: Sat, 01 Feb 2020 00:00:00 GMT
Content-Encoding: gzip
Expires: Fri, 01 May 2020 00:00:00 GMT
Server: Apache
Set-Cookie: SessionID=5
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type: NoSniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block

[page content]
```

21. What is the response status code?
  - _200_

22. What web server is handling this HTTP response?
  - _Apache webserver_

23. Does this response have a user session associated to it?
  - _Yes, Set-Cookie: SessionID=5_

24. What kind of content is likely to be in the [page content] response body?
  - _The code to the website, as seen in Content-Type: text/html_ (Text / HTML - Detail of the page configuration)_

25. If your class covered security headers, what security request headers have been included?
  - _HTTP Strict Transport Security (HSTS) - Strict-Transport-Security: max-age=31536000; includeSubDomains_
  - _X-Content-Type-Options HTTP - X-Content-Type: NoSniff_
  - _X-Frame-Options HTTP - X-Frame-Options: DENY_
  - _Cross Site Scripting Protection (X-XSS) - X-XSS-Protection: 1; mode=block_

#### Monoliths and Microservices

Answer the following questions about monoliths and microservices:

26. What are the individual components of microservices called?
  - _There are 8 core components:_
    - _Clients_
    - _Identity Providers_
    - _API Gateway_
    - _Messaging Formats_
    - _Databases_
    - _Static Content_
    - _Management_
    - _Service_

27. What is a service that writes to a database and communicates to other services?
  - _API_

28. What type of underlying technology allows for microservices to become scalable and have redundancy?
  - _Containers allow microservices to be scalable along with Load Balancing._

#### Deploying and Testing a Container Set

Answer the following questions about multi-container deployment:

29. What tool can be used to deploy multiple containers at once?
  - _Docker-compose_ used to deply multiple containers.
  - _`docker-compose up`_ used to launch the containers.

30. What kind of file format is required for us to deploy a container set?
  - _`YAML`_

#### Databases

31. Which type of SQL query would we use to see all of the information within a table called `customers`?
  - _SELECT * from customers;_
    - ```sql
      SELECT * from customers 
      where firstname='Bob' AND lastname='Smith';
      ```

32. Which type of SQL query would we use to enter new data into a table? (You don't need a full query, just the first part of the statement.)
  - _INSERT INTO customers;_
    - ```sql
      INSERT INTO customers (key_1,key_2,...) 
      VALUES ('value_1','value_2',...);
      ```

33. Why would we never run `DELETE FROM <table-name>;` by itself?
  - _This deletes the enire table if you include `where` then you can specify, with out the `where` the sql does not know which table(s) and deletes them all._

---

### Bonus Challenge Instructions: The Cookie Jar

First, using Docker Compose, navigate to the Day 1 WordPress activity directory and bring up the container set:

- `/home/sysadmin/Documents/docker_files`

Using `curl`, you will do the following for the Ryan user:

  - Log into WordPress and save the user's cookies to a cookie jar.

  - Test a WordPress page by using a cookie from the cookie jar.

  - Pipe the output from the cookie with `grep` to check for authenticated page access.

  - Attempt to access a privileged WordPress admin page.

---

Navigate to `~/Documents` in a terminal to save your cookies.

1. Construct a `curl` request that enters two forms: `"log={username}"` and `"pwd={password}"` and goes to `http://localhost:8080/wp-login.php`. Enter Ryan's credentials where there are placeholders.

    - **Question:** Did you see any obvious confirmation of a login? (Y/N)

2. Construct the same `curl` request, but this time add the option and path to save your cookie: `--cookie-jar ./ryancookies.txt`. This option tells `curl` to save the cookies to the `ryancookies.txt` text file.

3. Read the contents of the `ryancookies.txt` file.

   - **Question:** How many items exist in this file?

Note that each one of these is a cookie that was granted to Ryan after logging in.

#### Step 4: Log in Using Cookies

1. Craft a new `curl` command that now uses the `--cookie` option, followed by the path to your cookies file. For the URL, use `http://localhost:8080/wp-admin/index.php`.

   - **Question:** Is it obvious that we can access the Dashboard? (Y/N)

2. Press the up arrow on your keyboard to run the same command, but this time, pipe `| grep Dashboard` to the end of your command to return all instances of the word `Dashboard` on the page.

    - **Question:**  Look through the output where `Dashboard` is highlighted. Does any of the wording on this page seem familiar? (Y/N) If so, you should be successfully logged in to your Editor's dashboard.

#### Step 5: Test the Users.php Page

1. Finally, write a `curl` command using the same `--cookie ryancookies.txt` option, but attempt to access `http://localhost:8080/wp-admin/users.php`.

    - **Question:** What happens this time?

---

### Submission Guidelines

* Save the file where you documented your solutions and submit it as your homework deliverable. 

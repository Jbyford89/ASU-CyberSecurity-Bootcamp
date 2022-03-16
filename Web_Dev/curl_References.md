# cURL References

This is a reference sheet for your second activity but also the rest of this day's lesson.

## The cURL Syntax

### cURL

`cURL` is a tool to transfer data from or to a server, using one of the supported protocols without user interaction.

```bash
# Fetch HTML
curl example.com
```

This fetches the HTML for a web page using a GET request

```bash
# Views the request/response text
curl -v example.com
```

This views the request/response text by adding the `-v` flag


###

```bash
# View the response headers
curl -I example.com
```

This uses the `-I`  flag to view the response headers only.



###

```bash
# Setting a request type and URL
curl --request GET --url example.com
```

This explicitly sets a request type and URL with the `--request` and` --url` options


###

```bash
# Viewing available options
curl --help
```

- The `--help` flag shows all available options for cURL command.

###

```bash
# Send a GET request with parameters
curl --request https://example.com/get?parameter=value
```

- This sends a GET request to the /get endpoint with the indicated parameters. 

  - `-- request`: set the request type
  - `-- name`: your name
  - `-- location`: your current city


###

```bash
# Send a GET request with parameters and show both request and response headers
curl -v --request https://example.com/get?name=rodric&location=atlanta
```

- This sends a GET request to the /get endpoint with the following parameters: name, location but also prints out both request and response headers

  - `-v`: Show more detailed info like both request and response header.
  - `--request`: set the request type
  - `name`: your name
  - `location`: your current city


###

```bash
# Send a POST request with parameters
curl -v --request POST --url https://postman-echo.com/post --data 'name=<yourname>&location=<yourlocation>'
```

- This sends a POST request to the /post endpoint using the same data as query parameters before, but using cURL's --data option instead.

  - `--url` specific custom URL
  - `--data` specify parameters

```bash
# Send a GET request with request headers
curl -X --url https://httpbin.org/bearer -H 'authorization: {Type} {Credential}'
```

- This sends a GET request to the bearer endpoint for httpbin.org. You need to set the `type` of authorization and also the `credential`.

  - `-H`: Sets a request header
    

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.  

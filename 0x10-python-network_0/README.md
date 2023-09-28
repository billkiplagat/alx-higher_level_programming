# Python Networking

# Important Commands used
1. curl - is a command-line tool and library used for making HTTP requests to interact with web services and retrieve or send data over the internet. It can handle various protocols, not just HTTP, including FTP, SMTP, SCP, and more.

2. awk - is a text-processing tool that can process text or data line by line.

# Some common curl options:

-X, --request <HTTP_METHOD>: Specifies the HTTP method for the request (e.g., GET, POST, PUT, DELETE).

-H, --header <HEADER>: Adds custom HTTP headers to the request. You can use this option multiple times to add multiple headers.

-d, --data <DATA>: Sends data in the request body, typically used for HTTP POST requests. You can use it to send form data or JSON payloads.

-F, --form <DATA>: Similar to -d, but specifically used for sending form data as if it were submitted via an HTML form.

-o, --output <FILE>: Saves the response to a file instead of displaying it in the terminal.

-i, --include: Includes the HTTP response headers in the output.

-L, --location: Follows HTTP redirects automatically.

-c, --cookie <COOKIE_STRING>: Sends a specific cookie in the request.

-b, --cookie-jar <FILE>: Stores received cookies in a file for subsequent requests.

-A, --user-agent <USER_AGENT>: Specifies the User-Agent header to identify the client making the request.

-u, --user <USER:PASSWORD>: Provides HTTP basic authentication credentials.

--cert <CERT[:PASS]>: Specifies a client certificate file and optional password for SSL/TLS connections.

-k, --insecure: Disables SSL certificate verification, useful for testing with self-signed certificates (not recommended for production use).

-v, --verbose: Enables verbose mode, which displays detailed information about the request and response.

--url <URL>: Specifies the URL to send the request to.

-I, --head: Sends an HTTP HEAD request to retrieve only the headers of a resource.

--max-time <SECONDS>: Sets the maximum time allowed for the request to complete.

-X, --proxy <PROXY>: Specifies an HTTP proxy server to use for the request.

--compressed: Requests compressed content and automatically decompresses it.

--data-urlencode <DATA>: URL-encodes data for use in POST requests.

--upload-file <FILE>: Uploads a file as part of the request.

--limit-rate <RATE>: Limits the transfer rate of data in bytes per second.


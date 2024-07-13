# http.server
* `class http.server.BaseHTTPRequestHandler(request, client_address, server)`
    * Handle HTTP requests that arrive to server but must be subclassed to handle each request method like POST, GET

## Instance variables
* `client_address`
    * Tuple: `(host, port)` *client address*
* `server`
    * Instance
* `close_connection`
    * Boolean should be set before `handle_one_request()` returns. Indicating if another request may be expected.
* `command`
    * request type. Example: `'GET'`
* `path`
    * request path
* `headers`
    * Holds and instances of the class specified by the `MessageClass` class variable. This instances parses and manages the headers in the HTTP request. `parse_headers()` function from `http.client` is used to parse the headers and it requires that the HTTP request provide a valid RFC 2822 style heade
* `rfile`
    * An `io.BufferedIOBase` input stream, ready to read from the start of the optional input data
* `wfile`
    * Contains the output stream for writing a response back to the client. Proper adherences to the HTTP protocol must be used when writing to this stream in order to achieve successful interoperation with HTTP
    clients

## Attributes
* server_version
    * Specifies the server software version. Format: `'BaseHTTP/0.2`.
* sys_version
    * Contains the Python system version 
* Error_message_format
    * Specifies a format string that should be used by send_error() method for building an error response to the client. The string is filled by default with variables from `responses` based on the status code that passed to `send_error()`
* protocol_version
* MessageClass
    * Specifies an `email.message.Message`-like class to parse HTTP headers. Typically, this is not overridden, and it defaults to `http.client.HTTPMessage`
* responses
    * This attr contains mapping of error code integers to two-element tuples containing a short and long message. For example: `{code: (shortmessage, longmessage)}` (key: exaplain key)
    * it is used by `send_response_only()` and `send_error()`

## Methods
* `handle()`
    * Class `handle_one_request()` once or multiple times *(persistences)* to handle incoming HTTP requests. You should never need to override it; instead, implement appripiate do_*() methods
* `handle_one_request()`
    * This method will parse and dispath the request to the appropiate do_*() **You should never need to override it**
* `handle_expect_100()`
    * Whenan HTTP conformant server receives and `Expect: 100-continue` request, it responds back with a `100 Continue` followed by `200 OK` headers. This method can be overriden to raise an error if the server does not want the client to continue. For example: server can choose to send `417 Expectation Failed` as a response header and return `False`
* `send_error(code, message=None, Explain=None)`
    * Sends and logs a complete error reply to the client
        + code: *HTTP error code*
        + message: short human readable description
        + explain: more detail information
* `send_response(code, message=None)`
    * Adds a response header to the headers buffer and logs the accepted requests
* `send_header(keyword, value)`
    * Adds the HTTP header to an internal buffer which will be written to the output stream when either `end_headers()` or `flush_headers()` is invoked
* `send_response_only(code, message=None)`
    * Used for porpuses when `100 continue` response is sent by the server to the client.
* `end_headers()`
    * Adds a black line (indicating the end of the HTTP header response)
* `flush_headers()`
    * Finally send the headers to the output stream and flush the internal headers buffer.
* `log_request(code='-', size='-')`
    * Logs an accepted (successfull) request.
    * code should specify the numeric HTTP code associated with the response. If a size of the response is available, then it should be passed as the size parameter.
* `log_message(format, ...)`
    * Logs an arbitraty message to `sys.stderr`
    * This is typically overridden to create custom error loggin mechanisms
* `version_string()`
    * Returns the server software version string
* `date_time_string(timestamp=None)`
    * Returns the date and time given by timestamp (which must be None or in the format returned by time.time()), formatted for a message header. If timestamp is omitted, it uses the current date and time.
* `log_date_time_string()`
    * Returns the current date and time
* `address_string()`
    returns the client address.
# `class http.server.SimpleHTTPRequestHandler(request, client_address, server, directory=None)`
    * This class serves files from the directory directory and below, or the current directory if directory is not provided, directly mapping the directory structure to HTTP requests.
## class-level attributes
* `server_version`
* `extensions_map`
    * A dictionary mapping suffixed into MIME types, contains custom overrides for the default system mappings. The mapping is used case-insensitively, and so should contain only lower-cased keys.
* `do_HEAD()`
    * This method serves the `'HEAD'` request type: it sends the headers it would send for the equivalent `'GET'` request
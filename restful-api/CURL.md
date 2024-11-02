# How to use CURL
## HTTP GET request
`curl https://flaviocopes.com/`
## HTTP response headers
`curl -i https://flaviocopes.com/`
## Only get HTTP response headers
`curl -I https://flaviocopes.com/`
## HTTP POST request
`curl -X GET https:://flaviocopes.com/`
### HTTP POST request passing data
`curl -d "option=value&something=anothervalue" -X POST https://flaviocopes.com/`
## HTTP POST request sending JSON
`curl -d {"option": "value", "something": "anothervalue"} -H "Content-Type: application/json" -X POST https://flaviocopes.com/`
### send JSON file from disk
`curl -d "@my-file.json" -X POST http://flaviocopes.com/`
## HTTP PUT request
`curl -X PUT https://flaviocopes.com/`
### Follow a redirect
* A redirect response like 301, which specifies the `Location` response header, can be automatically followed by specifying the `L` option 
`curl -L http://flaviocopes.com/`
## Store the response to a file
`o`: output
`curl -o file.html https://flaviocopes.com/`
### Can also save a file by its name on the server with `O`
`curl -O https://flaviocopes.com/index.html`
## HTTP authentication
`curl -u user:pass https//flaviocopes.com`
## Set a different User Agent
`curl --user-agent "my-user-agent" https://flaviocopes.com`
## Inspecting details of the request and the response
`curl --verbose -I https://flaviocopes.com/`
```
*   Trying 178.128.202.129...
* TCP_NODELAY set
* Connected to flaviocopes.com (178.128.202.129) port 443 (#0)
* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
* Server certificate: flaviocopes.com
* Server certificate: Let's Encrypt Authority X3
* Server certificate: DST Root CA X3
> HEAD / HTTP/1.1
> Host: flaviocopes.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
HTTP/1.1 200 OK
< Cache-Control: public, max-age=0, must-revalidate
Cache-Control: public, max-age=0, must-revalidate
< Content-Type: text/html; charset=UTF-8
Content-Type: text/html; charset=UTF-8
< Date: Mon, 30 Jul 2018 08:08:41 GMT
Date: Mon, 30 Jul 2018 08:08:41 GMT
...
```
## Copying any browser network request to a curl command
* When inspecting any network request using the **Chrome Developer Tools**, you have the option to copy that request to a curl request `copy as cURL`:
`curl 'https://github.com/curl/curl' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Upgrade-Insecure-Requests: 1' -H 'DNT: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Referer: https://www.google.it/' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,it;q=0.8' -H 'Cookie: _octo=GH1.1.933116459.1507545550; _ga=GA1.2.643383860.1507545550; tz=Europe%2FRome; user_session=XXXXX; __Host-user_session_same_site=YYYYYY; dotcom_user=flaviocopes; logged_in=yes; has_recent_activity=1; _gh_sess=ZZZZZZ' --compressed`
# URL's
## Name and Password
* `curl ftp://user:password@example.com/`
*If you want a non-ASCII letter or maybe a : or @ as part of the username and/or password, remember to URL encode that letter: write it as %HH where HH is the hexadecimal byte value. : is %3a and @ is %40.*
## Query
The query part of a URL is the dat that is to the right of a question mark (?) but to the left of the *fragment*, which begins with a hash (#). <br />
*Can be any string as long as they are URL encoded* <br />
**Best practice**: sequence of key/value pairs separated by (`&`) added by curl
* `https://example.com/?name=daniel&tool=curl`
* Using `--url-quert [content]` adds the provided content to the end of the privided url.
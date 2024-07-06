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

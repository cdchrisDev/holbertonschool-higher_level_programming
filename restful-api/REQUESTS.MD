# Requests Python Module
```
import requests

r = requests.get('https://api.github.com/events) # r is now a response obj
```
* HTTP POST request:
`r = requests.post('https://httpbin.org/post', data={'key': 'value'})`
* HTTP request types:
```
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
```
## Passing parameters in URL's
* Request allows you to privided them using `params` keyword
```
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(https://httpbin.org/get', params=payload)
print(r.url)
```
    * `https://httpbin.org/get?key2=value2&key1=value1`
*Any dict key whose value is None will not be added to the URL's query string*
## Response Content
* read the content of the server's response
`r.text` **See content**
`r.encoding` **See encoding**
`r.encoding = 'ISO-8859-1'` **Change Encoding**
## Binary response
```
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))
```
## JSON response content
```
r = requests.get('https://api.github.com/events')
r.json()
```
*To check if the request is successful, use `r.raise_for_status()` or `r.status_code`*
## Raw response Content
```
r = requests.get('https://api.github.com/events', stream=True)
r.raw
```
* `<urllib3.response.HTTPResponse object at 0x101194810>`
* `r.raw.read(10)`
    * `b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'`
*You should use a pattern like this to save what is being streamed to a file*:
```
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
Using `Response.iter_content` will handle a lot of what you would otherwise
have to handle when using `Response.raw` directly. When streaming a download, the above is the preferred and recommended way to retrieve the content. `chunk_size` can be freely adjusted to a number that may better fit your use cases
# Note
An important note about using `Response.iter_content` versus `Response.raw. Response.iter_content` will automatically decode the `gzip` and `deflate` transfer-encodings. `Response.raw` is a raw stream of bytes – it does not transform the response content. If you really need access to the bytes as they were returned, use `Response.raw`.
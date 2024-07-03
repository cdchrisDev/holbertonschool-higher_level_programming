# This is restful api Python Module
## Introduction
The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.
## Learning Objectives
1. **HTTP/HTTPS Basic**: Understanding principles of the web's primary protocol, how data transfer occurs and the differences between both
2. **API Consumption with Command Line**: Hands-On experience in interacting with API's using command-line tools
3. **API Consumption with Python**: Implement different data fetching techniques for more advance proccessing and data manipulation
4. **API Development with `http.server`**: Understand the basics of crafting and API from scratch using Python's built-in modules.
5. **API Development with Flask Framework**: Focusing on routing, data management and scalability. `Flask` is meant to make something robust, professional and stable no matter how big can be.
6. **API Security & Authentication**: Address the crusial aspects of security, knowing how to protect data transactions and ensure only authorized access to resources
7. **API Standards & Documentation with OpenAPI**: standardized documentation is important to delivery API usage, understand and mantain the projects
# Tasks
## 00
### Objective:
At the end of this exercise, students should be able to:
1. Differentiate between HTTP and HTTPS.
2. Understand the basic working and structure of HTTP requests and responses.
3. Recognize and explain the common HTTP methods and status codes.
## Resources:
1. [Mozilla Developer Network (MDN) - An Overview of HTTP](https://intranet.hbtn.io/rltoken/BKDRX5JLz6CKgQqC8HiUAA)
2. [Difference between HTTP and HTTPS](https://intranet.hbtn.io/rltoken/ZM7mVhUBk2rRPkpsNh56HA)
3. [List of HTTP status codes](https://intranet.hbtn.io/rltoken/vAPbpS8hUG2BFS4RcGx1WQ)
### Expected Output
1. A brief summary explaining the differences between HTTP and HTTPS.
	* HTTP *(Hypertext transfer protocol)* Is a technology that power almost every communication on the internet, and the other version HTTPS, it's an extension of HTTP that encrypts every transaction made.
2. A depiction or outline of the structure of an HTTP request and response.
	
3. Lists of common HTTP methods and status codes with their descriptions and possible use cases. For example:
* **GET: Read**
	+ 200 (OK) list of entities. Use pagination, sorting and filtering to navigate big lists.
	+ 404 (Not found)
* **POST: Create**
	+ 201 (Created), Response contains response similar to GET /user/{id} containing new ID.
* **PATCH: Update**
	+ [Batch API](https://doc.oroinc.com/api/batch-api/#web-services-api-batch-api)
* **DELETE: Delete**
	+ 204 (No Content).
	+ 400 (Bad Request) if no filter is specified.
* **PUT: Create/Replace**
## 01
### Objective:
1. install and use `curl` from the command line
2. Construct and execute basic API requests using `curl`, including setting headers and inspecting output.
3. Interpret the results of common API request
## Resources
1. [curl - Everything curl](https://intranet.hbtn.io/rltoken/eFoZ3X1pF42IdfyzLC3M3A)
2. [Using curl to interact with HTTP API's](https://intranet.hbtn.io/rltoken/ieEz_6p00Tv67oobkwYHTA)
3. Public API to Play with: [JSONPlaceholder](https://intranet.hbtn.io/rltoken/Ut3d3Tzd0l_sH0evg3GiMg)
### Expected Output:
1. Upon running `curl --version` and see supported protocols
	* **curl** supports these protocols: DICT, FILE, FTP, FTPS, GO-
       PHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS,
       SMTP, SMTPS, TELNET or TFTP. The command is designed to work without user interaction
2. Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like `userID`, `id`, `title` and `body`
3. Fetching only headers should give a concise output showing status codes and headers without the actual content.
4. Making POST request should yield a response from the server acknowledging the reception of the data.
for JSONPlaceholder, it typically returns the created post with and `id` of `101` (since it doesn't actually save the new post, but simulates the creation)

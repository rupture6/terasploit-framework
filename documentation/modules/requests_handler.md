# Requests Handler

## Metadata
- Module: Auxiliary
- Version: 1.0
- Author: Handler4
- Name: HTTP Requests Handler via Yaml Config

## Description
This module is made for handling http requests by reading yaml config file to gather requests contents. It can also be use to exploit a target with web vulnerabilities such as remote code execution. It can upload a shell on the target but it will not start a session automatically. To start a session, you will need to use an exploit module (exploit/multi/handler. You will need multi_handler exploit module to start a session.

## Config Format
Content is the main key for reading the config format so be sure that content key is not missing in config.yml file.
```
content: {
  "method" : "get",
  "url" : "http://www.google.com:80",
  ... : ...
}
```
### List of available options
- method - the http request method
- url - the url of the request
- params - parameter values
- data - A dictionary, list of tuples, bytes or a file object to send to the specified url.
- headers - A dictionary of HTTP headers to send to the specified url.
- cookies - A dictionary of cookies to send to the specified url.
- files - A dictionary of files to send to the specified url
- auth - A tuple to enable a certain HTTP authentication.
- timeout - A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
- proxies - A dictionary of the protocol to the proxy url.
- verify - A Boolean or a String indication to verify the servers TLS certificate or not.
- cert - A String or Tuple specifying a cert file or key.
- stream - A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
- json - A JSON object to send to the specified url

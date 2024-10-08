## Metadata
- License => Terasploit Framework License (BSD)
- Module => Auxiliary
- Name => HTTP Requests Handler via Yaml Config
- Version => 1.0

## Description
Versatile module that allows a user to use requests library for web exploitation via yaml file config

## Basic Options
```
tsf auxiliary(http/requests_handler) > show options

Auxiliary options (auxiliary/http/requests_handler):

   Name      Current Settings  Required  Description
   ────      ────────────────  ────────  ───────────
   CONFIG                      yes       yaml config to read
   SESSION   false             yes       use http request session



To view the full module information, use 'info <path>' command.

tsf auxiliary(http/requests_handler) >
```

## Config Format
Content is the main key for reading the config format so be sure that content key is not missing in config.yml file.
```
content: {
  "method" : "get",
  "url" : "http://www.google.com:80",
  ... : ...
}
```
### Config Keys
- `method` - The http request method
- `url` - The url of the request
- `params` - A dictionary, list of tuples or bytes to send as a query string.
- `data` - A dictionary, list of tuples, bytes or a file object to send to the specified url.
- `headers` - A dictionary of HTTP headers to send to the specified url.
- `cookies` - A dictionary of cookies to send to the specified url.
- `files` - A dictionary of files to send to the specified url
- `auth` - A tuple to enable a certain HTTP authentication.
- `timeout` - A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
- `proxies` - A dictionary of the protocol to the proxy url.
- `verify` - A Boolean or a String indication to verify the servers TLS certificate or not.
- `cert` - A String or Tuple specifying a cert file or key.
- `stream` - A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
- `json` - A JSON object to send to the specified url

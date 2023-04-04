This project is an attempt to build a browser in python, following the steps laid out in the Web Browser Engineering website here: https://browser.engineering/

For the first commit, I followed the steps in chapter one: https://browser.engineering/http.html

1. Parse URL from command line argument
2. Open websocket and connect to website
3. Send HTTP request
4. Download response
5. Parse headers
6. Iterate over the body and print out content between angle brackets

You can run this script by passing a URL as the argument: `python src/browser.py http://example.org/index.html`.

It prints the website text to the console.

- Currently, this only works for HTML 1.0. Does not work for HTML/1.1 or HTML/2
- Does not handle HTTPS. This is what I'm planning on doing next!
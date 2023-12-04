<!-- @format -->

### Networking applications

- HTTP protocol
- Browser
- Client
- Endpoints

### Python

- Interpreted

  - Global Interpreter Lock

    - Thread
    - Multiple thread
      - Threads share interpreter
      - GIL serializes threads
        - slow due to having to wait for locks to get out
        - solution is to use multiple GILs so threads are used in isolation
    - Memory location

  - CPython
    - Source code > feed to engine (v8) > to byte code
  - Don't need complie over and over again

- Complied
  - Just in time compliation
  - Target specific CPU (ARM, M2, etc) and change to machine code for that CPU, after it is processed
  - Stack | Heap > Execution
    - stack
    - heap
    - execution

### HTTP Protocol

- Universal
- Listen on a port
- accept request
- send responds
- handlers
- Methods
  - Get
    - read only
  - Post
    - changes information on server
  - Put
    - Updated inforamtion on server
  - URL
  - Query parameters
  - Resources parameters

### Tornado (applying HTTP Protocol)

- handlers
  - tornado.web.RequestHandler
  - class that has functions to run when hitting that endpoint
- write vs render
  - render: HTML files
  - write: plain text
- tornado.web.Application
  - takes array of tuples with path and handler
  - listen
- tornado.ioloop.IOLoop.current().start()
  - handle async events

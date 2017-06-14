# Coding Style

1. Always sse `os.path` for handling file paths
1. [IO sandwich](http://www.perrygeo.com/processing-vector-features-in-python.html): 
    split up functions into three functions: (1) file input, (2) processing 
    (e.g. take numpy, return numpy), and (3) file output.

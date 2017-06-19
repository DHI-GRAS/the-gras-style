# Coding Style


## Style

1. Follow most of the [guidelines in PEP 0008](https://www.python.org/dev/peps/pep-0008/).
    Use a Python linter (preferably `flake8`-powered) to help you with that.
1. [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)
1. We do not strictly stay within 80 characters, but 
    lines should not be longer than **100** characters.
1. Write docstrings for all public functions and write them in 
    [Numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) format.


## Other guidelines

1. Always use `os.path` for handling file paths - never split by literal slashes or so.
1. [IO sandwich](http://www.perrygeo.com/processing-vector-features-in-python.html): 
    split up functions into three functions: (1) file input, (2) processing 
    (e.g. take numpy, return numpy), and (3) file output.
1. Be conscious of what you expect and raise descriptive exceptions when you do not get it, e.g.
```python
pattern = '/path/*.ext'
infiles = glob.glob(pattern)
if not infiles:
    raise RuntimeError('No files found with pattern \'{}\'.'.format(pattern))
```

# So, you want to learn about The GRAS Style ...

## Python Specifics

### General coding style

1. Follow the [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/).
1. The only exception to PEP8: Lines may be up to 100 columns wide.
1. Use the Python linter `flake8` and make sure there are no violations (plugins are available for most editors).
1. Many reasonable suggestions are found in [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html). Read it carefully, and violate it only in exceptional circumstances.
1. Write docstrings for all public functions, in
    [Numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) format.
1. Use descriptive names. Avoid abbreviations for anything that isn't an acronym.


### House rules

1. Always use `os.path` for handling file paths - never split e.g. by literal slashes.
1. Consider using the [IO sandwich](http://www.perrygeo.com/processing-vector-features-in-python.html) pattern:
    split up functions into three functions: (1) file input, (2) processing
    (e.g. take numpy, return numpy), and (3) file output.
1. Defensive programming: Be conscious of what you expect and raise descriptive exceptions when you do not get it, e.g.
```python
pattern = '/path/*.ext'
infiles = glob.glob(pattern)
if not infiles:
    raise RuntimeError('No files found with pattern \'{}\'.'.format(pattern))
```
1. Use the modern `rasterio` and `fiona` instead of the old `gdal` and `ogr` Python bindings.

### Package architecture

1. Think carefully before adding a dependency to a repository that is not in pure Python. Every dependency you add will lead to larger environments, longer installation time, and additional maintenance on updates. If you include a big library and end up using just a small part of it, think triple carefully. Rule of thumb: Adding a library for the purpose it was written for is usually okay.
1. Don't be shy to create a separate repository for new, powerful, re-usable features if you deem it necessary. However, keep in mind that every repository must at least have a proper `README` file, and scattering functionality across repositories does make installation and maintenance somewhat more cumbersome. Rule of thumb: Refrain from creating a new repository until you want to use the feature from at least two different projects.

## Git workflow

1. If there is more than one person working on the repository, do not commit directly into `master` (except hotfixes or when changing less than 10 lines of code).
2. If you contribute code to a repository that has CI (*Continuous Integration*, e.g. through Travis CI) set up, you *must* create a Pull Request to commit to `master`.
3. Merge as often as possible, especially when multiple people are working on the same repository.
4. Inform your collaborators before major refactoring operations.
5. Prefix Pull Requests that are work in progress with `WIP`. Remove the `WIP` label before merging. Do not merge Pull Requests with the `WIP` label.
6. Only squash commits in exceptional circumstances (e.g. after doing many small changes that were reversed later on).

## Testing

1. If you contribute code to a repository that has CI set up, you *must* at least write one test for your code (could be as simple as 'code runs without crashing').
2. If you contribute code to a repository that also measures code coverage, your addition must not decrease coverage (unless in rare cases, e.g. when some code is untestable).

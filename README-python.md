# Python

## General coding style

1. Follow the [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/).
1. The only exception to PEP8: Lines may be up to 100 columns wide.
1. Use the Python linter `flake8` and make sure there are no violations (plugins are available for most editors).
1. Many reasonable suggestions are found in [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html). Read it carefully, and violate it only in exceptional circumstances.
1. Write [docstrings](https://sphinxcontrib-napoleon.readthedocs.io) for all public functions, in
   [Numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) format.
1. Use concise and descriptive names. Avoid abbreviations for anything that isn't an acronym.
1. Khan Academy's [style guide](https://github.com/Khan/style-guides/blob/master/style/python.md) is very similar to ours and a bit more elaborate
1. We have not yet decided on hand-crafted PEP8/flake8 vs [Black](https://github.com/psf/black) yet. But do either.

## House rules

1. Python >=3.6 only.
1. Use [`pathlib`](https://docs.python.org/library/pathlib.html) for handling file paths - never split e.g. by literal slashes.
1. Consider using the [IO sandwich](http://www.perrygeo.com/processing-vector-features-in-python.html) pattern:
   split up tasks into three functions: (1) file input, (2) processing
   (e.g. take numpy, return numpy), and (3) file output.
1. Defensive programming: Be conscious of what you expect and raise descriptive exceptions when you do not get it, e.g.
   ```python
   infiles = list(Path('/path').glob('*.ext'))
   if not infiles:
       raise RuntimeError('No files found with pattern \'{}\'.'.format(pattern))
   ```
1. Use `rasterio` and `fiona` instead of the old `gdal` and `ogr` Python bindings.
1. Always use the Python [format string](https://docs.python.org/3/library/string.html#format-string-syntax) instead of the old `%` syntax or `+str(something)+`.

## Dependencies

1. Think carefully before adding a dependency that is not in pure Python to a repository. Every dependency you add will lead to larger environments, longer installation time, and additional maintenance on updates. If you include a big library and end up using just a small part of it, think triple carefully. Rule of thumb: Adding a library for the exact purpose it was written for is usually okay.
1. Don't be shy to create a separate repository though for new, powerful, re-usable features if you deem it necessary. Keep in mind that every repository must at least have a proper `README` file, and scattering functionality across repositories does make installation and maintenance somewhat more cumbersome.
1. Rule of three: Refrain from splitting moving code a separate package / module until you want to use the feature from at least [three](<https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)>) different projects.

## Packaging and releases

1. Keep to the latest package structure
1. Consider using `setup.cfg` or `pyproject.toml` for static info
1. Use [`setuptools-scm`](https://github.com/pypa/setuptools_scm/) and (semantic) versions from tags (see Git workflow)
1. Automate the release

# Compatibility

When designing your package, assume as little as possible about the system that is used to run it. You _must not_ assume a certain folder structure. You _may_ assume a certain target OS, if keeping your code multi-platform compliant would impose an unreasonable amount of extra maintenance.

If your code does not run on other systems, it is worthless.

# Command Line Interfaces (CLI)

A good CLI is crucial to the usability and thus success of your package, but also one of the hardest things to get right. There is no silver bullet, but these general guidelines may help:

1. Use a sophisticated, well-established library to handle the CLI for you. For Python, we prefer `click`.
1. Follow the conventions set by the GNU toolchain:

   1. Arguments specified with a single `-` may only be followed by a single character; otherwise, use `--`.

      - Good: `-i` and `--input`
      - Bad: `-in` or `--i`.

   1. Use hyphens to split words in your arguments:
      - Good: `--input-folder`
      - Bad: `--inputfolder` or `--input_folder`.

1. Make proper use of flags and multi-argument commands. `--debug` is better than `--debug=True`. `--input-files 1.tif 2.tif 3.tif` is better than `--input-files 1.tif,2.tif,3.tif`. If the former is not possible due to technical reasons, use `-i 1.tif -i 2.tif -i 3.tif`.
1. Write expressive help messages. Include default values for arguments.

Also, think whether you need a CLI at all. Is your package just a Python wrapper around a command line tool? Chances are, you will be better off calling the command line tool in question directly, and maybe just do some pre-processing in Python. Python is generally good "glue", but there are better choices for large workflows ([Snakemake](http://snakemake.readthedocs.io/en/stable/) can be a good choice for that).

# Testing

1. If you contribute code to a repository that has continuous integration (CI) set up, you _must_ at least write one test for your code (could be as simple as "code runs without crashing").
1. If you contribute code to a repository that also measures code coverage, your addition must not decrease coverage. If your code is _inherently untestable_ for technical reasons, you may use `# pragma: no cover` to exclude a certain branch or function from coverage reports.

# How we write Snakefiles :snake:

1. The most important aspect when writing Snakefiles is to make sure that a rule may only succeed if it actually succeeded (that is, to minimize false positive executions), and to never modify products in-place. A workflow that strictly adheres to these rules will never leave the data storage in a corrupted state. It is therefore critical to test your assumptions about the output products of a rule before exiting, e.g. by asserting that files were actually created (and contain meaningful data). We call this _defensive rule writing_.
1. Snakefiles should be as self-contained as possible. One of the strengths of Snakemake is that it is very transparent how products are created; an advantage that is nullified if too much logic is moved outside the Snakefile.
1. When using directories as outputs (via the `directory` directive), it is often useful to add a rule that "scatters" the directory contents to make them visible to Snakemake. These scatter rules take the created directory as input and outputs the products that are required downstream without modifying them.
1. Make sure that your rules do not leave any temporary files behind. The `shadow` directive can be helpful to enforce this.
1. Add a graphical version of your workflow to the README (via `snakemake --rulegraph | dot -Tpng -o graph.png`)
1. Group output folder trees by product, not by scene (i.e., `cloudmask/{scene_id}`, `extracted/{scene_id}` instead of `{scene_id}/cloudmask` and `{scene_id}/extracted`).

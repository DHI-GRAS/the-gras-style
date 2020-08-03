# So, you want to learn about The GRAS Style ...

This document contains some of the general guidelines we at DHI GRAS have agreed upon. Read it carefully, follow it, and extend it where necessary.
For specifics on the front-end style check out section [Frontend](#frontend)

If you don't understand something, or are unsure how to design your software, talk to people. Good software is an amalgamation of opinions, a common, balanced denominator of as many use cases as possible. Discussions are a requirement to achieve this.

## Python Specifics

### General coding style

1. Follow the [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/).
1. The only exception to PEP8: Lines may be up to 100 columns wide.
1. Use the Python linter `flake8` and make sure there are no violations (plugins are available for most editors).
1. Many reasonable suggestions are found in [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html). Read it carefully, and violate it only in exceptional circumstances.
1. Write [docstrings](https://sphinxcontrib-napoleon.readthedocs.io) for all public functions, in
   [Numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) format.
1. Use concise and descriptive names. Avoid abbreviations for anything that isn't an acronym.
1. Khan Academy's [style guide](https://github.com/Khan/style-guides/blob/master/style/python.md) is very similar to ours and a bit more elaborate
1. We have not yet decided on hand-crafted PEP8/flake8 vs [Black](https://github.com/psf/black) yet. But do either.

### House rules

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

### Dependencies

1. Think carefully before adding a dependency that is not in pure Python to a repository. Every dependency you add will lead to larger environments, longer installation time, and additional maintenance on updates. If you include a big library and end up using just a small part of it, think triple carefully. Rule of thumb: Adding a library for the exact purpose it was written for is usually okay.
1. Don't be shy to create a separate repository though for new, powerful, re-usable features if you deem it necessary. Keep in mind that every repository must at least have a proper `README` file, and scattering functionality across repositories does make installation and maintenance somewhat more cumbersome.
1. Rule of three: Refrain from splitting moving code a separate package / module until you want to use the feature from at least [three](<https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)>) different projects.

### Packaging and releases

1. Keep to the latest package structure
1. Consider using `setup.cfg` or `pyproject.toml` for static info
1. Use [`setuptools-scm`](https://github.com/pypa/setuptools_scm/) and (semantic) versions from tags (see Git workflow)
1. Automate the release

## Compatibility

When designing your package, assume as little as possible about the system that is used to run it. You _must not_ assume a certain folder structure. You _may_ assume a certain target OS, if keeping your code multi-platform compliant would impose an unreasonable amount of extra maintenance.

If your code does not run on other systems, it is worthless.

## Command Line Interfaces (CLI)

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

## Version Control (Git)

### Repository creation

1. Create public repositories whenever possible. But make sure they are tidy.
1. Naming: Prefer dashes `-` over underscores `_` in repo names (e.g. `my-python-package.git/my_python_package/__init__.py`).

### Git workflow

1. Great commit messages are short (<=50 chars) and generally start with capitalized action words in imperative ("Add feature X", "Improve performance" rather than "Added ..." or "Fixes ...").
1. Write issues before you start to fix something and take the description seriously.
1. Always create feature branches and PRs, even for small fixes (except maybe changing a line in the docs or so). Use `Closes #1` or `Fixes #1` or [similar](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to link issues to the pull request. You can also use these keywords in commit messages to close issues automatically.
1. Please always write in the Pull Request title what you are fixing and write a short description, even if it is just one sentence.
1. When applicable, link the PR to one or more issues that it addresses, fixes or closes (pls note the difference). You may know this, but you can use [magic keywords](https://help.github.com/en/enterprise/2.16/user/github/managing-your-work-on-github/closing-issues-using-keywords) like `Fixes #3` or `Closes #4` in the description and GH will link the issues to the PR and close them when the PR is merged. These also work in commit messages, but don't overuse.
1. Open Pull Requests that are work in progress as Draft Pull Requests first.
1. A nice thing for large PRs is also to include Markdown check box lists (`- [x] tick this off`) to keep track of what you intend to include with the PR and how far you got.
1. Only squash commits in exceptional circumstances (e.g. after doing many small changes that were reversed later on).
1. Only maintainers of a code base may assign issues and pull requests to other maintainers, add tags, and merge pull requests.
1. Merge as often as possible, especially when multiple people are working on the same repository.
1. Use git tags for ([semantic](https://semver.org/)!) versioning and tag frequently, e.g. `v1.0.0`, `v2.0.0-beta1` or `v3.0.0-rc1`.

## Testing

1. If you contribute code to a repository that has continuous integration (CI) set up, you _must_ at least write one test for your code (could be as simple as "code runs without crashing").
1. If you contribute code to a repository that also measures code coverage, your addition must not decrease coverage. If your code is _inherently untestable_ for technical reasons, you may use `# pragma: no cover` to exclude a certain branch or function from coverage reports.

## How we write Snakefiles

1. The most important aspect when writing Snakefiles is to make sure that a rule may only succeed if it actually succeeded (that is, to minimize false positive executions), and to never modify products in-place. A workflow that strictly adheres to these rules will never leave the data storage in a corrupted state. It is therefore critical to test your assumptions about the output products of a rule before exiting, e.g. by asserting that files were actually created (and contain meaningful data). We call this _defensive rule writing_.
1. Snakefiles should be as self-contained as possible. One of the strengths of Snakemake is that it is very transparent how products are created; an advantage that is nullified if too much logic is moved outside the Snakefile.
1. When using directories as outputs (via the `directory` directive), it is often useful to add a rule that "scatters" the directory contents to make them visible to Snakemake. These scatter rules take the created directory as input and outputs the products that are required downstream without modifying them.
1. Make sure that your rules do not leave any temporary files behind. The `shadow` directive can be helpful to enforce this.
1. Add a graphical version of your workflow to the README (via `snakemake --rulegraph | dot -Tpng -o graph.png`)
1. Group output folder trees by product, not by scene (i.e., `cloudmask/{scene_id}`, `extracted/{scene_id}` instead of `{scene_id}/cloudmask` and `{scene_id}/extracted`).

## Frontend (#frontend)
Our front-end style guide is based on the [Airbnb JS style guide](https://github.com/airbnb/javascript) and [Airbnb React style guide](https://github.com/airbnb/javascript/tree/master/react). A selection of points are highlighted below. For any other questions consider the [Airbnb React style guide](https://github.com/airbnb/javascript/tree/master/react).

### IDE
Use [VSCode](https://code.visualstudio.com/)

### Repositories
When initiating new repositories use `-` to seperate words and append `-app` as trailing.
Fx `global-seas-app`

### React
Use functional components with hooks.

### Package manager
Use `yarn` 

### Linting
Use prettier in the VSCode IDE for linting. Currently we use these linting settings:

``` 
module.exports = {
  trailingComma: 'es5',
  tabWidth: 2,
  semi: true,
  singleQuote: true,
};
```

### ES6+
Use ES6+ as much as possible. This includes:
- Using `const` and `let` instead of var
- Using arrow functions as much as possible

### Naming
Take your time to think of descriptive names for variables and functions. 
Aim for keeping the namings short but dont compromise on clarity. fx `setSnowCoverData` is fine.

Use `PascalCasing` for your components and classes. use `camelCasing` for your objects, functions, and instances.

### Alphabetical order
When importing dependecies add them to the top of your page and in alphabetical order.
When using lists of props put them in alphabetical order

### Folder structure
When making components create a folder for each component and export this component from the index.js fx:
``` 
Map 
- index.js 
- Map.js 
```

When structing your React projects put your components in the `src` folder and subsquently create a `components` and `containers` folder.
The `container` folder can be used for fx `Sidebar`, `SidebarControl`, `Map` and `Landingpage`. Create `partials` folder inside these components for components that are used within these containers, and feel free to nest partials:
```
Map 
- partials
	- GeoJsonLayer
	- RasterLayer
	- MapControls
		- partials
			- ZoomControl
			- SearchControl
```
Use the 'components' folder for components that are shared accross the application.



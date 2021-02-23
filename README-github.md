# Social Coding (Git and GitHub)

## Repository creation

1. Create public repositories whenever possible. But make sure they are tidy.
2. Open Source is only open if you [add](https://docs.github.com/en/enterprise-server@3.0/github/building-a-strong-community/adding-a-license-to-a-repository) a corresponding license. Default to MIT.
3. Naming: Prefer dashes `-` over underscores `_` in repo names (e.g. `my-python-package.git/my_python_package/__init__.py`).

## Git workflow

1. Great commit messages are short (`<=50` chars) and generally start with capitalized action words in imperative ("Add feature X", "Improve performance" rather than "Added ..." or "Fixes ...").
1. Write issues before you start to fix something and take the description seriously.
1. Always create feature branches and PRs, even for small fixes (except maybe changing a line in the docs or so). Use `Closes #1` or `Fixes #1` or [similar](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to link issues to the pull request. You can also use these keywords in commit messages to close issues automatically.
1. Please always write in the Pull Request title what you are fixing and write a short description, even if it is just one sentence.
1. When applicable, link the PR to one or more issues that it addresses, fixes or closes (pls note the difference). You may know this, but you can use [magic keywords](https://help.github.com/en/enterprise/2.16/user/github/managing-your-work-on-github/closing-issues-using-keywords) like `Fixes #3` or `Closes #4` in the description and GH will link the issues to the PR and close them when the PR is merged. These also work in commit messages, but do not overuse.
1. Open Pull Requests that are work in progress as Draft Pull Requests first - if we have those, else mark them with `WIP` in the title.
1. A nice thing for large PRs is also to include Markdown check box lists (`- [x] tick this off`) to keep track of what you intend to include with the PR and how far you got.
1. Only squash commits in exceptional circumstances (e.g. after doing many small changes that were reversed later on).
1. Only maintainers of a code base may assign issues and pull requests to other maintainers, add tags, and merge pull requests.
1. Merge as often as possible, especially when multiple people are working on the same repository.
1. Use git tags for ([semantic](https://semver.org/)!) versioning and tag frequently, e.g. `v1.0.0`, `v2.0.0-beta1` or `v3.0.0-rc1`.


## Raising issues

Well written issues are always welcome, even when you are not 100% sure about their relevance. 

Write a descriptive title stating
* the bug: "App breaks when hit with X"
* the question: "How to do Y?"
* the feature request: "Add function to perform task Z"

In the issue description, write what you expect and justify why. If it is a bug report, be as clear as possible 
about when you encountered the issue. If possible, provide a [Minimal Workable Example (MWE)](https://stackoverflow.com/help/minimal-reproducible-example) 
so other developers can try reproducing your issue. Often you will actually figure out the cause of your issue while stripping down your code to an MWE.

Please note: Adding labels and assignment are for maintainers only. On most repos where you are not maintainer, 
you will not be able to add labels or assign issues to someone. But if you can - leave it to the maintainers, as
they might have some internal logic and workflow.

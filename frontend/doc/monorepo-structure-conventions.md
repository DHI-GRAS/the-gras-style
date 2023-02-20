# Monorepo setup and usage

## About
There are many apps using very similar code, including code that doesn't make sense to share between all kinds of apps in libraries. These could be yearly iterations of apps, or apps that are the same but made with different features for different customers.  

To facilitate these use cases, related apps can be placed and maintained in a single repository, where they can share the same local dependencies and be maintained in a single code base. That way many similar apps can share code between each other, keep getting maintained and are all kept up to date.  

Monorepos are not widely used and not very standardised. Most monorepos therefore include custom conventions, tooling and scripts to get everything to work together.

## Yarn 2
Yarn 2 has good [workspaces](https://yarnpkg.com/features/workspaces) functionality, which allows to have a structure of a root workspace, containing multiple packages, each with their own `package.json` file. It also implements [dependency hoisting](https://yarnpkg.com/advanced/lexicon#hoisting) well, among other features that allow us to set up a monorepo without the need of monorepo-specifc tooling like [lerna](https://lerna.js.org/).


## Setup guide

Use this as a rough guide or checklist for what needs to be done to create a new monorepo, as well as documentation for the structure of existing monorepos.

You may prefer to use existing monorepo projects as a reference, such as the [data shops](https://github.com/DHI-GRAS/gras-data-shops) and use the below as a troubleshooting tool, to ensure you have correctly set all the necessary components up.

### 1. Set up yarn

#### Create a new repository
#### Set up Yarn 2/3
##### Ensure Yarn is installed on your system  

```
npm install -g yarn
```

##### Initialize the Yarn project

```
# Inside the empty repository

yarn init -2
```

For more information, see the [official doccumentation](https://yarnpkg.com/getting-started/install) 


##### Change settings  

Yarn now follows [Zero-Installs](https://yarnpkg.com/features/zero-installs), enabling [Plug'n'Play](https://yarnpkg.com/features/pnp) by default, which at the time of writing is not sufficiently well supported by TypeScript and some other tooling libraries, especially when used in monorepos.

To disable [Plug'n'Play](https://yarnpkg.com/features/pnp), add the following code to `.yarnrc.yml`:  

```
nodeLinker: node-modules
```

Also, ensure the following is added to `.gitignore`, so the cache files do not get checked in and therefore mistakenly committed to the repo.
```
# Yarn 2
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/sdks
!.yarn/versions
```


### 2. Set up workspaces / packages
Workspaces is a Yarn feature, read more about it [here](https://yarnpkg.com/features/workspaces).  

For consistant project structure across monorepos, it is recommended to add the following field to the root `package.json` file.
The workspaces field declares where to find the workspaces/packages, which can be represented by apps, internal packages, APIs etc..
```
"workspaces": [
    "./apps/*",
    "./func-apis/*",
    "./libs/*"
],
```

Then create each necessary package in the directories specified above. For instance a web app called, `test-app`.

To keep app names consistant, it is also recommended to suffix them after their type
Example: `test-app`, `test-api`
Library packages should usually be named after what they contain, as they usually don't belong to any app.  

The package/workspace directory names should match the `name` field in the `package.json` file.

### 3. Set up development tooling
Most projects have development tooling libraries - these should be installed to the project root, so that it is shared between all child packages/workspaces.  

It is recommended to declare all root dependencies as `devDependencies`.


Only 2 examples will be given here, but this should generally apply for all development tooling libraries - in order to ensure that the entire project, with its containing workspaces, is maintained and developed as a single codebase.


#### [ESLint](https://eslint.org/)
Install eslint and all dependency plugins and configs to the project root. Add a root config file, such as `.eslintrc.yml`, with `root: true` specified. Any global rules and overrides can also be specified in this file.  

Optionally, add package-specific eslint configurations to child packages, where specific rules can be overriden, if needed. Do not install ESLint in the child packages.  

Add scripts for runnnig eslint to the project root `package.json`, such as 
```
"lint": "eslint --ext ts,tsx . --cache",
"lint:fix": "eslint --ext ts,tsx . --fix --cache",
```

#### [TypeScript](https://www.typescriptlang.org/)
It is also recommended that the entire project uses a single, shared TypeScript installatiom, that is installed in the project root.

All shared TypeScript configuration can be declared in a `tsconfig.json` file in the project root, and the packages can extend from it with a `"extends": "../../tsconfig.json"` field. 

#### Data shops reference example
These 2 most common libraries are at the time of writing implemented in the [data shops](https://github.com/DHI-GRAS/gras-data-shops).


### 4. Set up scripts
To keep script naming consistent and predictable, name the scripts using the same format in all packages/workspaces, such as  `package:action`.

The "package" is the name of the workspace/package, so it should be the same as the directory name, and the name specified in the `"name"` field in the `package.json` file.

The "action" is the name of the script, most commonly these would be `build` and `start` for web-apps.

For our custom react app bundler/builder and its setup, see the [builder documentation](https://github.com/DHI-GRAS/frontend-common/blob/main/builder/README.md)


#### Root scripts
The project root package should contain project tooling scripts - these don't need to be in a special format.

It can also contain scripts that apply to multiple packages, such as starting a web app and an API that it depends on, with a single command.

#### `:` character in script names
The `:` character in script names ensures these scripts can be run in the entire project, as specified in the [`yarn run` documentation](https://yarnpkg.com/cli/run#details)

### 5. Set up CI/CD

Generally, all apps and APIs in a monorepo should be deployed together, as they are a part of the same codebase, with interlinked components.

This would mean that when writing CI/CD pipelines, you should be thinking of the entire repository as a single project and codebase.

#### Azure multi deploy GitHub Action
To make this easier, we have developed a [github action](https://github.com/DHI-GRAS/azure-multi-deploy-action) that takes care of deploying the developed website on the production storage account environment, but also creates staging storage accounts for each Pull Request.

For setup documentation, see [here](https://github.com/DHI-GRAS/azure-multi-deploy-action)

**IMPORTANT**: The action relies on the project structure and script format outlined above - so ensure that your project is following them, if the action is not working correctly.

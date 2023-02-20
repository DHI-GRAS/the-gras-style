# Code conventions for React projects

Conventions help us make our code comparable across projects for easier on-boarding and consistent quality. They serve as a shared definition of best practice and make us reflect on what that means to us as a team. 

Our conventions are guidelines that can change over time. We try to adhere to them in our projects, incorporate them into hour habits, and review them periodically to see whether they still work for us.

We automate part of our conventions using tools such as ESLint, editorconfig and prettier, together with CI. There is a lot of coding practice beyond what a linter can detect, though. Below are guidelines for some of these aspects of best practice. Please read, recognize, reflect, revisit. Oh, and relish!


## Variable, prop, etc. naming conventions

As a general rule, a variable should be named after what it holds and what it is for. It should convey that information to the reader easily - avoid potentially mysterious abbreviations.  
When using TypeScript, the type, its structure and name can already provide a lot of information about the variable.  

Often it makes sense to break variables up and compose them to make the logic more easily understandable.

## DRY
Follow the "Don't Repeat Yourself" principle as much as possible. You should do so especially when you find yourself writing multiple similar statements or expressions that could instead be composed of multiple variables.  An example of that is:
```
const range = datasets[0].range
const min = range[0]
const max = range[1]
```

instead of  

```
const min = datasets[0].range[0]
const max = datasets[0].range[1]
```

or  

```
const responseKeyMap = {
	'/upload-validation-data': 'validation_data',
}

const responseKey = responseKeyMap['/upload-validation-data']
```

instead of  

```
const responseKey = (localRoute: string) => {
	switch (localRoute) {
		case '/upload-validation-data':
			return 'validation_data'
		case '/upload-training-data':
			return 'training_data'
		default:
			return 'training_data'
	}
}
```

This is a general programming principle - examples can't be given for every scenario. If you see something that looks repetitive, look into ways of making it less so.  

## Specific conventions

#### Boolean naming
Make sure to name boolean declerations clearly, so that the name implies a boolean value.  


Often the name itself can imply a boolean value.  
Example: `valid`, `open`, `active`.  

The `is` suffix can be used when the name otherwise doesn't imply a boolean value clearly enough.  
Examples: `isCurrent`, `isLoaded`  

`has` can also be used for cases where a boolean declares whether something, for example, contains or belongs to something.  
Examples: `hasContactId`, `hasData`  

Be aware to not mix them up, as an example - `hasLoaded` can imply a state boolean in past tense.  

#### String variables which are used as presentational, translatable UI element text should be named or suffixed with `label`.
Example: `buttonLabel`

#### Variables which can be used as identifiers within a given set and are not presentational should be named `value`  
Example:
```js
[
	{
		value: 10,
		label: 'Ten'
	}
]
```

## Imports

Note: We are considering to enforce the import order convention with ESLint rules, which would make this section obsolete.

Ordered by what comes first  
1. `React`
2. `react-dom`
3. Application level logic libraries, such as `react-router`
4. Commonly used libraries, such as `@material-ui/*`
5. Other libraries
6. Imports from the same project
7. Imports from the same directory


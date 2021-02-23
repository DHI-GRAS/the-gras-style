# Frontend (#frontend)
Our front-end style guide is based on the [Airbnb JS style guide](https://github.com/airbnb/javascript) and [Airbnb React style guide](https://github.com/airbnb/javascript/tree/master/react). A selection of points are highlighted below. For any other questions consider the [Airbnb React style guide](https://github.com/airbnb/javascript/tree/master/react).

## IDE
Use [VSCode](https://code.visualstudio.com/)

## Repositories
When initiating new repositories use `-` to seperate words and append `-app` as trailing.
Fx `global-seas-app`

## React
Use functional components with hooks.

## Package manager
Use `yarn` 

## Linting
Use prettier in the VSCode IDE for linting. Currently we use these linting settings:

``` 
module.exports = {
  trailingComma: 'es5',
  tabWidth: 2,
  semi: true,
  singleQuote: true,
};
```

## ES6+
Use ES6+ as much as possible. This includes:
- Using `const` and `let` instead of var
- Using arrow functions as much as possible

## Naming
Take your time to think of descriptive names for variables and functions. 
Aim for keeping the namings short but dont compromise on clarity. fx `setSnowCoverData` is fine.

Use `PascalCasing` for your components and classes. use `camelCasing` for your objects, functions, and instances.

## Alphabetical order
When importing dependecies add them to the top of your page and in alphabetical order.
When using lists of props put them in alphabetical order

## Folder structure
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



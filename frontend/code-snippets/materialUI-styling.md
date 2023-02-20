# Material-UI styling tips

[MaterialUI](https://material-ui.com/) offers some styling guidelines which are resourceful but at the same time not really practical.
This is a place where you can find various custom styling for Material-UI with code examples.

Feel free to contribute to this doc whenever you find something interesting and useful for other devs 🚀

## Binding selectors

You can bind pseudo-class by following the structure `&:{pseudoClass}`.

This example binds the `hover` pseudo-class
```
const useStyles = makeStyles(() => ({
	icon: {
		color: '#FFF',
		'&:hover': {
			color: '#000'
		}
	}
}))
```
**Note**: There is *no space* between `&` and `:`.

## Overriding Mui classes

This example overrides the `MuiButton-label` CSS class.
The structure for the latter example is `&.{MuiDesiredClass}`. 

```
<Button
	variant={'outlined'}
	classes={{ label: classes.settingsButton }}
>
	{'Click here'}
</Button>
```
or

```
const useStyles = makeStyles(() => ({
	button: {
		color: '#FFF',
		'&.MuiButton-label': { 
			color: '#000'
		}
	}
}))
```
**Note**: There is *no space* between `&` and `.`.

## Media queries

These are a few ways the responsiveness can be implemented with MaterialUI.

### The `Grid` component 
- details about the Grid component can be found in the [Grid API docs](https://material-ui.com/components/grid/)

### Theme breakpoints
```
const useStyles = makeStyles((theme) => ({
	button: {
		color: '#FFF',
		[ theme.breakpoints.down('sm') ]: {
			color: '#000'
		},
	}
}))
```
### More specific media querries

```
const useStyles = makeStyles((theme) => ({
	button: {
		color: '#FFF',
		'@media (min-width: 600px)': {
			color: '#000'
		},
	}
}))
```

## Nesting selectors

At times, we have to be more specific for achieving the desired result

### Nesting regular HTML tags

The format is `& {htmlTag}`;

```
const useStyles = makeStyles((theme) => ({
	box: {
		color: '#FFF',
		'& span': {
			color: '#000'
		},
	}
}))
```

**Note**: *There is a space* between `&` and `the HTML tag`.

### Nesting other classes

The format is `& $classReference`.
```
const useStyles = makeStyles((theme) => ({
	box: {
		'& $p1': {
			color: '#000'
		},
	}
	p1: {
		color: '#FFF',
	}
}))
```
**Note**: *There is a space* between `&` and `$`.

### Nesting selectors with pseudo-classes

```
const useStyles = makeStyles((theme) => ({
	box: {
		'&:hover': {
			'& $p1': {
				color: '#000'
			},
		}
	}
	p1: {
		color: '#FFF',
	}
}))
```

### Children elements

```
const useStyles = makeStyles((theme) => ({
	box: {
		// first child
		'&:first-child': {...},
		
		// nth child
		'&:nth-child(2)': {...},
		
		// last child
		'&:last-child': {...}

		// uneven child
		'&:last-child(2n+1)': {...}
		
		// even child
		'&:last-child(2n)': {...}
	}
}))
```


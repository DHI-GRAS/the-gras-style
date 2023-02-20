# Project structure, state management guidelines for React projects

### Notes
- This specification is generally only applicable for larger projects. For smaller ones, some aspects may not be as applicable.
- State management, data fetching and processing is still in a testing and deciding phase.


### Structure & What defines a feature
Within the `src` directory, code is structured only by features of the application.  

A feature is effectively a higher-level component of the application. It usually modularizes a visible block of rendered UI and application logic, components and assets.  

#### Articles
You can read about the general concept of feature project structures in these articles.  
Note that we may have different conventions than the ones proposed there.  
- [A feature based approach to React development - Ryan Lancia](https://ryanlanciaux.com/blog/2017/08/20/a-feature-based-approach-to-react-development/)
- [Package by Feature - Philipp Hauer's Blog](https://phauer.com/2020/package-by-feature/)

### What a feature **should aim** to be
- Represent a block of UI or a clearly defined piece of application logic
- Modular, portable, reusable - easy to implement
- Highly composable (same way as components)
- Clear and concise - it should be easy to understand what the feature is, what it depends on and what it renders
- Easy to test
- In larger or projects or where it is deemed necessary - high-level UI features should be easy to disable with flags, or to remove by simply removing the imports and instances of that component.
- Expose only the necessary components, logic, state and props outside the feature


### What a feature **should avoid** to be
- Tightly dependent on other features, unless the link is made syntactically obvious and deemed necessary
- Exposing state to be stored outside the feature that the feature itself updates (use feature-scoped contexts instead)
- Exposing too much logic, components, types, assets or state that must be implemented outside the feature itself (keep it simple and modular)
- Be a collection of assets, logic or components that are grouped by how they are related, not by where they are implemented (in other words - be a layer)


#### Notes
- It won't always be possible or easy to make a feature fully fit all the above recommendations - evaluate, balance and discuss what solutions make most sense in a given scenario
- The extent necessary to fulfill many of the recommendations can be interpreted subjectively - evaluate, balance and discuss what solutions make most sense in a given scenario


### Structure within feature directories

Features have no strict internal structure guidelines defined, as they can vary greatly in size and complexity, where different structures may make more sense.

Features containing no more than approximately 10 files can have all files in the root of the feature directory.

Features containing more files often make sense to group by type, i.e. package by layer inside the feature to keep it more organized.

Example: 
```
payment-screen
│   FormView.tsx
│   FormFields.tsx
│   PaymentScreen.tsx
│
├───components
│       LabelCheckbox.tsx
│       LoadingOverlay.tsx
│       SelectionSummaryBox.tsx
│
├───data
│       companySizes.ts
│       countries.ts
│       segments.ts
│       useBsApiOptions.ts
│
├───state
│       CustomerDataContext.tsx
│
└───types
        CustomerData.ts
        formSchema.ts

```
In the example above, views, screens strictly belonging to the payment feature are still placed in the root of the feature - they are treated as the primary components of the feature.


### The `common` feature

Often there will be some components and other assets that can and are used within many features, and don't contextually belong to a certain feature.  
If that is the case, they should be moved to the `common` feature.  
It usually contains directories, grouping files by type. Example: `images`, `components`, `hooks`, `types`.  
Components and assets that end up here often make sense to share elsewhere across projects.

## Components

### What a component **should aim** to be
- Concise - it should do or render ***one*** thing
- Clearly describe what it renders and what it belongs to by its name
- Composable (if it can be)
- Clearly and correctly define what props are required, what they are, and what they for

### What a component **should avoid** to be
- Render UI that is not dependent on one another (unless it's layout)
- Handle both domain logic and UI state
- Contain too much logic that could be extracted into functions
- Causing unnecessary re-renders
- Export more than just a component
- Contain excessively verbose JSX

### Articles
[Composition vs Inheritance - React documentation](https://reactjs.org/docs/composition-vs-inheritance.html)
[React - Seperation of Concerns - Andrei Calazans](https://blog.g2i.co/react-separation-of-concerns-78ec0545bf36)
[React components naming convention - Charly Poly](https://charlypoly.com/publications/react-components-naming-convention)


### Component types
Below are examples of how types of components usually can be defined and named - most should easily fall within one of these, if they don't then it may be a sign that a component serves the purpose of multiple of these and could be split up.  

#### `Page` component
Example: `LandingPage`  

Pages are views that can be accessed by routes.
Does not apply to React Native - pages there would be called screens, which usually are a part of screen stacks.

#### `Screen` component
Example: `OptionsScreen`  

Screens contain page-wide views of pages, with exceptions such as navigation bars, that don't have to be a part of screens but rather part of a component higher up in the tree such as a page.  

#### `View` component
Example: `PaymentFormView`  

Views are usually collections of components, declaring their layout, logic and state between them.  
Some may be more familiar with calling them blocks or containers - in this case they're basically the same.


#### UI element component
Example: `LabelCheckbox`  
Atomic UI components - things like buttons, checkboxes, etc.

#### Wrapper/container component
Example: `FormData`, `FormContainer`
Usually handles higher-level state or domain logic. Depending on the situation - Pages, Screens and Views could also serve the same purpose.


### Feature-specific components

Make sure to make a clear distinction between components that strictly belong to a feature, and ones which are atomic but currently implemented only in the given feature.

If an atomic component is implemented within more than one feature, it should be moved to the `common` feature. If it's not atomic and is composed out of multiple components, it should be its own feature.


## State management

### Props 
When needed, props should generally be used and passed up and down to all child components within a feature. Generally, you should aim for prioritizing passing props rather than context. This visualizes the data flow and composition. Make sure to use component composition where it makes sense.

### State and data shared between features

Most features will have a state that can be consumed by other features. The best way of sharing this, while keeping the feature as modular as possible, would be to export a feature-scoped context. The ContextProvider should be added as low down the component tree as possible, depending on where its state would be relevant to consume.

[React documentation on context](https://reactjs.org/docs/context.html)  
Contexts should be strongly typed. [A TypeScript guide](https://www.pluralsight.com/guides/using-react's-context-api-with-typescript)  

To make context values even more easy to access, it can be abstracted in hooks.


#### Bloated components
If a certain component starts to manage too much state, become too large or complex, it should be re-evaluated, to see if its UI could be separated or split into another `View` component. In some cases, it can also make sense to move some functions out of the component file.

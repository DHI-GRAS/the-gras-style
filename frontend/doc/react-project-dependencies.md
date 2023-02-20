# Build, linting and other common dependencies of React projects  

## @dhi-gras/builder  

For further documentation on the builder, see [here](https://github.com/DHI-GRAS/frontend-common/blob/main/builder)  

To allow for custom optimization, customization of the dev server and build procedure, we use a custom shared webpack configuration across our projects with the `@dhi-gras/builder` package.  
It's still largely experimental and will have more features added as needed.  

Usage:  
- Use `builder build` to build a production-ready bundle in the `dist` directory  
- Use `builder start` to start a dev server at http://127.0.0.1:3000  
- Use `builder analyze` to open a visualization of bundled file sizes  


Features:
- Reads `.env` file, if it exists, containing environment variables - can then be accessible in the `process.env` object  
- Files in the `static` directory will be copied to the `dist` folder when built  
- Images are compressed in production builds  
- Linting and type errors don't prevent a successful build  


## @dhi-gras/eslint-config  

Consists of three config packages to extend from  
- [`@dhi-gras/eslint-config-react`](https://github.com/DHI-GRAS/frontend-common/blob/main/eslint-config-react) - Contains rules specific to React  
- [`@dhi-gras/eslint-config-ts`](https://github.com/DHI-GRAS/frontend-common/blob/main/eslint-config-ts) - Contains rules specific to TypeScript projects  
- [`@dhi-gras/eslint-config-js`](https://github.com/DHI-GRAS/frontend-common/blob/main/eslint-config-js) - Contains rules specific to ES6+ projects  

Further usage documentation can be found in the root readme.md  


## SWR - data fetching

`swr` should be used for querying and fetching data. [Documentation](https://swr.vercel.app/)  

In many cases it will be a good idea to compose your own fetcher hooks with `swr`.  

It requires the use of your own fetcher - the native `fetch` API should be used for that: [Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)  


`swr` generally only makes sense to use in GET requests. Other requests can simply be put within a function, using the `fetch` API.

More usage examples can be added here.  


## date-fns - date & time formatting and parsing

`date-fns` should be used for working with dates as it is the most lightweight, well known and flexible library for this.  
[Documentation](https://date-fns.org/)  

If a project needs only very basic parsing of dates to certain localized human-readable dates, then using only the `Intl.DateTimeFormat` object may make more sense.  
[Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)

## deck.gl - Map visualization framework

[deck.gl](https://deck.gl/) is the recommended map visualization framework, used in many of the newer apps, where you can see existing layers and other components made for it, for both reuse and as examples for new solutions.  

[`react-map-gl`](https://visgl.github.io/react-map-gl/) is still used by many projects, and should only be replaced by deck.gl when it makes sense.


## echarts - charts
`echarts-for-react` should be used for charts and graphs, and many other types of data visualization.  
- `echarts-for-react`: [Documentation](https://github.com/hustcc/echarts-for-react)
- `echarts`: [Documentation](https://echarts.apache.org/en/index.html)
- `echarts`: [examples](https://echarts.apache.org/examples/en/index.html)  

More usage examples can be added here.  


## formik - forms
`formik` should be used for forms  
[Documentation](https://formik.org/)  

## Material-UI, clsx, notistack
- `@material-ui/core` should be used for component foundations. Use the DHI shared ThemeProvider, import styling related components, hooks, types and functions from `@material-ui/core/styles`
- `@material-ui/icons` should be used for icons - DHI specific icons can currently be found in `@dhi/icons`, stored in the [DHI/react-components repository](https://github.com/dhi/react-components/)
- `clsx` should be used for using multiple and/or conditional classes. [Documentation](https://github.com/lukeed/clsx/)
- `notistack` should be used for displaying snackbars. [Documenation](https://github.com/iamhosseindhv/notistack)

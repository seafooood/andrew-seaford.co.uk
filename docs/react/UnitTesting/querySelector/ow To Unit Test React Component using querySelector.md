# How To Unit Test React Component using querySelector

In this example, we will Unit Test a React component using the function querySelector. The querySelector will find an elements based on CSS selectors.

## Procedure
- We are going to test a simple component called demo-query-selector. `npx create-react-app demo-query-selector`
- Change directory `cd demo-query-selector`
- Create file `DemoQuerySelector.js` in the `src` folder. Note that the div contains the id `id="current-selection"`.
[DemoQuerySelector.js](DemoQuerySelector.js)
- Create file `DemoQuerySelector.test.js` in the `src` folder. The unit test will find the div using the id attribue `id="current-selection"` and confirm the text contains the word "fred".
[DemoQuerySelector.test.js](DemoQuerySelector.test.js)

- Run the unit test `npm test`

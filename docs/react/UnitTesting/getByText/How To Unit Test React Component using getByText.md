# How To Unit Test React Component using getByText

In this example, we will Unit Test a React component using the function getByText. The getByText will confim if the element contains the given text.

## Procedure

- We are going to test a simple component called demo-get-by-text. `npx create-react-app demo-get-by-text`

- Change directory `cd demo-get-by-text`

- Create file `DemoGetByText.js` in the src folder.
[DemoGetByText.js](DemoGetByText.js)

- Create file `DemoGetByText.test.js` in the src folder. The unit test confirm if the component conains the text "too hot" or "too cold".
[DemoGetByText.test.js](DemoGetByText.test.js)

- Run the unit test `npm test`

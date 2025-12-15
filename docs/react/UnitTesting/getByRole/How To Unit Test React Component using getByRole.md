# How To Unit Test React Component using getByRole

In this example, we will Unit Test a React component using the function getByRole. The getByTestId is useful if the div has a specific role, you can use getByRole. This is particularly useful for semantic HTML where elements have roles like "button," "checkbox," etc.

## Procedure

- Create a simple component called DemoGetByRole. `npx create-react-app demo-get-by-role`

- Change directory `cd demo-get-by-role`

- Create file `DemoGetByRole.js` in the `src` folder. Note that the component contain three different buttons.
[DemoGetByRole.js](DemoGetByRole.js)

- Create file `DemoGetByRole.test.js` in the `scr` folder. The unit test will find second button.
[DemoGetByRole.test.js](DemoGetByRole.test.js)

- Run the unit test `npm test`

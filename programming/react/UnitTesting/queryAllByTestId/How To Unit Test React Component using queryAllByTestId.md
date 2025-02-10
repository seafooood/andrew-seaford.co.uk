# How To Unit Test React Component using queryAllByTestId

In this example, we will Unit Test a React component using the function queryAllByTestId. The queryAllByTestId will confim all of the checkbox element contains the id `data-testid="myid"` value is checked.

## Procedure

- We are going to test a simple component called demo-query-by-test-id. `npx create-react-app demo-query-by-test-id`

- Change directory `cd demo-query-by-test-id`

- Create file `DemoQueryAllByTestIds.js` in the `src` folder.
[DemoQueryAllByTestIds.js](DemoQueryAllByTestIds.js)

- Create file `DemoQueryAllByTestIds.test.js` in the src folder. 
[DemoQueryAllByTestIds.test.js](DemoQueryAllByTestIds.test.js)

- Run the unit test `npm test`

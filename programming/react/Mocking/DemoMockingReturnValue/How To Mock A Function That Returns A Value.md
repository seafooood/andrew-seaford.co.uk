# How To Mock A Function That Returns A Value

In this article we are demostrate how to mock a function that returns a value.

## Procedure

- Create the react app `npc create-react-app demo-mocking-return-value`.
- Change directory `cd demo-mocking-return-value`
- Create the file `DemoMockReturnValue.js` in the `src` directory. A referance to the function f is passed to the component as a prop. The function f is called and the result from the function is used to update the div with the test id myresult.
[DemoMockReturnValue.js](DemoMockReturnValue.js)

- Create the file `DemoMockReturnValue.test.js` in the `src` directory. The unit test will create a mocked function f using the jest library `const f = jest.fn();`. The function is confirmed to return a value using the code `f.mockReturnValue(expectedValue);`. The assert confirms that the div with the test id myresult contains the expected data.
[DemoMockReturnValue.test.js](DemoMockReturnValue.test.js)
- Run the tests `npm test`

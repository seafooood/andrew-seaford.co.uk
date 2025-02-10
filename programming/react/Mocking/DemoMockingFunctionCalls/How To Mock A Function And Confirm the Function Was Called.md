# How To Mock A Function And Confirm the Function Was Called

In this article we are demostrate how to mock a function and confirm the function was called multiple times with two different tests of arguments.

## Procedure

- Create the react app `npc create-react-app demo-mocking-function-calls`.
- Change directory `cd demo-mocking-function-calls`
- Create the file `DemoMockingFunctionCalls.js` in the `src` directory. A referance to the function f is passed as an argument to the function DemoMockingFunctionCalls. The function calls f twice with two different sets of arguments.
[DemoMockingFunctionCalls.js](DemoMockingFunctionCalls.js)

- Create the file `DemoMockingFunctionCalls.test.js` in the `src` directory. The unit test will create a mocked function f using the jest library `const f = jest.fn();`. The assert checks that the function was called twice by checking the `f.mock.calls` matches the array of expected calls.
[DemoMockingFunctionCalls.test.js](DemoMockingFunctionCalls.test.js)
- Run the tests `npm test`

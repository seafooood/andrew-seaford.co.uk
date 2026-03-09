---
---
title: "How To Mock A Function And Confirm the Function Was Called"
description: "Demonstrates how to mock a function with Jest in a Node/React project and assert it was called with the expected arguments and count. Includes an example component and unit test."
date: 2025-02-02
categories:
  - "prog"
keywords: [jest, mocking, unit-tests, react, testing, javascript]
slug: "how-to-mock-a-function-and-confirm-the-function-was-called"
---

When developing a JavaScript or React application you may need to verify that a callback or helper function is invoked with the correct arguments and number of calls. Mocking the function makes it simple to observe each call and its parameters without executing the real implementation.

This guide will walk you through creating a small example component and a Jest unit test that mocks a function, asserts it was called twice, and checks the arguments passed on each call. The steps assume a Node.js development environment on Windows, macOS, or Linux.

## Procedure

- Create the React app `npx create-react-app demo-mocking-function-calls`.
- Change directory: `cd demo-mocking-function-calls`.
- Create the file `src/DemoMockingFunctionCalls.js`. This module should export a function that accepts a callback `f` and calls it twice with two different sets of arguments.
- Create the file `src/DemoMockingFunctionCalls.test.js`. The unit test should create a mocked function using Jest: `const f = jest.fn();`, call the exported function passing `f`, and then assert `f` was called twice and that `f.mock.calls` matches the expected array of calls.
- Run the tests: `npm test`.

Example `f.mock.calls` for two calls might look like:

```
[
  [1, 'first'],
  [2, 'second']
]
```

## Expected output

When the test runs successfully you should see Jest report the passing test suite and test, for example:

```
 PASS  src/DemoMockingFunctionCalls.test.js
  ✓ calls function twice with expected args (X ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        0.5 s
```

Additionally, inspecting `f.mock.calls` in the test will show the recorded calls and their arguments so you can perform fine-grained assertions against each invocation.

## Example code

Below are minimal example implementations you can drop into the `src` directory of a `create-react-app` project.

`src/DemoMockingFunctionCalls.js`

```javascript
export function DemoMockingFunctionCalls(f) {
  // Call the provided callback twice with different arguments
  f(1, 'first');
  f(2, 'second');
}
```

`src/DemoMockingFunctionCalls.test.js`

```javascript
import { DemoMockingFunctionCalls } from './DemoMockingFunctionCalls';

test('calls function twice with expected args', () => {
  const f = jest.fn();
  DemoMockingFunctionCalls(f);

  expect(f).toHaveBeenCalledTimes(2);
  expect(f.mock.calls).toEqual([
    [1, 'first'],
    [2, 'second'],
  ]);
});
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-mock-a-function-and-confirm-the-function-was-called](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-mock-a-function-and-confirm-the-function-was-called)

## JavaScript Related Articles

- [Creating a Restfull Server Using NextJs](../creating-a-restfull-server-using-nextjs/index.md)
- [How To Build A Static Page That Refreshes Every 60 Seconds Using NextJs](../how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs/index.md)
- [How To Create a Combobox React Component With Unit Tests](../how-to-create-a-combobox-react-component-with-unit-tests/index.md)
- [How To Create a Next JS App From Scratch](../how-to-create-a-next-js-app-from-scratch/index.md)
- [How To Create a React Component That Returns a Promise With Unit Tests](../how-to-create-a-react-component-that-returns-a-promise-with-unit-tests/index.md)

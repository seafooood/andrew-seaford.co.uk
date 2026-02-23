---
title: "How To Mock A Function And Confirm the Function Was Called"
date: 2025-02-02
categories:
  - "prog"
keywords: [jest, mocking, unit-tests, react, testing]
---

In this article we are demostrate how to mock a function and confirm the function was called multiple times with two different tests of arguments.

## Procedure

- Create the react app `npc create-react-app demo-mocking-function-calls`.
- Change directory `cd demo-mocking-function-calls`
- Create the file `DemoMockingFunctionCalls.js` in the `src` directory. A referance to the function f is passed as an argument to the function DemoMockingFunctionCalls. The function calls f twice with two different sets of arguments.
    
- Create the file `DemoMockingFunctionCalls.test.js` in the `src` directory. The unit test will create a mocked function f using the jest library `const f = jest.fn();`. The assert checks that the function was called twice by checking the `f.mock.calls` matches the array of expected calls.
    
- Run the tests `npm test`


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-mock-a-function-and-confirm-the-function-was-called](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-mock-a-function-and-confirm-the-function-was-called)

## JavaScript Related Articles

- [Creating a Restfull Server Using NextJs](../creating-a-restfull-server-using-nextjs/index.md)
- [How To Build A Static Page That Refreshes Every 60 Seconds Using NextJs](../how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs/index.md)
- [How To Create a Combobox React Component With Unit Tests](../how-to-create-a-combobox-react-component-with-unit-tests/index.md)
- [How To Create a Next JS App From Scratch](../how-to-create-a-next-js-app-from-scratch/index.md)
- [How To Create a React Component That Returns a Promise With Unit Tests](../how-to-create-a-react-component-that-returns-a-promise-with-unit-tests/index.md)

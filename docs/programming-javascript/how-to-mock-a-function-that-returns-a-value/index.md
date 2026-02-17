---
title: "How To Mock A Function That Returns A Value"
date: 2025-02-02
categories: 
  - "prog"
---

In this article we are demostrate how to mock a function that returns a value.

## Procedure

- Create the react app `npc create-react-app demo-mocking-return-value`.
- Change directory `cd demo-mocking-return-value`
- Create the file `DemoMockReturnValue.js` in the `src` directory. A referance to the function f is passed to the component as a prop. The function f is called and the result from the function is used to update the div with the test id myresult.
    
- Create the file `DemoMockReturnValue.test.js` in the `src` directory. The unit test will create a mocked function f using the jest library `const f = jest.fn();`. The function is confirmed to return a value using the code `f.mockReturnValue(expectedValue);`. The assert confirms that the div with the test id myresult contains the expected data.
    
- Run the tests `npm test`


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-mock-a-function-that-returns-a-value](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-mock-a-function-that-returns-a-value)

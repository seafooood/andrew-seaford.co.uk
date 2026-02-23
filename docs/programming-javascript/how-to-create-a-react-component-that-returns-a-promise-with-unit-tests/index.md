---
title: "How To Create a React Component That Returns a Promise With Unit Tests"
date: 2025-02-02
categories:
  - "prog"
keywords: [react, promises, async, unit-tests, javascript]
---

In this article we will create a React component that returns a Promise. The promise will be the sum of two numbers. We will also create unit test to confirm the components functionality.

## Component Setup

- create the app `npx create-react-app demo-promise`.
- Change directory `cd demo-promise`.
- Create a directory within `src` called `components`.
- Create a file called `DemoPromise.js` withing the `components` directory.

```js

const DemoPromise = ({a,b}) => {
    return Promise.resolve(a+b);
}

export default DemoPromise;
```

- Create a file called `DemoPromise.test.js` withing the `components` directory.

```js
import DemoPromise from "./DemoPromise"

test('Should confirm promise returns sum of a and b', async () => {
    // Arrange
    const a = 1;
    const b = 2;

    // Act
    const result = await DemoPromise({a,b});

    // Assert
    expect(result).toBe(a + b);
})
```

- Execute the tests `npm test`


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-create-a-react-component-that-returns-a-promise-with-unit-tests](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-create-a-react-component-that-returns-a-promise-with-unit-tests)

## JavaScript Related Articles

- [Creating a Restfull Server Using NextJs](../creating-a-restfull-server-using-nextjs/index.md)
- [How To Build A Static Page That Refreshes Every 60 Seconds Using NextJs](../how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs/index.md)
- [How To Create a Combobox React Component With Unit Tests](../how-to-create-a-combobox-react-component-with-unit-tests/index.md)
- [How To Create a Next JS App From Scratch](../how-to-create-a-next-js-app-from-scratch/index.md)
- [How to  Handle Server-side API Routes in React](../how-to-handle-server-side-api-routes-in-react/index.md)

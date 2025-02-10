# How To Create a React Component That Returns a Promise With Unit Tests

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

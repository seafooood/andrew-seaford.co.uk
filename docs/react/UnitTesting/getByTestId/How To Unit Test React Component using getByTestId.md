# How To Unit Test React Component using getByTestId

In this example, we will Unit Test a React component using the function getByTestId. The getByTestId will find an element from the DOM using the attribute data-testid.

## Procedure

- Create a simple component called demo-get-by-test-id. `npx create-react-app demo-get-by-test-id`

- Change directory `cd demo-get-by-test-id`

- Create file `DemoGetByTestId.js` in the `scr` folder. Note that the div contains the attribue `data-testid="current-selection"`.
```javascript
const DemoGetByTestId = () => (
    <div data-testid="current-selection">Current selection = fred</div>
  );
  
export default DemoGetByTestId;
```

- Create file `DemoGetByTestId.test.js` in the `src` folder.  The unit test will find the div using the attribue `data-testid="current-selection"` and confirm the text contains the word "fred".
```javascript
import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import DemoGetByTestId from './DemoGetByTestId';

// Test confirms that the div with the test id 'current-selection' contains the test "fred"
test("Component renders text", () => {
    // Arrange

    // Act
    render(<DemoGetByTestId/>);

    // Assert
    const result = screen.getByTestId('current-selection');
    expect(result).toHaveTextContent("fred");
});
```

- Run the unit test `npm test`

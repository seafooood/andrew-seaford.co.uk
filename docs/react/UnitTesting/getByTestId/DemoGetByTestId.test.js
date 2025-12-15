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
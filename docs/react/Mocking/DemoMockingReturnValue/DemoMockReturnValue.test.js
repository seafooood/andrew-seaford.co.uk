import { render, screen } from '@testing-library/react';
import DemoMockReturnValue from "./DemoMockReturnValue";

test("Show display the value from the mocked function", () =>{

    // Arrange
    const expectedValue = 12;
    const f = jest.fn();
    f.mockReturnValue(expectedValue);

    // Act
    render(<DemoMockReturnValue f={f} />);

    // Assert
    expect(f()).toBe(expectedValue); // Confirm mock is configured correctly
    const result = screen.getByTestId("myresult");
    expect(result).toHaveTextContent(expectedValue);

});
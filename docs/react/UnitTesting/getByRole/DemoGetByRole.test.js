import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import DemoGetByRole from './DemoGetByRole';

test("Component renders button", () => {
    // Arrange
    const expectedText = "Button Two"; 

    // Act
    render(<DemoGetByRole/>);

    // Assert
    const result = screen.getByRole('button', { name: expectedText });
    expect(result).toHaveTextContent(expectedText);
});

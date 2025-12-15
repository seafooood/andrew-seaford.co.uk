import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import DemoGetByText from './DemoGetByText';

// Test confirms that the div will contain the text "too hot"
test("Component renders text too hot", () => {
    // Arrange
    const temperature = 40

    // Act
    render(<DemoGetByText temperature={temperature}/>);

    // Assert
    const result = screen.getByText('too hot');
    expect(result).not.toBeNull();
});

// Test confirms that the div will contain the text "too cold"
test("Component renders text too cold", () => {
    // Arrange
    const temperature = 10
    
    // Act
    render(<DemoGetByText temperature={temperature}/>);

    // Assert
    const result = screen.getByText('too cold');
    expect(result).not.toBeNull();
});
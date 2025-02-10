import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import DemoSelect from './DemoSelect';

// Test confirms the default selection matches the first option 
test("Component renders default selection", () => {
    // Arrange
    const optionOne = "apple";
    const optionTwo = "orange";
    const optionList = [optionOne, optionTwo];

    // Act
    render(<DemoSelect optionList={optionList} />);

    // Assert
    const result = screen.getByTestId('current-selection');
    expect(result).toHaveTextContent(optionOne);
});

// Test confirms that the select contains the correct number of options
test("Component has correct number of options", () =>{
    // Arrange
    const optionOne = "apple";
    const optionTwo = "orange";
    const optionList = [optionOne, optionTwo];

    // Act
    render(<DemoSelect optionList={optionList} />);

    // Assert
    const result = screen.getByRole('combobox');
    expect(result.length).toBe(optionList.length);
});


// Test confirms that the select contains options from the list
test("Component contains options from list", () =>{
    // Arrange
    const optionOne = "apple";
    const optionTwo = "orange";
    const optionList = [optionOne, optionTwo];

    // Act
    render(<DemoSelect optionList={optionList} />);

    // Assert
    const result = screen.getByRole('combobox');
    expect(result.length).toBe(optionList.length);
    expect(result.options[0].text).toBe(optionOne);
    expect(result.options[1].text).toBe(optionTwo);
});


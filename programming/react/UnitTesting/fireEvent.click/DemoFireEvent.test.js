import '@testing-library/jest-dom';
import { render, screen, fireEvent } from '@testing-library/react';
import DemoFireEvent from './DemoFireEvent';

test("component resnders default value of zero", () => {
  // Arrange
  
  // Act
  render(<DemoFireEvent />);

  // Assert
  const result = screen.queryByTestId("result");
  expect(result.textContent).toBe("0");
});

test("Component increments count on click", () => {
  // Arrange
  render(<DemoFireEvent />);
  const button = screen.queryByRole('button');

  // Act
  fireEvent.click(button);
  
  // Assert
  const result = screen.queryByTestId("result");
  expect(result.textContent).toBe("1");
});

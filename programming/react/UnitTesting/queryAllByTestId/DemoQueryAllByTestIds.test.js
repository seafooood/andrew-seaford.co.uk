import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import DemoQueryAllByTestIds from './DemoQueryAllByTestIds';

test("Component renders multiple checkboxes", () => {
  // Arrange

  // Act
  render(<DemoQueryAllByTestIds />);

  // Assert
  const inputs = screen.queryAllByTestId("myid");
  expect(inputs.length).toBe(3);
  inputs.forEach((input) => {
    expect(input.checked).toBe(true);
  });
});

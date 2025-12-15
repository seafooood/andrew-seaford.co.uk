import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import DemoQuerySelector from './DemoQuerySelector';

test("Component renders text using container query", () => {
  // Arrange

  // Act
  render(<DemoQuerySelector />);

  // Assert
  const result = document.querySelector('#current-selection');
  expect(result).toHaveTextContent("fred");
});

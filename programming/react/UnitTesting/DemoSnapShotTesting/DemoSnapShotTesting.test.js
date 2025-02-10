import DemoSnapShotTesting from './DemoSnapShotTesting';
import TestRenderer from 'react-test-renderer'; 

test("Should check component output against snapshot", () => {
    // Arrnag

    // Act
    const result = TestRenderer.create(<DemoSnapShotTesting />).toJSON();

    // Assert
    expect(result).toMatchSnapshot();
});
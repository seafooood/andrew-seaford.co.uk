import DemoPromise from "./DemoPromise"

test('Should confirm promise returns sum of a and b', async () => {
    // Arrange
    const a = 1;
    const b = 2;

    // Act
    const result = await DemoPromise({a,b});

    // Assert
    expect(result).toBe(a + b);
})
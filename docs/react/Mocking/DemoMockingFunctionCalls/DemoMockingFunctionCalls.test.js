import DemoMockingFunctionCalls from "./DemoMockingFunctionCalls";

test("Confirm that function was called twice", () =>{
    // Arrange
    const f = jest.fn();

    // Act
    DemoMockingFunctionCalls(f);

    // Assert
    expect(f.mock.calls).toEqual(
        [
            [1,2,3],
            ['a']
        ]
    );
});
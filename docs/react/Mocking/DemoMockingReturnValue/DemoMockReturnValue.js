const DemoMockReturnValue=({f}) => {
    const result = f();
    return (
        <div data-testid="myresult">{result}</div>
    );
}
export default DemoMockReturnValue;
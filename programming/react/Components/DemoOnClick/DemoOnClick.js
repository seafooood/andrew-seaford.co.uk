
const DemoOnClick = () => {

    function handleClick(name){
        alert('Hello ' + name);
    }

    const names = ['Andrew', 'Sara', 'Dylan', 'Kyle'];
    return (
        names.map(name => <h1 onClick={() => handleClick(name)}>Hello, {name}!</h1>)
    )
}

export default DemoOnClick;
import styled from 'styled-components'

const DemoStyleCssInJs = () => {
    const TomatoButton = styled.button`
    color: tomato;
    border-color: tomato;
    `;
    return (<TomatoButton>Click Me</TomatoButton>)
};

export default DemoStyleCssInJs;
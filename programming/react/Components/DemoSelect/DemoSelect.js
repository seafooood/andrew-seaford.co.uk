import {useState} from 'react'

const DemoSelect = ({optionList}) => {
    const [selection, setSelection] = useState(optionList[0]);

    return (
        <div>
            <p>Demo Selector</p>
            <select 
                value={selection}
                onChange={(event) => setSelection(event.target.value)}
            >
                {optionList.map(t=><option value={t} key={t}>{t}</option>)}
            </select>
            <div data-testid="current-selection">Current selection = {selection}</div>
        </div>
    );
}

export default DemoSelect;

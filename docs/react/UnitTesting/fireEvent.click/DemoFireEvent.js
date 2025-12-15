import React from 'react';
import {useState} from 'react';

const DemoFireEvent = () => {
  const [count, setCount] = useState(0);
  return (
    <div>
      <button onClick={() => {setCount(count+1);}}>Click Me</button>
      <div>Result=<div data-testid="result">{count}</div></div>
    </div>  
  )

};

export default DemoFireEvent;

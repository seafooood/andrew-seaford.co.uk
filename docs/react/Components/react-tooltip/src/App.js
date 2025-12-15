import React from 'react';
import { Tooltip } from 'react-tooltip';
import 'react-tooltip/dist/react-tooltip.css';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>React Tooltip Examples</h1>
        <div style={{ display: 'flex', gap: '20px', marginTop: '30px' }}>

          {/* Example 1: Basic Tooltip (Top) */}
          <a data-tooltip-id="my-tooltip-1" data-tooltip-content="This is a simple tooltip.">
            <button>Top Tooltip</button>
          </a>          

          {/* Example 2: Warning Tooltip (Bottom) */}
          <a data-tooltip-id="my-tooltip-2" data-tooltip-content="Be careful!">
            <button>Bottom Tooltip</button>
          </a>

          {/* Example 3: Error Tooltip (Top) */}
          <a data-tooltip-id="my-tooltip-3" data-tooltip-content="Error!">
            <button>Top Tooltip</button>
          </a>

          {/* Example 4: Success Tooltip (Right) */}
          <a data-tooltip-id="my-tooltip-4" data-tooltip-content="Great success!">
            <button>Right Tooltip</button>
          </a>

        </div>

        {/* Tooltip Components */}
        <Tooltip id="my-tooltip-1" place="top" effect="solid" />
        <Tooltip id="my-tooltip-2" place="bottom" variant="warning" effect="float" />
        <Tooltip id="my-tooltip-3" place="top" variant="error" />
        <Tooltip id="my-tooltip-4" place="right" variant="success" />

      </header>
    </div>
  );
}

export default App;


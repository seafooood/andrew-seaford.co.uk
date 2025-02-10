# How To Style A React Component Using Inline Style

In this example, we will learn how to style a button on a React component using inline styles. The inline style is set using the attribute style. The system value is an object arrary of camel case style names.

In this example, we will change the font size and colour of the button.
[!button.png](button.png)

## Procedure

- Create the react app `npx create-react-app demo-inline-style`.
- Change directory `cd demo-inline-style`.
- Create the file `DemoInlineStyle.js` in the `src` folder. Note the style attribute of the button.
[DemoInlineStyle.js](DemoInlineStyle.js)
- Update the code in `index.js` to render the DemoInlineStyle component.

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import DemoInlineStyle from './DemoInlineStyle';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <DemoInlineStyle />
  </React.StrictMode>
);
```

- Start the app `npm start`

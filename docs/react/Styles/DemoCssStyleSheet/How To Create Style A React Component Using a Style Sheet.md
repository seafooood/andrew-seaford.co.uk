# How To Create Style A React Component Using a Style Sheet

In this article, we are going to style a button on a React component using a CSS Style Sheet.

## Procedure

- Create a React app `npx create-react-app demo-css-style-sheet`
- Change directory `cd demo-css-style-sheet`
- Create the css file `DemoCssStyleSheet.css` in the directory `src`.
[DemoCssStyleSheet.css](DemoCssStyleSheet.css)
- Create the js file `DemoCssStyleSheet.js` in the directory `src`. Note that the button contains an attribute `className="button"` and the css import `import "./DemoCssStyleSheet.css"`
[DemoCssStyleSheet.js](DemoCssStyleSheet.js)
- Update the `index.js` to use the new component

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import DemoCssStyleSheet from './DemoCssStyleSheet';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <DemoCssStyleSheet />
  </React.StrictMode>
);
```

- Start the app `npm start`

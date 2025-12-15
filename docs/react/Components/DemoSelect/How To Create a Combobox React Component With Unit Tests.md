# How To Create a Combobox React Component With Unit Tests

In this article we will create a React component that displays a Combobox. The values of the combobox are set from an array. We will also create unit test to confirm the components functionality.

## Component Setup

- Create the app `npx create-react-app demo-select`.
- Change directory `cd demo-select`.
- Create a directory within `src` called `components`.
- Create a file called `DemoSelect.js` withing the components directory.
[DemoSelect.js](DemoSelect.js)

- Create a file called `DemoSelect.test.js`
[DemoSelect.test.js](DemoSelect.test.js)

- Run the tests `npm test`

- To use the component add an include line to your project file eg `import DemoSelect from './DemoSelect';`. Create a list of options eg `const optionList = ["apple", "orange"];`, create an instance of the component and pass the list to the component `<DemoSelect optionList={optionList} />`.

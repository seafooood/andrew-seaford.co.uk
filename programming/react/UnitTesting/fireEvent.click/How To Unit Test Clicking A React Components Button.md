# How To Unit Test Clicking A React Components Button

In this article we are demostrate how to unit test clicking a button in a React Component. 

The React Component is a simple component with a button that incremens a counter every time the button is clicked. The button click event is triggered in the unit test using the code `fireEvent.click(button);`

## Procedure

- Create the react app `npc create-react-app demo-fire`.
- Change directory `cd demo-fire`
- Create the file `DemoFireEvent.js` in the `src` directory.
[DemoFireEvent.js](DemoFireEvent.js)
- Create the file `DemoFireEvent.test.js` in the `src` directory. The unit test will await for the result of the promise.
[DemoFireEvent.test.js](DemoFireEvent.test.js)
- Run the tests `npm test`

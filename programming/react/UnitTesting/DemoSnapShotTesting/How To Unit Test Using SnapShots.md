# How To Unit Test Using SnapShots

In this article we are demostrate create a snapshot from the rendering of a component. The unit test will fail if the conponent rendering does not match the snapshot.

## Procedure

- Create the react app `npc create-react-app demo-snapshot-testing`
- Change directory `cd demo-snapshot-testing`
- Install the test renderer `npm install react-test-renderer`
- Create the file `DemoSnapShotTesting.js` in the `src` directory.
[DemoSnapShotTesting.js](DemoSnapShotTesting.js)
- Create the file `DemoSnapShotTesting.test.js` in the `src` directory. The unit test will render the component and save the output to the variable result in JSON format. The unit test will then compare the result to the snapshot.
[DemoSnapShotTesting.test.js](DemoSnapShotTesting.test.js)
- The first time the test is executed, the test will create a snapshot within the directory `__snapshots__`.
[__snapshots__\DemoSnapShotTesting.test.js.snap](__snapshots__\DemoSnapShotTesting.test.js.snap)
- Run the tests `npm test`

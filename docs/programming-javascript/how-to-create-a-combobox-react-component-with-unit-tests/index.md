---
title: "How To Create a Combobox React Component With Unit Tests"
date: 2025-02-02
categories:
  - "prog"
keywords: [react, combobox, unit-tests, components, testing]
---

In this article we will create a React component that displays a Combobox. The values of the combobox are set from an array. We will also create unit test to confirm the components functionality.

## Component Setup

- Create the app `npx create-react-app demo-select`.
- Change directory `cd demo-select`.
- Create a directory within `src` called `components`.
- Create a file called `DemoSelect.js` withing the components directory.
    
- Create a file called `DemoSelect.test.js`
    
- Run the tests `npm test`
    
- To use the component add an include line to your project file eg `import DemoSelect from './DemoSelect';`. Create a list of options eg `const optionList = ["apple", "orange"];`, create an instance of the component and pass the list to the component `<DemoSelect optionList={optionList} />`.


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-create-a-combobox-react-component-with-unit-tests](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-create-a-combobox-react-component-with-unit-tests)

## JavaScript Related Articles

- [Creating a Restfull Server Using NextJs](../creating-a-restfull-server-using-nextjs/index.md)
- [How To Build A Static Page That Refreshes Every 60 Seconds Using NextJs](../how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs/index.md)
- [How To Create a Next JS App From Scratch](../how-to-create-a-next-js-app-from-scratch/index.md)
- [How To Create a React Component That Returns a Promise With Unit Tests](../how-to-create-a-react-component-that-returns-a-promise-with-unit-tests/index.md)
- [How to  Handle Server-side API Routes in React](../how-to-handle-server-side-api-routes-in-react/index.md)

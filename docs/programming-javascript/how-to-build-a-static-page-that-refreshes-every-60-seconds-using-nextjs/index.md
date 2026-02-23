---
title: "How To Build A Static Page That Refreshes Every 60 Seconds Using NextJs"
date: 2025-02-02
categories:
  - "prog"
keywords: [nextjs, static-generation, revalidate, isr, javascript]
---

In this example, we will build a page that is rendered server-side using NextJs. NextJs will be configured to re-render the page every 60 seconds.

## Description

- The code for generating the server-side content is in the function `export async function getStaticProps(){`
- The page will refresh every 60 seconds because the return statement contain the revalidate 60. `return {props: {productsFromDb: productsFromDb}, revalidate: 60}`

## Getting Started

- Install package `npm install`
- Build the site `npm run build`
- Start the site `npm run start`


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-javascript/how-to-build-a-static-page-that-refreshes-every-60-seconds-using-nextjs)

## JavaScript Related Articles

- [Creating a Restfull Server Using NextJs](../creating-a-restfull-server-using-nextjs/index.md)
- [How To Create a Combobox React Component With Unit Tests](../how-to-create-a-combobox-react-component-with-unit-tests/index.md)
- [How To Create a Next JS App From Scratch](../how-to-create-a-next-js-app-from-scratch/index.md)
- [How To Create a React Component That Returns a Promise With Unit Tests](../how-to-create-a-react-component-that-returns-a-promise-with-unit-tests/index.md)
- [How to  Handle Server-side API Routes in React](../how-to-handle-server-side-api-routes-in-react/index.md)

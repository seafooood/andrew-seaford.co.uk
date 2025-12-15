# How To Build A Static Page That Refreshes Every 60 Seconds Using NextJs

In this example, we will build a page that is rendered server-side using NextJs. NextJs will be configured to re-render the page every 60 seconds.

## Description

- The code for generating the server-side content is in the function `export async function getStaticProps(){`
- The page will refresh every 60 seconds because the return statement contain the revalidate 60. `return {props: {productsFromDb: productsFromDb}, revalidate: 60}`

## Getting Started

- Install package `npm install`
- Build the site `npm run build`
- Start the site `npm run start`
# Creating a Restfull Server Using NextJs

## Description

- NextJs will automatically create routes for all of the files within the `pages\api` directory.
- In this example, a file called `pages\api\products.js` has been created that will return a JSON list of products.
- `pages\index`.js` demonstrates how to use the fetch function to get the product data from the api.

## Getting Started

- Install the packages `npm install`
- Run the server `npm dev run`
- View the products code in the file [pages\api\products.js](pages\api\products.js)
- Navigate to the page [http:\\localhost:3000\api\products](http:\\localhost:3000\api\products)
- or using Postman issue an `GET` request to the URL `http:\\localhost:3000\api\products`
- The result will be a list of products

    ```json
    [
        "apple",
        "orange",
        "pear"
    ]
    ```

- Navigate to the page [http:\\localhost:3000](http:\\localhost:3000)

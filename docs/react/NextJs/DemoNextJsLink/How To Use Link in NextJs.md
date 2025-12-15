# How To Use Link in NextJs

The NextJs Link component replaces `<a href`. The Link component is superior to a href because a href causes a full reload of the dom when switching between pages. Link is faster because it will only load the components that have changed into the DOM.

## Description

- The site has three pages inside the pages directory index, About and Contact.
- At the top of each page is a header containing links. The header is created using the component `Components\Header.js`.

    ```js
    import Link from 'next/link'

    const Header = () => (
        <>
            <Link href="\">Home</Link> / 
            <Link href="About">About</Link> / 
            <Link href="Contact">Contact</Link> 
        </>
    )

    export default Header;
    ```

- The header is displayed at the top of every page using `pages\_app.js`.

    ```js
    function MyApp({Component, pageProps}){
        return <>
            <Header />
            <Component {...pageProps} />
        </>
    }
    ```

## Getting Started

- Install the npm packages `npm install`
- Start the server `npm dev run`
- Navigate to the web page [http://localhost:3000](http://localhost:3000)
- Click the Home, About and Contact links to switch between pages.

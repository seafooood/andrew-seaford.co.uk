import Header from "../Components/Header.js"

function MyApp({Component, pageProps}){
    return <>
        <Header />
        <Component {...pageProps} />
    </>
}
export default MyApp;
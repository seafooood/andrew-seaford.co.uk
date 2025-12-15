import {useState, useEffect} from 'react'

export async function getStaticProps(){

    async function getProducts(){
        return ["apple", "pear", "orange", "melon"];
    }

    const productsFromDb = await getProducts();

    return {props: {productsFromDb: productsFromDb}, revalidate: 60}
}

const HomePage = ({productsFromDb}) => {
    return (
        <>
            <h1>Products</h1>
            <ul>
                {productsFromDb.map(product => <li key={product}>{product}</li>)}
            </ul>
        </>
    )
}

export default HomePage;
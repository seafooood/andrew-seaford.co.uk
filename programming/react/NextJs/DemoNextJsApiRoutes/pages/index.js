import {useState, useEffect} from 'react'

const HomePage = () => {
    const [products, setProducts] = useState([]);

    function fetchProducts() {
            fetch('/api/products')
            .then(res => res.json())
            .then(data => setProducts(data));
    }

    useEffect(() => fetchProducts(), [])

    return (
        <>
            <h1>Products</h1>
            <ul>
                {products.map(product => <li>{product}</li>)}
            </ul>
        </>
    )
}

export default HomePage;
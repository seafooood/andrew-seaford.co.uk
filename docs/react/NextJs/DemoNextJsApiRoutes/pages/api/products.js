
async function getProducts() {
    const products = ["apple", "orange", "pear"];    
    return products;
}

export default async function handler(req, res) {
    const products = await getProducts();
    res.status(200).json(products);
}
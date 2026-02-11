const apiUrl = 'http://127.0.0.1:5000/images';

// Function to update an image
async function updateImage(imageId, imageData) {
    const url = `${apiUrl}/${imageId}`;
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageData })
    });

    if (response.status === 204) {
        console.log(`Image ${imageId} updated successfully`);
    } else {
        const errorData = await response.json();
        console.error('Error updating image:', errorData);
    }
}

// Function to get an image
async function getImage(imageId) {
    const url = `${apiUrl}/${imageId}`;
    const response = await fetch(url, {
        method: 'GET',
    });

    if (response.ok) {
        const imageData = await response.json();
        console.log(`Image ${imageId} data:`, imageData);
    } else {
        const errorData = await response.json();
        console.error('Error fetching image:', errorData);
    }
}

// Example usage
const imageId = '1';
const imageData = 'base64encodedstring';

// Fetch the deafult image
getImage(imageId);

// Update the image
updateImage(imageId, imageData).then(() => {

    // Fetch the updated image data
    getImage(imageId);
});

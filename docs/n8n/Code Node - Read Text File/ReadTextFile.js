// The 'items' array contains the data from the previous node.
const outputItems = [];

for (const item of items) {
  // Check if there's a binary property named 'data'
  if (item.binary && item.binary.data) {
    // Check if the data is a Base64 string
    const base64Content = item.binary.data.data;
    if (typeof base64Content === 'string') {
      // Decode the Base64 string to a buffer
      const buffer = Buffer.from(base64Content, 'base64');
      
      // Convert the buffer to a string assuming UTF-8 encoding
      const fileContent = buffer.toString('utf8');

      // Split the content by newline characters
      const lines = fileContent.split('\n');
      
      // Create a new item for each line and add it to the output array
      for (const line of lines) {
        outputItems.push({
          json: {
            line: line
          }
        });
      }
    } else {
      // If the data is not a string, handle the original binary case
      outputItems.push({
        json: {
          error: 'Unexpected data format: Expected a Base64 string.'
        }
      });
    }
  } else {
    // If no binary data is found or the structure is unexpected, return an error message
    outputItems.push({
        json: {
          error: 'File content not found in expected binary property structure (item.binary.data).'
        }
      });
  }
}

return outputItems;
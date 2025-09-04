import base64

def process_items(items):
    """
    Processes a list of n8n items, reads file content from a binary property,
    and returns a new list of items where each item represents a line from the file.

    Args:
        items (list): The list of items from a previous n8n node.

    Returns:
        list: A new list of items, each containing a line from the file.
    """
    output_items = []
    
    # Iterate through each item received from the previous node.
    for item in items:
        # Check if the expected binary data structure exists.
        if 'binary' in item and 'data' in item['binary'] and 'data' in item['binary']['data']:
            base64_content = item['binary']['data']['data']
            
            # Ensure the content is a Base64 string before decoding.
            if isinstance(base64_content, str):
                try:
                    # Decode the Base64 string to bytes.
                    decoded_bytes = base64.b64decode(base64_content)
                    
                    # Decode the bytes to a string assuming UTF-8 encoding.
                    file_content = decoded_bytes.decode('utf-8')
                    
                    # Split the content into a list of lines.
                    lines = file_content.split('\n')
                    
                    # For each line, create a new output item with the line content.
                    for line in lines:
                        output_items.append({
                            'json': {
                                'line': line
                            }
                        })
                except (base64.binascii.Error, UnicodeDecodeError) as e:
                    # Append an error item if decoding fails.
                    output_items.append({
                        'json': {
                            'error': f'Decoding error: {e}'
                        }
                    })
            else:
                # Append an error item if the data is not a string.
                output_items.append({
                    'json': {
                        'error': 'Unexpected data format: Expected a Base64 string.'
                    }
                })
        else:
            # Append an error item if the expected data structure is missing.
            output_items.append({
                'json': {
                    'error': 'File content not found in expected binary property structure.'
                }
            })
    
    return output_items

# return process_items(items) #uncomment this line when using in n8n
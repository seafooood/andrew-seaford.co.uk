---
keywords: [n8n, code node, python, JsProxy, pyodide]
---

# Code Node - JsProxy to Python

```python
# The input is the single n8n item object.
item_wrapper = item

# --- DEBUG STEP: Print the full incoming item structure ---
# We use copy.deepcopy to safely convert the JsProxy object for JSON serialization.
try:
    # Safely convert the incoming item object (JsProxy) to a standard Python dictionary
    # by using the .to_py() method (available in the Pyodide environment) 
    # and then serialize it using the json library.
    item_dict = item_wrapper.to_py()
    print("--- FULL INCOMING ITEM STRUCTURE ---")
    print(json.dumps(item_dict, indent=2))
    print("------------------------------------")
except Exception as e:
    print(f"DEBUG ERROR: Could not serialize item for printing. Error: {e}")
    # Fallback to the original, less-detailed print
    print("Full Item Object (JsProxy):", item_wrapper)
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/n8n/code-node-jsproxy-to-python](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/n8n/code-node-jsproxy-to-python)

## N8N Related Articles

- [Code Node - Read Text File](../code-node-read-text-file/index.md)
- [How To Install n8n with Langchain.js](../how-to-install-n8n-with-langchain.js/index.md)
- [How To Chat With Langflow From A Python Script](../../langflow/how-to-chat-with-langflow-from-a-python-script/index.md)
- [How To Enable Logging In Langflow](../../langflow/how-to-enable-logging-in-langflow/index.md)
- [How To Install Langflow on Ubuntu Using Docker](../../langflow/how-to-install-langflow-on-ubuntu-using-docker/index.md)

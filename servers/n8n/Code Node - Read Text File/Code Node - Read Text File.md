# Code Node - Read Text File

This n8n code node reads a file from a previous node and outputs an array of lines from that file. It is particularly useful for processing text files line-by-line in a workflow.

## How It Works

The node first checks for the presence of a binary file in the item.binary.data property, which is the standard way n8n stores file data from nodes like "Read/Write Files from Disk." The code then takes the Base64-encoded string that represents the file's content and converts it back into a binary buffer.

Once the data is in a buffer, the code decodes it into a UTF-8 string, which is the standard character encoding for most text files. Finally, it splits the string into an array of individual lines using the newline character \n as the delimiter.

## How to Use

- Add a "Read/Write Files from Disk" Node: Start your workflow with this node to read a file from your file system.

- Add a "Code" Node: Connect the output of the file node to the input of a code node.

- Paste the Code: Copy and paste the provided code into the code node's editor.

[ReadTextFile.js](<ReadTextFile.js>)

or 

[ReadTextFile.py](<ReadTextFile.py>) !!! **Uncomment the last line of the python script** !!!

- Execute the Workflow: When the workflow runs, the code node will receive the file's content, process it, and output a JSON object containing an array of lines, accessible via the lines property.

The output will look something like this:
```JSON
[
    {
    "line": "#!/bin/sh"
    },
    {
    "line": "if [ -d /opt/custom-certificates ]; then"
    },
    {
    "line": "  echo \"Trusting custom certificates from /opt/custom-certificates.\""
    },
    {
      ...
  }
]
```

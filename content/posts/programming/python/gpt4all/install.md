https://www.linode.com/docs/guides/create-a-python-virtualenv-on-ubuntu-18-04/

sudo apt install virtualenv
mkdir ~/python-environments && cd ~/python-environments
virtualenv --python=python3 env
ls env/lib
source env/bin/activate

pip install gpt4ll
nano p.py

```python
from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
output = model.generate("The capital of France is ", max_tokens=3)
print(output)
```

python3 p.py

- failed with error " Unable to instantiate model: CPU does not support AVX"
https://forums.virtualbox.org/viewtopic.php?t=111636


cd ~/python-environments
source env/bin/activate
# How To Install GPT4all on Ubuntu

- Create a python virtual environment

```bash
sudo apt install virtualenv
mkdir ~/python-environments && cd ~/python-environments
virtualenv --python=python3 env
ls env/lib
source env/bin/activate
```

- Insall gpt4all

```bash
pip install gpt4ll
```


- Create a test script called p.py

```bash
nano p.py
```

```python
from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
output = model.generate("The capital of France is ", max_tokens=3)
print(output)
```

- Exectue scipt

```bash
python3 p.py
```

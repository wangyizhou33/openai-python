## README

### Dependency
```sh
pip install openai Pillow
```

### Credentials file
```json
{
    "azure-chatgpt-key" : "xxxxx",
    "deepseek-key": "xxxxx"
}
```


### References
1. [openai-python](https://github.com/openai/openai-python)

### Facts
1. The azure deployment does not contain `image` capability. So `azure_image.py` does not work.
2. `gpt-4o` model does not support `completions` capability. So there is no azure equivalent of `deepseek_completion.py`
3. try ollama
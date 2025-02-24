## README

### Dependency
```sh
pip install openai Pillow ollama
```

### Credentials file
```json
{
    "llmapi-url": "https://llmapi-aiinfra.navinfo.com/v1/",
    "llmapi-key": "xxx",
    "public-deepseek-url": "https://api.deepseek.com",
    "public-deepseek-key": "xxx",
    "azure-chatgpt-url": "https://wyzgpt4.openai.azure.com",
    "azure-chatgpt-key": "xxx",
    "sglang-v3-url": "http://10.41.112.18:30000/",
    "sglang-v3-key": "xxx",
    "sglang-r1-url": "http://10.41.112.38:30000/",
    "sglang-r1-key": "xxx",
    "ollama-url": "http://10.41.0.98:11434"
}
```
Note:  
* `llmapi` is the gateway for all private-hosted llm backbends. 
* `public-deepseek` is the hosted by deepseek company. We use it for api behavior comparison. Key is purchased personally.
* `azure-chatgpt` is the microsoft hosted chatgpt service purchased by navinfo. Key is given per user.
* `sglang-v3` is the sglang backend of the v3 model, by-passing llmapi. For test purpose. llmapi reroutes requests selectively, which sometimes creates confusion.
* `sglang-r1` is the sglang backend of the r1 model, by-passing llmapi. For the same reason as above.



### References
1. [openai-python](https://github.com/openai/openai-python)

### Facts
1. The azure deployment does not contain `image` capability. So `azure_image.py` does not work.
2. `gpt-4o` model does not support `completions` capability. So there is no azure equivalent of `deepseek_completion.py`
3. My local `ollama` instance is at `http://localhost:7869`
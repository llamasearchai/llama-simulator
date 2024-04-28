# llama-simulator

A comprehensive simulation framework for AI research and testing scenarios, with a focus on MLX acceleration and advanced simulation capabilities.

## Installation

```bash
pip install -e .
```

## Usage

```python
from llama_simulator import LlamaSimulatorClient

# Initialize the client
client = LlamaSimulatorClient(api_key="your-api-key")
result = client.query("your query")
print(result)
```

## Features

- Fast and efficient
- Easy to use API
- Comprehensive documentation

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/nikjois/llama-simulator.git
cd llama-simulator

# Install development dependencies
pip install -e ".[dev]"
```

### Testing

```bash
pytest
```

## License

MIT

## Author

Nik Jois (nikjois@llamasearch.ai)

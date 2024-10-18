#!/usr/bin/env python3
"""
Llama Simulator - Python package for LlamaSearch AI
"""

from setuptools import setup, find_packages

setup(
    name="llama_simulator",
    version="0.1.0",
    description="A comprehensive simulation framework for AI research and testing scenarios, with a focus on MLX acceleration and advanced simulation capabilities.",
    long_description="""# llama-simulator

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
""",
    long_description_content_type="text/markdown",
    author="Nik Jois",
    author_email="nikjois@llamasearch.ai",
    url="https://github.com/llamasearchai/llama-simulator",
    project_urls={
        "Documentation": "https://github.com/llamasearchai/llama-simulator",
        "Bug Tracker": "https://github.com/llamasearchai/llama-simulator/issues",
        "Source Code": "https://github.com/llamasearchai/llama-simulator",
    },
    py_modules=['policy-network', 'generators-init', 'base-environment', 'environment-registry', 'federated-init', 'specialized-agents-init', 'ethical-init', 'environments-init', 'config-utils', 'simulation-init', 'base-agent', 'simulation-lab', 'models-init', 'agents-init', 'utils-init', 'agent-registry', 'resnet-model'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)

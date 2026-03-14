# LibreFang Model Catalog

Community-maintained model metadata catalog for [LibreFang](https://github.com/librefang/librefang) -- the open-source Agent Operating System.

This repository is the source of truth for model metadata (pricing, context windows, capabilities). When new models are released (e.g. GPT-5.5, Claude 5), anyone can submit a PR here without touching the LibreFang binary.

## Structure

```
model-catalog/
├── providers/          # One TOML file per provider
│   ├── anthropic.toml
│   ├── openai.toml
│   ├── gemini.toml
│   └── ...
├── aliases.toml        # Global alias mappings (e.g. "sonnet" -> "claude-sonnet-4-6")
├── schema.toml         # Reference schema documenting all fields
├── scripts/
│   └── validate.py     # Validation script
├── CONTRIBUTING.md     # How to add a new model
└── LICENSE             # MIT
```

## How LibreFang Uses This Catalog

LibreFang ships with a built-in model catalog compiled into the binary. This repository serves as the upstream source. To update your local catalog:

```bash
librefang catalog update
```

This fetches the latest TOML files from this repository and merges them into your local catalog.

### Custom Local Models

You can also add custom models locally without submitting a PR:

```bash
# Add to your personal config
# ~/.librefang/model_catalog.toml

[[models]]
id = "my-custom-model"
display_name = "My Custom Model"
provider = "ollama"
tier = "local"
context_window = 32768
max_output_tokens = 4096
input_cost_per_m = 0.0
output_cost_per_m = 0.0
supports_tools = true
supports_vision = false
supports_streaming = true
```

## Schema Reference

Each provider file contains a `[provider]` section and one or more `[[models]]` entries:

```toml
[provider]
id = "provider-id"                  # Unique provider identifier
display_name = "Provider Name"      # Human-readable name
api_key_env = "PROVIDER_API_KEY"    # Environment variable for API key
base_url = "https://api.example.com"  # Default API endpoint
key_required = true                 # Whether an API key is needed

[[models]]
id = "model-id"                    # Unique model identifier (API model ID)
display_name = "Human Name"        # Human-readable display name
tier = "smart"                     # frontier | smart | balanced | fast | local
context_window = 128000            # Maximum input tokens
max_output_tokens = 16384          # Maximum output tokens
input_cost_per_m = 2.50            # USD per million input tokens
output_cost_per_m = 10.0           # USD per million output tokens
supports_tools = true              # Tool/function calling support
supports_vision = true             # Vision/image input support
supports_streaming = true          # Streaming response support
aliases = ["alias1", "alias2"]     # Short names for this model
```

### Tier Definitions

| Tier | Description | Examples |
|------|-------------|----------|
| `frontier` | Most capable, cutting-edge models | Claude Opus, GPT-4.1, Gemini 2.5 Pro |
| `smart` | Smart, cost-effective models | Claude Sonnet, GPT-4o, Gemini 2.5 Flash |
| `balanced` | Balanced speed/cost | GPT-4.1 Mini, Llama 3.3 70B |
| `fast` | Fastest, cheapest | GPT-4o Mini, Claude Haiku |
| `local` | Local models (zero cost) | Ollama, vLLM, LM Studio |

## How to Add a New Model

1. Edit the appropriate provider file in `providers/`
2. Run validation: `python scripts/validate.py`
3. Submit a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

## Validation

```bash
python scripts/validate.py
```

This checks all TOML files for correctness: required fields, valid tiers, non-negative costs, no duplicate IDs.

## Current Stats

- **30+ providers** including Anthropic, OpenAI, Google, DeepSeek, Groq, Mistral, xAI, and more
- **190+ models** with pricing, context windows, and capability flags
- **80+ aliases** for quick model selection

## License

MIT License. See [LICENSE](LICENSE).

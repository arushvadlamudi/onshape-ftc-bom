# onshape_ftc_bom

Generate FTC-ready BOMs and cutlists from Onshape assemblies with validation.

## Installation

```bash
pip install onshape_ftc_bom
```

## Quick Start

```python
from onshape_ftc_bom import OnshapeFtcBom

instance = OnshapeFtcBom()
result = instance.run()
print(result)
```

## Features

- Onshape Assembly BOM export to CSV/JSON
- Part metadata validation (material, thickness, vendor, quantity)
- Config-aware BOM generation for variants

## API Reference

### `OnshapeFtcBom`

#### Constructor

```python
OnshapeFtcBom(options: OnshapeFtcBomOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `OnshapeFtcBomResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/onshape_ftc_bom/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT

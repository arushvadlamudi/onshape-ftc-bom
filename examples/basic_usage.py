#!/usr/bin/env python3
"""Basic usage example for onshape_ftc_bom."""

from onshape_ftc_bom import OnshapeFtcBom, OnshapeFtcBomOptions


def main() -> None:
    # Create with default options
    instance = OnshapeFtcBom()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = OnshapeFtcBomOptions(verbose=True)
    instance = OnshapeFtcBom(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()

"""
onshape_ftc_bom - Generate FTC-ready BOMs and cutlists from Onshape assemblies with validation.
"""

__version__ = "0.1.0"

from .onshape_assembly_bom_export_to import OnshapeFtcBom
from .types import OnshapeFtcBomOptions, OnshapeFtcBomResult
from .exceptions import OnshapeFtcBomError, ConfigurationError, ValidationError

__all__ = [
    "OnshapeFtcBom",
    "OnshapeFtcBomOptions",
    "OnshapeFtcBomResult",
    "OnshapeFtcBomError",
    "ConfigurationError",
    "ValidationError",
]

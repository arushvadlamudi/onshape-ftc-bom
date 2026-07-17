"""Type definitions for onshape_ftc_bom."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class OnshapeFtcBomOptions:
    """Configuration options for OnshapeFtcBom.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Onshape Assembly BOM export to CSV/JSON
        feature_2: Configuration for: Part metadata validation (material, thickness, vendor, quantity)
        feature_3: Configuration for: Config-aware BOM generation for variants
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None


@dataclass
class OnshapeFtcBomResult:
    """Result returned by OnshapeFtcBom operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None

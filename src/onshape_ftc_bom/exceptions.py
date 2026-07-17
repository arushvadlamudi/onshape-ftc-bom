"""Custom exceptions for onshape_ftc_bom."""

from __future__ import annotations


class OnshapeFtcBomError(Exception):
    """Base exception for all OnshapeFtcBom errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(OnshapeFtcBomError):
    """Raised when the SDK is misconfigured."""


class ValidationError(OnshapeFtcBomError):
    """Raised when input validation fails."""


class TimeoutError(OnshapeFtcBomError):
    """Raised when an operation exceeds its time limit."""

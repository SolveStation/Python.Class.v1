# ============================================================================
# Custom Exceptions
# ============================================================================


class FileManagerError(Exception):
    """Base exception for FileManager errors."""

    pass


class FileNotFoundError(FileManagerError):
    """Raised when a required file is not found."""
    pass


class FileCorruptedError(FileManagerError):
    """Raised when a CSV file is corrupted or has invalid format."""

    pass


class DuplicateEntryError(FileManagerError):
    """Raised when attempting to create a duplicate entry."""

    pass


class ValidationError(FileManagerError):
    """Raised when data validation fails."""

    pass


class PermissionError(FileManagerError):
    """Raised when file permissions are insufficient."""

    pass

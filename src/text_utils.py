
"""Utilities for cleaning and formatting text."""


def clean_name(raw):
    """Clean a name by removing extra whitespace and applying title case."""
    return " ".join(raw.split()).title()

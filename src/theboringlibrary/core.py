"""This literally does nothing."""

NOTHING = None

def do_nothing() -> None:
    """Returns None."""
    return NOTHING

def some_untested_fn() -> None:
    """It's actually tested now..."""
    return do_nothing()

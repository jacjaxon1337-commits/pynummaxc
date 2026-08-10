import pkg_resources

pkg_resources.require("pynummax>=1.0.0")

from .core import X

__all__ = ["X"]

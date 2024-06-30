from __future__ import annotations

__title__ = "ampharos_images"
__author__ = "Bijij"
__license__ = "MIT"
__copyright__ = "Copyright 2023-present Bijij"
__version__ = "3.1.0"

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ampharos.types import Pokemon

from .utils import get_base_dir


BASE_DIR = get_base_dir()

IMAGES_AVAILABLE = True

def get_image(pokemon: Pokemon) -> bytes | None:
    try:
        with open(BASE_DIR / f"img/{pokemon._term}.png", "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None

from abc import ABC, abstractmethod
from typing import Any, Optional
import requests


class BaseAPIClass(ABC):
    """Абстрактный класс для работы с API"""

    def __init__(self, base_url: str, api_key: Optional[str] = None):
        # " Инициализация API"
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

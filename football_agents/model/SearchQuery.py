from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class SearchQuery:
    search_query: str
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

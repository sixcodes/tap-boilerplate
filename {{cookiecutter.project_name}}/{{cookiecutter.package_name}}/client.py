from typing import Dict


class Client:

    BASE_URL = "https://"

    def __init__(self, config: Dict[str, str], state: Dict[str, str]):
        self.config = config
        self.last_record: str = state.get("last_record", config.get("start_date", ""))

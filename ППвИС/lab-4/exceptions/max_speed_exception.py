from utility.config import config


class MaxSpeedException(Exception):
    """Exception was raise because max speeds exceeds maximum or below min."""

    def __init__(
        self,
        max_speed: float,
        message=f"Max speed was not in range ({config.get('min_speed')}, {config.get('max_speed')}) km/h range. "
    ):
        message += f"Given was {max_speed}."
        super().__init__(message)

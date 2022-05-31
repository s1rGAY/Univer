from utility.config import config


class BrakingSpeedException(Exception):
    """Exception was raised because braking speed exceeds max or below min possible values."""

    def __init__(
        self,
        braking_speed: float,
        message=f"Braking speed wasn't in range ({config.get('min_braking_speed')}, {config.get('max_braking_speed')}) km/h. ",
    ):
        message += f"Given braking speed {braking_speed}."
        super().__init__(message)

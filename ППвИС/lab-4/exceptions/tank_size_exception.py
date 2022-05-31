from utility.config import config


class TankSizeException(Exception):
    """Exception was raised because given tank size exceeds maximum allowed."""

    def __init__(
        self,
        given_tank_size: float,
        message=f"Tank size is not in ({config.get('min_tank_size')}, {config.get('tank_size')}) liters range. "
    ):
        message += f"Given was {given_tank_size} liters."
        super().__init__(message)

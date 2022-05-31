from utility.config import config


class MaxAccelerationRatioException(Exception):
    """Exception was raised because given max acceleration ratio was not supported."""

    def __init__(
        self,
        given_ratio: float,
        message=f"Max acceleration ratio is not ({config.get('min_max_acceleration_ratio')}, {config.get('max_acceleration_ratio')}) km/h range. "
    ):
        message += f"Given ratio was {given_ratio}."
        super().__init__(message)

from utility.config import config


class MinAccelerationRatioException(Exception):
    """Exception was raised because ratio wasn't fullfilling conditions."""

    def __init__(
        self,
        given_ratio: float,
        message=f"Min acceleration ratio was not in a (0, {config.get('min_acceleration_ratio')}) range. "
    ):
        message += f"Given was {given_ratio}."
        super().__init__(message)

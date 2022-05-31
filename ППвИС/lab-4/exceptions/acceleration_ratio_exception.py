from utility.config import config


class AccelerationRatioException(Exception):
    """Exception was raise because acceleration ratio parameter wasn't fullfiling all conditions."""

    def __init__(
        self,
        given_acceleration_ratio: float,
        message=f"Acceleration ratio wasn't in (0, {config.get('acceleration_ratio')}) km/h range. ",
    ):
        message += f"Given was {given_acceleration_ratio} km/h."
        super().__init__(message)

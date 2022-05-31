from utility.config import config


class OnReserveBorderException(Exception):
    """Exception was raise because on border mark wasn't fullfilling conditions."""

    def __init__(
        self,
        on_reserve_border: float,
        message=f"On reserve border is not (0, {config.get('on_reserve_border')}). "
    ):
        message += f"Given was {on_reserve_border} liters."
        super().__init__(message)

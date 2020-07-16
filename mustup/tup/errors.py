import logging

logger = logging.getLogger(
    __name__,
)


class NotUnderTup(
            Exception,
        ):
    pass

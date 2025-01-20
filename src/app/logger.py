import logging
import sys
from logging import Formatter, Handler


def build_formatter() -> Formatter:
    formatter = Formatter("%(levelname)s:\t%(name)s --- %(message)s")
    return formatter


def build_handler() -> Handler:

    handler = logging.StreamHandler(sys.stdout)
    formatter = build_formatter()
    handler.setFormatter(formatter)

    return handler


def configure_logger(log_level: str, root_name: str = "src"):
    handler = build_handler()

    project_logger = logging.getLogger(root_name)
    project_logger.setLevel(log_level)
    project_logger.addHandler(handler)
    project_logger.propagate = False

    return project_logger

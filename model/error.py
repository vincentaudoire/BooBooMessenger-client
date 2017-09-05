class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class MissingKeyError(Error):
    """Exception raise from missing value in the DTO"""

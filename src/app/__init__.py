def application():
    # pylint: disable=C0415
    # Must be imported in the def context to avoid circular dependencies
    from .application import Application

    return Application()

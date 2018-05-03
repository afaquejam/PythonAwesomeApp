class Error(Exception):
    def __init__(self, error_message=None):
        if error_message is None:
            error_message = "Error occured in {}.".format(type(self))
        super(Error, self).__init__(error_message)

class PublicIPAddressError(Error):
    def __init__(self, error_message=None):
        super(PublicIPAddressError, self).__init__(error_message)
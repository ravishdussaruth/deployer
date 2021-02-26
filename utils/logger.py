class Logger:
    __environment = None

    def __init__(self):
        pass

    def set_environment(self, environment: str):
        """
        Log into the terminal.

        :param environment:
        :type environment: str

        :return:
        """

        self.__environment = environment

    def log(self, message):
        """
        Print message into console.

        :param message:
        :type message: str

        :returns:
        """

        print('[{environment}]: {message}'.format(environment=self.__environment,
                                                  message=message))

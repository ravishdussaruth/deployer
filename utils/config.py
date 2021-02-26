from configparser import ConfigParser


class Config:
    # Set default environment to staging.
    _key = 'staging'
    _path = 'config.ini'

    parser = None

    def __init__(self, key: str = None, path: str = None):
        self._key = key
        self._path = path

    def set_config_file_path(self, path: str):
        """
        Set the config file path.

        :param path
        :type path: str

        :return:
        """

        self._path = path

    def new(self):
        """
        Create new config parser.

        :returns: ConfigParser
        """

        return ConfigParser()

    def init(self):
        """
        Initialize the config file.

        :return:
        """
        self.parser = ConfigParser()
        self.parser.read(self._path)

    def get(self, key: str):
        """
        Get the config from file section.

        :param key
        :type key: str

        :returns:
        """

        return self.parser.get(self._key, key)

    def write(self, path: str, config: ConfigParser):
        """
        Write config file.

        :param path:
        :type path: str

        :param config:
        :type config: ConfigParser

        :returns:
        """

        config_file = open(path, 'w')
        config.write(config_file)
        config_file.close()

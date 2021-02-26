from utils.config import Config
from datetime import datetime


class DeployerConfig(Config):
    """
    The deployer configuration file, where the config like last deployed, number of repositories created are stored.
    """

    def last_deployed(self):
        """
        Get the last deployed date.

        :returns: str
        """

        return self.get('deployed_on')

    def old_releases(self):
        """
        The name of old releases.

        :returns: tuple
        """

        return eval(self.get('repos'))

    def deployed_count(self) -> int:
        """
        The number of deploys.

        :returns: int
        """

        return int(self.get('deployed_count'))

    def new_config(self, count: str):
        """
        Instantiate a new config file.

        :param count:
        :type count:str

        :return: None
        """

        parser = self.new()
        parser.add_section(self._key)
        parser.set(self._key, 'deployed_on', str(datetime.today()))
        parser.set(self._key, 'deployed_count', count)

        self.write(self._path, parser)

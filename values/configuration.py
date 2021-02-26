from utils.config import Config


class Configuration(Config):
    """
    The configuration file, where environment and other data are stored.
    """

    def repository(self):
        """
        Get the repository url.

        :return: str
        """

        return self.get('repository')

    def branch(self):
        """
        The branch to clone files from.

        :returns: str
        """

        return self.get('branch')

    def root_path(self):
        """
        The project root path.

        :returns: str
        """

        return self.get('path')

    def number_releases_to_keep(self):
        """
        The number of releases to keep.

        :returns: str
        """

        return int(self.get('keep_releases'))

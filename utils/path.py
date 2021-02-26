import os


class Path:
    # The project path.
    project_path = '/var/www/html'

    def __init__(self, path: str):
        """
        Init the paths class with the deploy directory path.

        :param path:
        :type path: str
        """

        self.project_path = path

    def set_project_path(self, path: str):
        """
        Set project path.

        :param path:

        :type path: str

        :return:
        """

        self.project_path = path

    def deployer_folder(self) -> str:
        """
        The deploy folder, in which the deploy config will be stored.

        :return:
        """

        return self.__make_path_in_root_directory('/.deployer')

    def the_deploy_config_file(self):
        """
        The deploy config file, in which the configs are stored.

        :return:
        """

        return self.__make_path_in_root_directory('/.deployer/config.ini')

    def release_path(self) -> str:
        """
        Determine the release path.

        :returns: str
        """

        return self.__make_path_in_root_directory('/current')

    def root(self):
        """
        The project root.

        :returns: str
        """

        return self.project_path

    def releases_directory(self):
        """
        The directory in which all releases will be stored.

        :return: str
        """

        return self.__make_path_in_root_directory('releases')

    def released_copy(self, release: str):
        """
        The path to copy the old release to.

        :param release:
        :type release: str

        :returns:
        """

        return self.releases_directory() + (release if release.startswith('/') else '/' + release)

    def __make_path_in_root_directory(self, path: str):
        """
        Create a new path in root directory.

        :param path:
        :type path: str

        :returns:
        """

        return self.project_path + (path if path.startswith('/') else '/' + path)

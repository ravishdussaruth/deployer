from utils.git import Git
from utils.path import Path
from datetime import datetime
from utils.system import System
from utils.logger import Logger
from values.configuration import Configuration
from values.deployer_configuration import DeployerConfig
import sys, getopt


class App(System, Logger):
    config, path, git, deployer_config = None, None, None, None

    def __init__(self, env: str):
        super(Logger, self).__init__()

        self.set_environment(env.upper())
        self._handle(env.upper())

    def _handle(self, env: str):
        """
        Run all the commands needed.

        :param env:
        :type env: str

        :return:
        """

        # Preparing the environment.
        self.log('Preparing the environment.')
        self._prepare(env)

        # Run commands before installation.
        self.log('Running commands before the install.')
        self.__before()

        # Run commands to install the project.
        self.log('Running commands to install the project.')
        self._install()

        # Run commands after installing the project.
        self.log('Running commands after the installation.')
        self.__after()

    def _prepare(self, env: str):
        """
        Prepare the environment before installing project.

        :param env:
        :type env: str

        :returns: None
        """

        self.log('Initializing configuration.')
        self.init(env)

        self.log('Checking if project root folder exists')

        # Will tell us if this is a first deploy.
        new = not self._exists(self.path.root())

        if new:
            self.log('Creating new repo: ' + self.path.root())
            self.init_root()

            self.log('Cloning project in path: ' + self.path.release_path())
            self.clone()

        self.log('Reading Deployer config file.')
        self.init_deployer_config()

        # Check if deployer config file exists.
        if not self._exists(self.path.the_deploy_config_file()):
            self.log('Writing first deployer config.')
            self.deployer_config.new_config('0')

        if not new:
            # Move current release to new destination.
            self.log('Retrieving last deployed data.')
            new_deploy_count = self.deployer_config.deployed_count() + 1

            self.log('Backing up old release to: ' + self.path.releases_directory())
            self.move_current_release(str(new_deploy_count))

            self.log('Cloning project in path: ' + self.path.release_path())
            self.clone()

            self.log('Writing in deployer config.')
            self.deployer_config.new_config(str(new_deploy_count))

            self.log('Removing old releases.')
            self.remove_old_release()

    def init_root(self):
        """
        Init project root folder.

        :return:
        """

        self._create_directory(self.path.root())
        self._create_directory(self.path.deployer_folder())

    def init(self, env: str):
        """
        Initialize config file.

        :return:
        """

        self.config = Configuration(env, self._config_file_path())
        self.config.init()

        self.init_path()
        self.init_git()

    def init_path(self):
        """
        Init project path.

        :return:
        """

        self.path = Path(self.config.get('path'))

    def init_git(self):
        """
        Init git Class.

        :return:
        """

        self.git = Git(self.config.repository(), self.config.branch())

    def init_deployer_config(self):
        """
        Read the deployer config file.

        :return:
        """

        self.deployer_config = DeployerConfig(key='CONFIG', path=self.path.the_deploy_config_file())
        self.deployer_config.init()

    def move_current_release(self, new_name: str):
        """
        Move current release.

        :param new_name:
        :type new_name: str

        :returns:
        """

        self._move_dir(self.path.release_path(), self.path.released_copy(new_name))

    def remove_old_release(self):
        """
        Remove old release.

        :returns: None
        """

        directory_length = self.number_of_files(self.path.releases_directory())
        release_to_keep = self.config.number_releases_to_keep()

        if directory_length > release_to_keep:
            file_list = self.list_files(self.path.releases_directory())
            file_list.sort(reverse=True)

            for release in file_list[-(directory_length - release_to_keep):]:
                self._remove(self.path.released_copy(release))

    def __before(self):
        """
        Run this method before installing the application.

        :return:
        """

        self._run_command(self._create_command(self._before_commands()))

    def _install(self):
        """
        Run the command to install the project.

        :return:
        """

        self._run_command(self._create_command(self._install_commands()))

    def __after(self):
        """
        Run commands after the install.

        :return:
        """

        self._run_command(self._create_command(self._after_commands()))

    def _before_commands(self) -> list:
        """
        The commands to run in the before section.

        :returns: list
        """

        return []

    def _after_commands(self) -> list:
        """
        The commands to run after the install.

        :return:
        """

        return []

    def _install_commands(self):
        """
        The install commands.

        :returns: list
        """

        return [
            'yarn'
        ]

    def clone(self):
        """
        Clone the repo.

        :returns:
        """

        self._run_command(self.git.clone_repo(self.path.release_path()))

    def _config_file_path(self) -> str:
        """
        Return the config file path.

        :returns: str
        """

        return 'config.ini'


if __name__ == '__main__':
    App(sys.argv[1:][0])

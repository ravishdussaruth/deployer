import os
import shutil


class System:
    def __init__(self):
        pass

    def _create_command(self, commands: list) -> str:
        """
        Concatenating commands to form a string.

        :param commands: list

        :returns: str
        """

        return ' && '.join(commands)

    def _run_command(self, command: str):
        """
        Run shell commands.

        :param command:
        :type command: str

        :return:
        """

        if len(command) > 0:
            os.system(command)

    def _cd(self, path: str):
        """
        Go to path

        :param path:
        :type path: str

        :return:
        """

        self._run_command('cd ' + path)

    def _mkdir(self, path: str):
        """
        Create a directory.

        :param path:
        :type path: str

        :return:
        """
        os.mkdir(path)

    def _clone_dir(self, src: str, dest: str):
        """
        Clone a directory.

        :param src:
        :param dest:

        :type src: str
        :type: dest: str

        :return:
        """

        shutil.copytree(src, dest)

    def _move_dir(self, src: str, dest: str):
        """
        Move a directory from src to dest specified.

        :param src:
        :param dest:

        :type src: str
        :type dest: str

        :return:
        """

        shutil.move(src, dest)

    def _exists(self, path: str) -> bool:
        """
        Will tell us if this path exists.

        :param path
        :type path: str

        :return: bool
        """

        return os.path.exists(path)

    def _remove(self, path: str):
        """
        Remove path contents.

        :param path:
        :type path: str

        :return:
        """

        shutil.rmtree(path)

    def _create_directory(self, path: str):
        """
        Create mentioned directory.

        :param path:
        :type path: str

        :return: None
        """

        if not self._exists(path):
            self._mkdir(path)

    def list_files(self, path: str):
        """
        List all files available in this path.

        :param path:
        :type path: str

        :returns:
        """

        return os.listdir(path)

    def number_of_files(self, path: str):
        """
        Number of files in this repo.

        :param path:
        :type path: str

        :returns:
        """

        return len(self.list_files(path))

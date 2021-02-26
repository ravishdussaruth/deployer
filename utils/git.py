class Git:
    # The git repo.
    _repo = None
    _branch = None

    def __init__(self, repo: str, branch: str):
        """
        Instantiate the git repo and branch to clone.

        :param repo:
        :param branch:
        :type repo: str
        :type branch: str
        """

        self._repo = repo
        self._branch = branch

    def clone_repo(self, dir='current') -> str:
        """
        Clone the repo.

        :param dir:
        :type dir: str

        :returns: str
        """

        return 'git clone --single-branch --branch {branch} {repository} {dir}'.format(branch=self._branch,
                                                                                       repository=self._repo,
                                                                                       dir=dir)

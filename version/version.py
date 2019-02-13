class CheckWrapper:
    # implement https://semver.org/ checker
    def __init__(self, version):
        Utilities.check_version(version)

        self.major = Utilities.get_major(version)
        self.minor = Utilities.get_minor(version)
        self.patch = Utilities.get_patch(version)

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'

    def __lt__(self, other):
        Utilities.check_before_comparison(other)

        is_major = self.major < other.major
        is_minor = self.minor < other.minor
        is_patch = self.patch < other.patch

        return is_major or is_minor or is_patch

    def __le__(self, other):
        Utilities.check_before_comparison(other)

        is_major = self.major <= other.major
        is_minor = self.minor <= other.minor
        is_patch = self.patch <= other.patch

        return is_major or is_minor or is_patch

    def __eq__(self, other):
        Utilities.check_before_comparison(other)

        is_major = self.major == other.major
        is_minor = self.minor == other.minor
        is_patch = self.patch == other.patch

        return is_major and is_minor and is_patch

    def __ne__(self, other):
        Utilities.check_before_comparison(other)

        is_major = self.major != other.major
        is_minor = self.minor != other.minor
        is_patch = self.patch != other.patch

        return is_major or is_minor or is_patch

    def __gt__(self, other):
        Utilities.check_before_comparison(other)

        is_major = self.major > other.major
        is_minor = self.minor > other.minor
        is_patch = self.patch > other.patch

        return is_major or is_minor or is_patch

    def __ge__(self, other):
        Utilities.check_before_comparison(other)

        is_major = self.major >= other.major
        is_minor = self.minor >= other.minor
        is_patch = self.patch >= other.patch

        return is_major or is_minor or is_patch


class Utilities:
    BASE_ENCODING = 'utf-8'

    @staticmethod
    def get_major(version):
        if isinstance(version, int):
            return version

        if isinstance(version, float):
            return int(version)

        if isinstance(version, bytes):
            version = version.decode(Utilities.BASE_ENCODING)

        if isinstance(version, str):
            group = version.split('.')

            if len(group) == 0:
                raise TypeError

            major_ver = group[0]
            major_ver = major_ver if major_ver[0] != 'v' else major_ver[1:]

            return int(major_ver)

    @staticmethod
    def get_minor(version):
        if isinstance(version, int):
            return 0

        if isinstance(version, float):
            integer = int(version)
            decimal = version - integer
            precise = 100  # keep only 3 signs
            return int(decimal * precise)

        if isinstance(version, bytes):
            version = version.decode(Utilities.BASE_ENCODING)

        if isinstance(version, str):
            group = version.split('.')

            # handle case version = 'v12'
            if len(group) == 1:
                return 0

            minor_ver = group[1]

            return int(minor_ver)

    @staticmethod
    def get_patch(version):
        if isinstance(version, int) or isinstance(version, float):
            return 0

        if isinstance(version, bytes):
            version = version.decode(Utilities.BASE_ENCODING)

        if isinstance(version, str):
            group = version.split('.')

            # handle case version = 'v15.123'
            if len(group) < 3:
                return 0

            patch_ver = group[2]

            return int(patch_ver)

    @staticmethod
    def check_version(version):
        '''
            left = v1, right = v10.9.0
                left = v0.1.2, right = 3.31
                left = 0, right = v0.4
                etc...
        '''
        try:
            assert (
                isinstance(version, str) or
                isinstance(version, bytes) or
                isinstance(version, int) or
                isinstance(version, float)
            )
            # TODO: handle versions:
            #  v13.saldalsd
            #  v2.42.32.2
        except AssertionError as error:
            raise error

    @staticmethod
    def check_before_comparison(other):
        assert (isinstance(other, CheckWrapper))

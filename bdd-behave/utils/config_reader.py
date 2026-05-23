import configparser


class ConfigReader:

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    @classmethod
    def get_base_url(cls):
        return cls.config.get("DEFAULT", "base_url")

    @classmethod
    def get_browser(cls):
        return cls.config.get("DEFAULT", "browser")

    @classmethod
    def get_timeout(cls):
        return cls.config.getint("DEFAULT", "timeout")

    @classmethod
    def get_implicit_wait(cls):
        return cls.config.getint("DEFAULT", "implicit_wait")

    @classmethod
    def get_headless(cls):
        return cls.config.getboolean("DEFAULT", "headless")
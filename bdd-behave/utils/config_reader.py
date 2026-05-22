import configparser


class ConfigReader:

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    @classmethod
    def get_browser(cls):
        return cls.config.get("DEFAULT", "browser")

    @classmethod
    def get_base_url(cls):
        return cls.config.get("DEFAULT", "base_url")

    @classmethod
    def get_timeout(cls):
        return cls.config.getint("DEFAULT", "timeout")

    @classmethod
    def get_product_url(cls):
        return cls.config.get("DEFAULT", "product_url")

    @classmethod
    def get_invalid_product(cls):
        return cls.config.get("DEFAULT", "invalid_product")

    @classmethod
    def get_search_product(cls):
        return cls.config.get("DEFAULT", "search_product")
import configparser
import os

from lib.common.utils import CustomDataStructure


class Config(CustomDataStructure):
    """
    配置文件解析工具.

    """

    _config_dir_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))),
        'config')

    def __init__(self, config_dir_path: str=None):
        parser = configparser.ConfigParser()
        parser.read(self._get_files(config_dir_path), 'utf-8')
        self._load(parser.items(), self)

    def _get_files(self, config_dir_path: str=None):
        """
        获取配置文件列表.

        :param config_dir_path:
        :return:
        """
        config_dir_path = config_dir_path if config_dir_path is not None else self._config_dir_path
        files = os.listdir(config_dir_path)

        config_files = []
        for file in files:
            if '.ini' == file[-4:]:
                config_files.append(os.path.join(config_dir_path, file))
        return config_files

    def _load(self, items: dict, instance: CustomDataStructure):
        """
        属性映射.

        :param items:
        :param instance:
        :return:
        """
        for key, ins in items:
            if not isinstance(ins, str):
                instance[key] = CustomDataStructure()
                self._load(ins.items(), instance[key])
            else:
                instance[key] = ins

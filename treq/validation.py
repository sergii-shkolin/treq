import yaml
from cerberus import Validator
from treq.exceptions import ConfigValidationExceptions

class ConfigValidation(object):
    def __init__(self):
        pass

    def parse_config(self, file):
        configs = None
        with open(file, 'r') as cfg:
            try:
                content = yaml.load(cfg, Loader=yaml.FullLoader)
                configs = content
            except yaml.YAMLError as exc:
                raise ConfigValidationExceptions(exc)
        return configs

    def data_validation(self, data={}):
        schema_config = '''
        requirements:
          type: dict
          schema:
            profile:
              type: string
            add:
              type: dict
              schema:
                buckets:
                    type: list
                dynamodb:
                    type: list
            remove:
              type: dict
              schema:
                buckets:
                    type: list
                dynamodb:
                    type: list
        '''

        schema_config_load = yaml.load(schema_config, Loader=yaml.FullLoader)
        content = data
        v = Validator(schema_config_load)
        status = v.validate(content)

        if not status:
            raise ConfigValidationExceptions("Invalid syntax: {0}".format(str((v.errors))))
        else:
            return status
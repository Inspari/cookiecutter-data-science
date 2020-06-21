"""This module provides configuration settings for the application."""

import sys
import os

from everett.component import RequiredConfigMixin, ConfigOptions
from everett.manager import ConfigManager, ConfigOSEnv, ConfigEnvFileEnv

# An example of configuration component for database access.
# For more information see: https://github.com/willkg/everett
class DbConfigComponent(RequiredConfigMixin):
    """A self-contained configuration component for database access."""

    OPTION_HOSTNAME = 'hostname'
    OPTION_DATABASE = 'database'
    OPTION_USERNAME = 'username'
    OPTION_PASSWORD = 'password'

    required_config = ConfigOptions()
    required_config.add_option(
        OPTION_HOSTNAME,
        parser=str,
        doc='The hostname of the database server.'
    )
    required_config.add_option(
        OPTION_DATABASE,
        parser=str,
        doc='The name of the database.'
    )
    required_config.add_option(
        OPTION_USERNAME,
        parser=str,
        doc='The username for accessing the database.'
    )
    required_config.add_option(
        OPTION_PASSWORD,
        parser=str,
        doc='The password for accessing the database.'
    )

    def __init__(self, config):
        # Bind the configuration to just the configuration this
        # component requires such that this component is
        # self-contained
        self.config = config.with_options(self)

        self.hostname = self.config(OPTION_HOSTNAME)
        self.database = self.config(OPTION_DATABASE)
        self.username = self.config(OPTION_USERNAME)
        self.password = self.config(OPTION_PASSWORD)


def get_db_config():
    manager = ConfigManager(
        environments=[
            ConfigEnvFileEnv(os.path.join('..', '.env')),
            ConfigOSEnv(),
        ],
        doc='Check the README.md file for configuration settings.'
    )

    # Apply the configuration class to the configuration manager
    # so that it handles option properties like defaults, parsers,
    # documentation, and so on.
    config = manager.with_namespace('db')
    return DbConfigComponent(config)

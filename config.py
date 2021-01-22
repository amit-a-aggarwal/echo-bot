#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "8da4d36c-81b7-42c6-8c3c-de53f26cce6a")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "AtLeastSixteenCharacters_0")

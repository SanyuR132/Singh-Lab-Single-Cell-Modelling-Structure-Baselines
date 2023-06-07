# ======================================================================== #
#
# Copyright (c) 2017 - 2020 scVAE authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ======================================================================== #

import json
import os

import importlib_resources as resources

# with resources.open_text("..Models.scvae", "defaults.json") as defaults_file:
#     defaults = json.load(defaults_file)

with open("defaults.json" if os.path.isfile("defaults.json") else "./scvae/defaults.json") as file:
    defaults = json.load(file)
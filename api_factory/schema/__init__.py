# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The ``schema`` module provides a normalized API representation.

In general, this module can be considered in three parts: wrappers,
metadata, and a roll-up view of an API as a whole.

These three parts are divided into the three component modules.
"""

from api_factory.schema.api import API
from api_factory.schema import metadata
from api_factory.schema import wrappers


__all__ = (
    'api',
    'metadata',
    'wrappers',
)
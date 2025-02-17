#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import sys

from ..config import Config
from .bernoulli import BernoulliObjectiveLikelihood
from .ordinal import OrdinalLikelihood

__all__ = [
    "BernoulliObjectiveLikelihood",
    "OrdinalLikelihood",
]

Config.register_module(sys.modules[__name__])

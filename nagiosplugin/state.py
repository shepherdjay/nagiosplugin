# -*- coding: utf-8 -*-
"""Classes  to represent check outcomes.

This module defines :class:`ServiceState` which is a NamedTuple class for check outcomes.

Note that the *warning* state is defined by the `Warn` variable. The
class has not been named `Warning` to avoid being confused with the
built-in Python exception of the same name.
"""

import collections
import functools


def worst(states):
    """Reduce list of *states* to the most significant state."""
    return functools.reduce(lambda a, b: a if a > b else b, states, Ok)


ServiceState = collections.namedtuple('ServiceState', ['code', 'text'])

Ok = ServiceState(0, 'ok')
Warn = ServiceState(1, 'warning')
Critical = ServiceState(2, 'critical')
Unknown = ServiceState(3, 'unknown')

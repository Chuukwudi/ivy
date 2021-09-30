import sys
import ivy
import jax
# noinspection PyPackageRequirements
import jaxlib
import jax.numpy as jnp
from jaxlib.xla_extension import Buffer

# make ivy.Container compatible with jax pytree traversal
from jax._src.lib import pytree
from jax.tree_util import register_pytree_node

register_pytree_node(
    ivy.Container,
    lambda c: pytree.flatten(c.to_dict()),
    lambda a, c: ivy.Container(pytree.unflatten(a, c))
)

# local
from .core import *
from . import nn
from .nn import *

# noinspection PyUnresolvedReferences
use = ivy.framework_handler.ContextManager(sys.modules[__name__])

# noinspection PyUnresolvedReferences,PyProtectedMember
NativeArray = (jax.interpreters.xla._DeviceArray, jaxlib.xla_extension.DeviceArray, Buffer)
# noinspection PyUnresolvedReferences,PyProtectedMember
NativeVariable = jax.interpreters.xla._DeviceArray
# noinspection PyUnresolvedReferences
Device = jaxlib.xla_extension.Device
Dtype = jnp.dtype

backend = 'jax'
from typing import Any
import warnings

warnings.simplefilter('ignore')

from faust.serializers import codecs
import msgpack


class raw_msgpack(codecs.Codec):
    def _dumps(self, obj: Any) -> bytes:
        return msgpack.packb(obj, use_bin_type=True)

    def _loads(self, s: bytes) -> Any:
        return msgpack.unpackb(s, raw=False)


def msgpack_codec() -> codecs.Codec:
    return raw_msgpack() | codecs.binary()


codecs.register('msgpack', msgpack_codec())

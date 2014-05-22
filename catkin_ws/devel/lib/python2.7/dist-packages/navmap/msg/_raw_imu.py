"""autogenerated by genpy from navmap/raw_imu.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class raw_imu(genpy.Message):
  _md5sum = "3507f0b63f5790cbc052576b2a56f94a"
  _type = "navmap/raw_imu"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int16 xacc
int16 yacc
int16 zacc
int16 xgyro
int16 ygyro
int16 zgyro
"""
  __slots__ = ['xacc','yacc','zacc','xgyro','ygyro','zgyro']
  _slot_types = ['int16','int16','int16','int16','int16','int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       xacc,yacc,zacc,xgyro,ygyro,zgyro

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(raw_imu, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.xacc is None:
        self.xacc = 0
      if self.yacc is None:
        self.yacc = 0
      if self.zacc is None:
        self.zacc = 0
      if self.xgyro is None:
        self.xgyro = 0
      if self.ygyro is None:
        self.ygyro = 0
      if self.zgyro is None:
        self.zgyro = 0
    else:
      self.xacc = 0
      self.yacc = 0
      self.zacc = 0
      self.xgyro = 0
      self.ygyro = 0
      self.zgyro = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_6h.pack(_x.xacc, _x.yacc, _x.zacc, _x.xgyro, _x.ygyro, _x.zgyro))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.xacc, _x.yacc, _x.zacc, _x.xgyro, _x.ygyro, _x.zgyro,) = _struct_6h.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_6h.pack(_x.xacc, _x.yacc, _x.zacc, _x.xgyro, _x.ygyro, _x.zgyro))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.xacc, _x.yacc, _x.zacc, _x.xgyro, _x.ygyro, _x.zgyro,) = _struct_6h.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6h = struct.Struct("<6h")
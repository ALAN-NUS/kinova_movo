# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from movo_arc_lib/upper_jp_movo_safeFeedback.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class upper_jp_movo_safeFeedback(genpy.Message):
  _md5sum = "24b93ade2ee0e857b2b0ba66e04f653d"
  _type = "movo_arc_lib/upper_jp_movo_safeFeedback"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#feedback
float32[7] jp_right
float32[7] jp_left
float32 jp_linear
float32[2] jp_head
float32 duration
float32[6] r_current_force
float32[6] l_current_force
"""
  __slots__ = ['jp_right','jp_left','jp_linear','jp_head','duration','r_current_force','l_current_force']
  _slot_types = ['float32[7]','float32[7]','float32','float32[2]','float32','float32[6]','float32[6]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       jp_right,jp_left,jp_linear,jp_head,duration,r_current_force,l_current_force

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(upper_jp_movo_safeFeedback, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.jp_right is None:
        self.jp_right = [0.] * 7
      if self.jp_left is None:
        self.jp_left = [0.] * 7
      if self.jp_linear is None:
        self.jp_linear = 0.
      if self.jp_head is None:
        self.jp_head = [0.] * 2
      if self.duration is None:
        self.duration = 0.
      if self.r_current_force is None:
        self.r_current_force = [0.] * 6
      if self.l_current_force is None:
        self.l_current_force = [0.] * 6
    else:
      self.jp_right = [0.] * 7
      self.jp_left = [0.] * 7
      self.jp_linear = 0.
      self.jp_head = [0.] * 2
      self.duration = 0.
      self.r_current_force = [0.] * 6
      self.l_current_force = [0.] * 6

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
      buff.write(_get_struct_7f().pack(*self.jp_right))
      buff.write(_get_struct_7f().pack(*self.jp_left))
      _x = self.jp_linear
      buff.write(_get_struct_f().pack(_x))
      buff.write(_get_struct_2f().pack(*self.jp_head))
      _x = self.duration
      buff.write(_get_struct_f().pack(_x))
      buff.write(_get_struct_6f().pack(*self.r_current_force))
      buff.write(_get_struct_6f().pack(*self.l_current_force))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 28
      self.jp_right = _get_struct_7f().unpack(str[start:end])
      start = end
      end += 28
      self.jp_left = _get_struct_7f().unpack(str[start:end])
      start = end
      end += 4
      (self.jp_linear,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 8
      self.jp_head = _get_struct_2f().unpack(str[start:end])
      start = end
      end += 4
      (self.duration,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 24
      self.r_current_force = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 24
      self.l_current_force = _get_struct_6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(self.jp_right.tostring())
      buff.write(self.jp_left.tostring())
      _x = self.jp_linear
      buff.write(_get_struct_f().pack(_x))
      buff.write(self.jp_head.tostring())
      _x = self.duration
      buff.write(_get_struct_f().pack(_x))
      buff.write(self.r_current_force.tostring())
      buff.write(self.l_current_force.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 28
      self.jp_right = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=7)
      start = end
      end += 28
      self.jp_left = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=7)
      start = end
      end += 4
      (self.jp_linear,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 8
      self.jp_head = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      start = end
      end += 4
      (self.duration,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 24
      self.r_current_force = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=6)
      start = end
      end += 24
      self.l_current_force = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=6)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_6f = None
def _get_struct_6f():
    global _struct_6f
    if _struct_6f is None:
        _struct_6f = struct.Struct("<6f")
    return _struct_6f
_struct_7f = None
def _get_struct_7f():
    global _struct_7f
    if _struct_7f is None:
        _struct_7f = struct.Struct("<7f")
    return _struct_7f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
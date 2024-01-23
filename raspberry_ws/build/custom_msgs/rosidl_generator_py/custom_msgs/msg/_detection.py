# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_msgs:msg/Detection.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Detection(type):
    """Metaclass of message 'Detection'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('custom_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_msgs.msg.Detection')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__detection
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__detection
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__detection
            cls._TYPE_SUPPORT = module.type_support_msg__msg__detection
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__detection

            from std_msgs.msg import Float32
            if Float32.__class__._TYPE_SUPPORT is None:
                Float32.__class__.__import_type_support__()

            from std_msgs.msg import String
            if String.__class__._TYPE_SUPPORT is None:
                String.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Detection(metaclass=Metaclass_Detection):
    """Message class 'Detection'."""

    __slots__ = [
        '_name',
        '_id',
        '_location_x',
        '_location_y',
        '_screen_size_x',
        '_screen_size_y',
        '_confidence',
    ]

    _fields_and_field_types = {
        'name': 'std_msgs/String',
        'id': 'std_msgs/String',
        'location_x': 'std_msgs/Float32',
        'location_y': 'std_msgs/Float32',
        'screen_size_x': 'std_msgs/Float32',
        'screen_size_y': 'std_msgs/Float32',
        'confidence': 'std_msgs/Float32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'String'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'String'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import String
        self.name = kwargs.get('name', String())
        from std_msgs.msg import String
        self.id = kwargs.get('id', String())
        from std_msgs.msg import Float32
        self.location_x = kwargs.get('location_x', Float32())
        from std_msgs.msg import Float32
        self.location_y = kwargs.get('location_y', Float32())
        from std_msgs.msg import Float32
        self.screen_size_x = kwargs.get('screen_size_x', Float32())
        from std_msgs.msg import Float32
        self.screen_size_y = kwargs.get('screen_size_y', Float32())
        from std_msgs.msg import Float32
        self.confidence = kwargs.get('confidence', Float32())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.name != other.name:
            return False
        if self.id != other.id:
            return False
        if self.location_x != other.location_x:
            return False
        if self.location_y != other.location_y:
            return False
        if self.screen_size_x != other.screen_size_x:
            return False
        if self.screen_size_y != other.screen_size_y:
            return False
        if self.confidence != other.confidence:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def name(self):
        """Message field 'name'."""
        return self._name

    @name.setter
    def name(self, value):
        if __debug__:
            from std_msgs.msg import String
            assert \
                isinstance(value, String), \
                "The 'name' field must be a sub message of type 'String'"
        self._name = value

    @property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if __debug__:
            from std_msgs.msg import String
            assert \
                isinstance(value, String), \
                "The 'id' field must be a sub message of type 'String'"
        self._id = value

    @property
    def location_x(self):
        """Message field 'location_x'."""
        return self._location_x

    @location_x.setter
    def location_x(self, value):
        if __debug__:
            from std_msgs.msg import Float32
            assert \
                isinstance(value, Float32), \
                "The 'location_x' field must be a sub message of type 'Float32'"
        self._location_x = value

    @property
    def location_y(self):
        """Message field 'location_y'."""
        return self._location_y

    @location_y.setter
    def location_y(self, value):
        if __debug__:
            from std_msgs.msg import Float32
            assert \
                isinstance(value, Float32), \
                "The 'location_y' field must be a sub message of type 'Float32'"
        self._location_y = value

    @property
    def screen_size_x(self):
        """Message field 'screen_size_x'."""
        return self._screen_size_x

    @screen_size_x.setter
    def screen_size_x(self, value):
        if __debug__:
            from std_msgs.msg import Float32
            assert \
                isinstance(value, Float32), \
                "The 'screen_size_x' field must be a sub message of type 'Float32'"
        self._screen_size_x = value

    @property
    def screen_size_y(self):
        """Message field 'screen_size_y'."""
        return self._screen_size_y

    @screen_size_y.setter
    def screen_size_y(self, value):
        if __debug__:
            from std_msgs.msg import Float32
            assert \
                isinstance(value, Float32), \
                "The 'screen_size_y' field must be a sub message of type 'Float32'"
        self._screen_size_y = value

    @property
    def confidence(self):
        """Message field 'confidence'."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if __debug__:
            from std_msgs.msg import Float32
            assert \
                isinstance(value, Float32), \
                "The 'confidence' field must be a sub message of type 'Float32'"
        self._confidence = value

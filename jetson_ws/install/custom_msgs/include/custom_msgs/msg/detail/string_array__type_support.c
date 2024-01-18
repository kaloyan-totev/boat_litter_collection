// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from custom_msgs:msg/StringArray.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "custom_msgs/msg/detail/string_array__rosidl_typesupport_introspection_c.h"
#include "custom_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "custom_msgs/msg/detail/string_array__functions.h"
#include "custom_msgs/msg/detail/string_array__struct.h"


// Include directives for member types
// Member `detections`
#include "custom_msgs/msg/detections.h"
// Member `detections`
#include "custom_msgs/msg/detail/detections__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void StringArray__rosidl_typesupport_introspection_c__StringArray_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  custom_msgs__msg__StringArray__init(message_memory);
}

void StringArray__rosidl_typesupport_introspection_c__StringArray_fini_function(void * message_memory)
{
  custom_msgs__msg__StringArray__fini(message_memory);
}

size_t StringArray__rosidl_typesupport_introspection_c__size_function__Detections__detections(
  const void * untyped_member)
{
  const custom_msgs__msg__Detections__Sequence * member =
    (const custom_msgs__msg__Detections__Sequence *)(untyped_member);
  return member->size;
}

const void * StringArray__rosidl_typesupport_introspection_c__get_const_function__Detections__detections(
  const void * untyped_member, size_t index)
{
  const custom_msgs__msg__Detections__Sequence * member =
    (const custom_msgs__msg__Detections__Sequence *)(untyped_member);
  return &member->data[index];
}

void * StringArray__rosidl_typesupport_introspection_c__get_function__Detections__detections(
  void * untyped_member, size_t index)
{
  custom_msgs__msg__Detections__Sequence * member =
    (custom_msgs__msg__Detections__Sequence *)(untyped_member);
  return &member->data[index];
}

bool StringArray__rosidl_typesupport_introspection_c__resize_function__Detections__detections(
  void * untyped_member, size_t size)
{
  custom_msgs__msg__Detections__Sequence * member =
    (custom_msgs__msg__Detections__Sequence *)(untyped_member);
  custom_msgs__msg__Detections__Sequence__fini(member);
  return custom_msgs__msg__Detections__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember StringArray__rosidl_typesupport_introspection_c__StringArray_message_member_array[1] = {
  {
    "detections",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_msgs__msg__StringArray, detections),  // bytes offset in struct
    NULL,  // default value
    StringArray__rosidl_typesupport_introspection_c__size_function__Detections__detections,  // size() function pointer
    StringArray__rosidl_typesupport_introspection_c__get_const_function__Detections__detections,  // get_const(index) function pointer
    StringArray__rosidl_typesupport_introspection_c__get_function__Detections__detections,  // get(index) function pointer
    StringArray__rosidl_typesupport_introspection_c__resize_function__Detections__detections  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers StringArray__rosidl_typesupport_introspection_c__StringArray_message_members = {
  "custom_msgs__msg",  // message namespace
  "StringArray",  // message name
  1,  // number of fields
  sizeof(custom_msgs__msg__StringArray),
  StringArray__rosidl_typesupport_introspection_c__StringArray_message_member_array,  // message members
  StringArray__rosidl_typesupport_introspection_c__StringArray_init_function,  // function to initialize message memory (memory has to be allocated)
  StringArray__rosidl_typesupport_introspection_c__StringArray_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t StringArray__rosidl_typesupport_introspection_c__StringArray_message_type_support_handle = {
  0,
  &StringArray__rosidl_typesupport_introspection_c__StringArray_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_custom_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_msgs, msg, StringArray)() {
  StringArray__rosidl_typesupport_introspection_c__StringArray_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_msgs, msg, Detections)();
  if (!StringArray__rosidl_typesupport_introspection_c__StringArray_message_type_support_handle.typesupport_identifier) {
    StringArray__rosidl_typesupport_introspection_c__StringArray_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &StringArray__rosidl_typesupport_introspection_c__StringArray_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

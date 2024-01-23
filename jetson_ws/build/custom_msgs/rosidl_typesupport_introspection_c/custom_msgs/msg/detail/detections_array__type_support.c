// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from custom_msgs:msg/DetectionsArray.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "custom_msgs/msg/detail/detections_array__rosidl_typesupport_introspection_c.h"
#include "custom_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "custom_msgs/msg/detail/detections_array__functions.h"
#include "custom_msgs/msg/detail/detections_array__struct.h"


// Include directives for member types
// Member `detections`
#include "custom_msgs/msg/detection.h"
// Member `detections`
#include "custom_msgs/msg/detail/detection__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  custom_msgs__msg__DetectionsArray__init(message_memory);
}

void DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_fini_function(void * message_memory)
{
  custom_msgs__msg__DetectionsArray__fini(message_memory);
}

size_t DetectionsArray__rosidl_typesupport_introspection_c__size_function__Detection__detections(
  const void * untyped_member)
{
  const custom_msgs__msg__Detection__Sequence * member =
    (const custom_msgs__msg__Detection__Sequence *)(untyped_member);
  return member->size;
}

const void * DetectionsArray__rosidl_typesupport_introspection_c__get_const_function__Detection__detections(
  const void * untyped_member, size_t index)
{
  const custom_msgs__msg__Detection__Sequence * member =
    (const custom_msgs__msg__Detection__Sequence *)(untyped_member);
  return &member->data[index];
}

void * DetectionsArray__rosidl_typesupport_introspection_c__get_function__Detection__detections(
  void * untyped_member, size_t index)
{
  custom_msgs__msg__Detection__Sequence * member =
    (custom_msgs__msg__Detection__Sequence *)(untyped_member);
  return &member->data[index];
}

bool DetectionsArray__rosidl_typesupport_introspection_c__resize_function__Detection__detections(
  void * untyped_member, size_t size)
{
  custom_msgs__msg__Detection__Sequence * member =
    (custom_msgs__msg__Detection__Sequence *)(untyped_member);
  custom_msgs__msg__Detection__Sequence__fini(member);
  return custom_msgs__msg__Detection__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_member_array[1] = {
  {
    "detections",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_msgs__msg__DetectionsArray, detections),  // bytes offset in struct
    NULL,  // default value
    DetectionsArray__rosidl_typesupport_introspection_c__size_function__Detection__detections,  // size() function pointer
    DetectionsArray__rosidl_typesupport_introspection_c__get_const_function__Detection__detections,  // get_const(index) function pointer
    DetectionsArray__rosidl_typesupport_introspection_c__get_function__Detection__detections,  // get(index) function pointer
    DetectionsArray__rosidl_typesupport_introspection_c__resize_function__Detection__detections  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_members = {
  "custom_msgs__msg",  // message namespace
  "DetectionsArray",  // message name
  1,  // number of fields
  sizeof(custom_msgs__msg__DetectionsArray),
  DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_member_array,  // message members
  DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_init_function,  // function to initialize message memory (memory has to be allocated)
  DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_type_support_handle = {
  0,
  &DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_custom_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_msgs, msg, DetectionsArray)() {
  DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_msgs, msg, Detection)();
  if (!DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_type_support_handle.typesupport_identifier) {
    DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &DetectionsArray__rosidl_typesupport_introspection_c__DetectionsArray_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

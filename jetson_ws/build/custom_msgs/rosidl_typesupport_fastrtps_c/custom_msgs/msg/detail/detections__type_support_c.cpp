// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from custom_msgs:msg/Detections.idl
// generated code does not contain a copyright notice
#include "custom_msgs/msg/detail/detections__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "custom_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "custom_msgs/msg/detail/detections__struct.h"
#include "custom_msgs/msg/detail/detections__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "std_msgs/msg/detail/string__functions.h"  // id, location_x, location_y, name, screen_size_x, screen_size_y

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_custom_msgs
size_t get_serialized_size_std_msgs__msg__String(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_custom_msgs
size_t max_serialized_size_std_msgs__msg__String(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_custom_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, String)();


using _Detections__ros_msg_type = custom_msgs__msg__Detections;

static bool _Detections__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Detections__ros_msg_type * ros_message = static_cast<const _Detections__ros_msg_type *>(untyped_ros_message);
  // Field name: name
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->name, cdr))
    {
      return false;
    }
  }

  // Field name: id
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->id, cdr))
    {
      return false;
    }
  }

  // Field name: location_x
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->location_x, cdr))
    {
      return false;
    }
  }

  // Field name: location_y
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->location_y, cdr))
    {
      return false;
    }
  }

  // Field name: screen_size_x
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->screen_size_x, cdr))
    {
      return false;
    }
  }

  // Field name: screen_size_y
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->screen_size_y, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _Detections__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Detections__ros_msg_type * ros_message = static_cast<_Detections__ros_msg_type *>(untyped_ros_message);
  // Field name: name
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->name))
    {
      return false;
    }
  }

  // Field name: id
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->id))
    {
      return false;
    }
  }

  // Field name: location_x
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->location_x))
    {
      return false;
    }
  }

  // Field name: location_y
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->location_y))
    {
      return false;
    }
  }

  // Field name: screen_size_x
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->screen_size_x))
    {
      return false;
    }
  }

  // Field name: screen_size_y
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->screen_size_y))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_msgs
size_t get_serialized_size_custom_msgs__msg__Detections(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Detections__ros_msg_type * ros_message = static_cast<const _Detections__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name name

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->name), current_alignment);
  // field.name id

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->id), current_alignment);
  // field.name location_x

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->location_x), current_alignment);
  // field.name location_y

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->location_y), current_alignment);
  // field.name screen_size_x

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->screen_size_x), current_alignment);
  // field.name screen_size_y

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->screen_size_y), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _Detections__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_custom_msgs__msg__Detections(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_msgs
size_t max_serialized_size_custom_msgs__msg__Detections(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: name
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        full_bounded, current_alignment);
    }
  }
  // member: id
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        full_bounded, current_alignment);
    }
  }
  // member: location_x
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        full_bounded, current_alignment);
    }
  }
  // member: location_y
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        full_bounded, current_alignment);
    }
  }
  // member: screen_size_x
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        full_bounded, current_alignment);
    }
  }
  // member: screen_size_y
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _Detections__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_custom_msgs__msg__Detections(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Detections = {
  "custom_msgs::msg",
  "Detections",
  _Detections__cdr_serialize,
  _Detections__cdr_deserialize,
  _Detections__get_serialized_size,
  _Detections__max_serialized_size
};

static rosidl_message_type_support_t _Detections__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Detections,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, custom_msgs, msg, Detections)() {
  return &_Detections__type_support;
}

#if defined(__cplusplus)
}
#endif
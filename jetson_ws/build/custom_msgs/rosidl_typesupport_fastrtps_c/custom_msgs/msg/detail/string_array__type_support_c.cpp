// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from custom_msgs:msg/StringArray.idl
// generated code does not contain a copyright notice
#include "custom_msgs/msg/detail/string_array__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "custom_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "custom_msgs/msg/detail/string_array__struct.h"
#include "custom_msgs/msg/detail/string_array__functions.h"
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

#include "custom_msgs/msg/detail/detections__functions.h"  // detections

// forward declare type support functions
size_t get_serialized_size_custom_msgs__msg__Detections(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_custom_msgs__msg__Detections(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, custom_msgs, msg, Detections)();


using _StringArray__ros_msg_type = custom_msgs__msg__StringArray;

static bool _StringArray__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _StringArray__ros_msg_type * ros_message = static_cast<const _StringArray__ros_msg_type *>(untyped_ros_message);
  // Field name: detections
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, custom_msgs, msg, Detections
      )()->data);
    size_t size = ros_message->detections.size;
    auto array_ptr = ros_message->detections.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  return true;
}

static bool _StringArray__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _StringArray__ros_msg_type * ros_message = static_cast<_StringArray__ros_msg_type *>(untyped_ros_message);
  // Field name: detections
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, custom_msgs, msg, Detections
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->detections.data) {
      custom_msgs__msg__Detections__Sequence__fini(&ros_message->detections);
    }
    if (!custom_msgs__msg__Detections__Sequence__init(&ros_message->detections, size)) {
      return "failed to create array for field 'detections'";
    }
    auto array_ptr = ros_message->detections.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_msgs
size_t get_serialized_size_custom_msgs__msg__StringArray(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _StringArray__ros_msg_type * ros_message = static_cast<const _StringArray__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name detections
  {
    size_t array_size = ros_message->detections.size;
    auto array_ptr = ros_message->detections.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_custom_msgs__msg__Detections(
        &array_ptr[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static uint32_t _StringArray__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_custom_msgs__msg__StringArray(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_msgs
size_t max_serialized_size_custom_msgs__msg__StringArray(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: detections
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_custom_msgs__msg__Detections(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _StringArray__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_custom_msgs__msg__StringArray(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_StringArray = {
  "custom_msgs::msg",
  "StringArray",
  _StringArray__cdr_serialize,
  _StringArray__cdr_deserialize,
  _StringArray__get_serialized_size,
  _StringArray__max_serialized_size
};

static rosidl_message_type_support_t _StringArray__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_StringArray,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, custom_msgs, msg, StringArray)() {
  return &_StringArray__type_support;
}

#if defined(__cplusplus)
}
#endif
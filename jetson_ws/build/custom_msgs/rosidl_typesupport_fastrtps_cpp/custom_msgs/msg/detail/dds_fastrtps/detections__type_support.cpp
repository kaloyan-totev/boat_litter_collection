// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from custom_msgs:msg/Detections.idl
// generated code does not contain a copyright notice
#include "custom_msgs/msg/detail/detections__rosidl_typesupport_fastrtps_cpp.hpp"
#include "custom_msgs/msg/detail/detections__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::String &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::String &);
size_t get_serialized_size(
  const std_msgs::msg::String &,
  size_t current_alignment);
size_t
max_serialized_size_String(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs

namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::String &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::String &);
size_t get_serialized_size(
  const std_msgs::msg::String &,
  size_t current_alignment);
size_t
max_serialized_size_String(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs

namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::String &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::String &);
size_t get_serialized_size(
  const std_msgs::msg::String &,
  size_t current_alignment);
size_t
max_serialized_size_String(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs

namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::String &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::String &);
size_t get_serialized_size(
  const std_msgs::msg::String &,
  size_t current_alignment);
size_t
max_serialized_size_String(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs

namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::String &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::String &);
size_t get_serialized_size(
  const std_msgs::msg::String &,
  size_t current_alignment);
size_t
max_serialized_size_String(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs

namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::String &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::String &);
size_t get_serialized_size(
  const std_msgs::msg::String &,
  size_t current_alignment);
size_t
max_serialized_size_String(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs


namespace custom_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_msgs
cdr_serialize(
  const custom_msgs::msg::Detections & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: name
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.name,
    cdr);
  // Member: id
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.id,
    cdr);
  // Member: location_x
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.location_x,
    cdr);
  // Member: location_y
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.location_y,
    cdr);
  // Member: screen_size_x
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.screen_size_x,
    cdr);
  // Member: screen_size_y
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.screen_size_y,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  custom_msgs::msg::Detections & ros_message)
{
  // Member: name
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.name);

  // Member: id
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.id);

  // Member: location_x
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.location_x);

  // Member: location_y
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.location_y);

  // Member: screen_size_x
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.screen_size_x);

  // Member: screen_size_y
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.screen_size_y);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_msgs
get_serialized_size(
  const custom_msgs::msg::Detections & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: name

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.name, current_alignment);
  // Member: id

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.id, current_alignment);
  // Member: location_x

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.location_x, current_alignment);
  // Member: location_y

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.location_y, current_alignment);
  // Member: screen_size_x

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.screen_size_x, current_alignment);
  // Member: screen_size_y

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.screen_size_y, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_custom_msgs
max_serialized_size_Detections(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: name
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_String(
        full_bounded, current_alignment);
    }
  }

  // Member: id
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_String(
        full_bounded, current_alignment);
    }
  }

  // Member: location_x
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_String(
        full_bounded, current_alignment);
    }
  }

  // Member: location_y
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_String(
        full_bounded, current_alignment);
    }
  }

  // Member: screen_size_x
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_String(
        full_bounded, current_alignment);
    }
  }

  // Member: screen_size_y
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_String(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static bool _Detections__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const custom_msgs::msg::Detections *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Detections__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<custom_msgs::msg::Detections *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Detections__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const custom_msgs::msg::Detections *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Detections__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_Detections(full_bounded, 0);
}

static message_type_support_callbacks_t _Detections__callbacks = {
  "custom_msgs::msg",
  "Detections",
  _Detections__cdr_serialize,
  _Detections__cdr_deserialize,
  _Detections__get_serialized_size,
  _Detections__max_serialized_size
};

static rosidl_message_type_support_t _Detections__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Detections__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace custom_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_custom_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<custom_msgs::msg::Detections>()
{
  return &custom_msgs::msg::typesupport_fastrtps_cpp::_Detections__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, custom_msgs, msg, Detections)() {
  return &custom_msgs::msg::typesupport_fastrtps_cpp::_Detections__handle;
}

#ifdef __cplusplus
}
#endif

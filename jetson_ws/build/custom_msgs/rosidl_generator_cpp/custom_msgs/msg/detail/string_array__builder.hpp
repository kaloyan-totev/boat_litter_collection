// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msgs:msg/StringArray.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__STRING_ARRAY__BUILDER_HPP_
#define CUSTOM_MSGS__MSG__DETAIL__STRING_ARRAY__BUILDER_HPP_

#include "custom_msgs/msg/detail/string_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msgs
{

namespace msg
{

namespace builder
{

class Init_StringArray_detections
{
public:
  Init_StringArray_detections()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_msgs::msg::StringArray detections(::custom_msgs::msg::StringArray::_detections_type arg)
  {
    msg_.detections = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msgs::msg::StringArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msgs::msg::StringArray>()
{
  return custom_msgs::msg::builder::Init_StringArray_detections();
}

}  // namespace custom_msgs

#endif  // CUSTOM_MSGS__MSG__DETAIL__STRING_ARRAY__BUILDER_HPP_

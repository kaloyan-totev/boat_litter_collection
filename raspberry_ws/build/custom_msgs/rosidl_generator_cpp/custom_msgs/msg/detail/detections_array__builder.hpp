// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msgs:msg/DetectionsArray.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__DETECTIONS_ARRAY__BUILDER_HPP_
#define CUSTOM_MSGS__MSG__DETAIL__DETECTIONS_ARRAY__BUILDER_HPP_

#include "custom_msgs/msg/detail/detections_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msgs
{

namespace msg
{

namespace builder
{

class Init_DetectionsArray_detections
{
public:
  Init_DetectionsArray_detections()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_msgs::msg::DetectionsArray detections(::custom_msgs::msg::DetectionsArray::_detections_type arg)
  {
    msg_.detections = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msgs::msg::DetectionsArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msgs::msg::DetectionsArray>()
{
  return custom_msgs::msg::builder::Init_DetectionsArray_detections();
}

}  // namespace custom_msgs

#endif  // CUSTOM_MSGS__MSG__DETAIL__DETECTIONS_ARRAY__BUILDER_HPP_

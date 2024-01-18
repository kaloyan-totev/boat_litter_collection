// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msgs:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__BUILDER_HPP_
#define CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__BUILDER_HPP_

#include "custom_msgs/msg/detail/detections__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msgs
{

namespace msg
{

namespace builder
{

class Init_Detections_screen_size_y
{
public:
  explicit Init_Detections_screen_size_y(::custom_msgs::msg::Detections & msg)
  : msg_(msg)
  {}
  ::custom_msgs::msg::Detections screen_size_y(::custom_msgs::msg::Detections::_screen_size_y_type arg)
  {
    msg_.screen_size_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msgs::msg::Detections msg_;
};

class Init_Detections_screen_size_x
{
public:
  explicit Init_Detections_screen_size_x(::custom_msgs::msg::Detections & msg)
  : msg_(msg)
  {}
  Init_Detections_screen_size_y screen_size_x(::custom_msgs::msg::Detections::_screen_size_x_type arg)
  {
    msg_.screen_size_x = std::move(arg);
    return Init_Detections_screen_size_y(msg_);
  }

private:
  ::custom_msgs::msg::Detections msg_;
};

class Init_Detections_location_y
{
public:
  explicit Init_Detections_location_y(::custom_msgs::msg::Detections & msg)
  : msg_(msg)
  {}
  Init_Detections_screen_size_x location_y(::custom_msgs::msg::Detections::_location_y_type arg)
  {
    msg_.location_y = std::move(arg);
    return Init_Detections_screen_size_x(msg_);
  }

private:
  ::custom_msgs::msg::Detections msg_;
};

class Init_Detections_location_x
{
public:
  explicit Init_Detections_location_x(::custom_msgs::msg::Detections & msg)
  : msg_(msg)
  {}
  Init_Detections_location_y location_x(::custom_msgs::msg::Detections::_location_x_type arg)
  {
    msg_.location_x = std::move(arg);
    return Init_Detections_location_y(msg_);
  }

private:
  ::custom_msgs::msg::Detections msg_;
};

class Init_Detections_id
{
public:
  explicit Init_Detections_id(::custom_msgs::msg::Detections & msg)
  : msg_(msg)
  {}
  Init_Detections_location_x id(::custom_msgs::msg::Detections::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Detections_location_x(msg_);
  }

private:
  ::custom_msgs::msg::Detections msg_;
};

class Init_Detections_name
{
public:
  Init_Detections_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Detections_id name(::custom_msgs::msg::Detections::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_Detections_id(msg_);
  }

private:
  ::custom_msgs::msg::Detections msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msgs::msg::Detections>()
{
  return custom_msgs::msg::builder::Init_Detections_name();
}

}  // namespace custom_msgs

#endif  // CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__BUILDER_HPP_

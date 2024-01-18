// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_msgs:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__TRAITS_HPP_
#define CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__TRAITS_HPP_

#include "custom_msgs/msg/detail/detections__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'name'
// Member 'id'
// Member 'location_x'
// Member 'location_y'
// Member 'screen_size_x'
// Member 'screen_size_y'
#include "std_msgs/msg/detail/string__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_msgs::msg::Detections>()
{
  return "custom_msgs::msg::Detections";
}

template<>
inline const char * name<custom_msgs::msg::Detections>()
{
  return "custom_msgs/msg/Detections";
}

template<>
struct has_fixed_size<custom_msgs::msg::Detections>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::String>::value> {};

template<>
struct has_bounded_size<custom_msgs::msg::Detections>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::String>::value> {};

template<>
struct is_message<custom_msgs::msg::Detections>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__TRAITS_HPP_

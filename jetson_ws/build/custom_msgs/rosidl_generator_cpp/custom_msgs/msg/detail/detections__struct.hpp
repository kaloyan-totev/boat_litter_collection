// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_msgs:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_HPP_
#define CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'name'
// Member 'id'
// Member 'location_x'
// Member 'location_y'
// Member 'screen_size_x'
// Member 'screen_size_y'
#include "std_msgs/msg/detail/string__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__custom_msgs__msg__Detections __attribute__((deprecated))
#else
# define DEPRECATED__custom_msgs__msg__Detections __declspec(deprecated)
#endif

namespace custom_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Detections_
{
  using Type = Detections_<ContainerAllocator>;

  explicit Detections_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : name(_init),
    id(_init),
    location_x(_init),
    location_y(_init),
    screen_size_x(_init),
    screen_size_y(_init)
  {
    (void)_init;
  }

  explicit Detections_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : name(_alloc, _init),
    id(_alloc, _init),
    location_x(_alloc, _init),
    location_y(_alloc, _init),
    screen_size_x(_alloc, _init),
    screen_size_y(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _name_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _name_type name;
  using _id_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _id_type id;
  using _location_x_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _location_x_type location_x;
  using _location_y_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _location_y_type location_y;
  using _screen_size_x_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _screen_size_x_type screen_size_x;
  using _screen_size_y_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _screen_size_y_type screen_size_y;

  // setters for named parameter idiom
  Type & set__name(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->name = _arg;
    return *this;
  }
  Type & set__id(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__location_x(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->location_x = _arg;
    return *this;
  }
  Type & set__location_y(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->location_y = _arg;
    return *this;
  }
  Type & set__screen_size_x(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->screen_size_x = _arg;
    return *this;
  }
  Type & set__screen_size_y(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->screen_size_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_msgs::msg::Detections_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_msgs::msg::Detections_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_msgs::msg::Detections_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_msgs::msg::Detections_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_msgs::msg::Detections_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_msgs::msg::Detections_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_msgs::msg::Detections_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_msgs::msg::Detections_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_msgs::msg::Detections_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_msgs::msg::Detections_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_msgs__msg__Detections
    std::shared_ptr<custom_msgs::msg::Detections_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_msgs__msg__Detections
    std::shared_ptr<custom_msgs::msg::Detections_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Detections_ & other) const
  {
    if (this->name != other.name) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    if (this->location_x != other.location_x) {
      return false;
    }
    if (this->location_y != other.location_y) {
      return false;
    }
    if (this->screen_size_x != other.screen_size_x) {
      return false;
    }
    if (this->screen_size_y != other.screen_size_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const Detections_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Detections_

// alias to use template instance with default allocator
using Detections =
  custom_msgs::msg::Detections_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_msgs

#endif  // CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_HPP_

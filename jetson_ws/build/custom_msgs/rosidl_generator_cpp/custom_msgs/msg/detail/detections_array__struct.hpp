// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_msgs:msg/DetectionsArray.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__DETECTIONS_ARRAY__STRUCT_HPP_
#define CUSTOM_MSGS__MSG__DETAIL__DETECTIONS_ARRAY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'detections'
#include "custom_msgs/msg/detail/detection__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__custom_msgs__msg__DetectionsArray __attribute__((deprecated))
#else
# define DEPRECATED__custom_msgs__msg__DetectionsArray __declspec(deprecated)
#endif

namespace custom_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DetectionsArray_
{
  using Type = DetectionsArray_<ContainerAllocator>;

  explicit DetectionsArray_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit DetectionsArray_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _detections_type =
    std::vector<custom_msgs::msg::Detection_<ContainerAllocator>, typename ContainerAllocator::template rebind<custom_msgs::msg::Detection_<ContainerAllocator>>::other>;
  _detections_type detections;

  // setters for named parameter idiom
  Type & set__detections(
    const std::vector<custom_msgs::msg::Detection_<ContainerAllocator>, typename ContainerAllocator::template rebind<custom_msgs::msg::Detection_<ContainerAllocator>>::other> & _arg)
  {
    this->detections = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_msgs::msg::DetectionsArray_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_msgs::msg::DetectionsArray_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_msgs::msg::DetectionsArray_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_msgs::msg::DetectionsArray_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_msgs__msg__DetectionsArray
    std::shared_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_msgs__msg__DetectionsArray
    std::shared_ptr<custom_msgs::msg::DetectionsArray_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DetectionsArray_ & other) const
  {
    if (this->detections != other.detections) {
      return false;
    }
    return true;
  }
  bool operator!=(const DetectionsArray_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DetectionsArray_

// alias to use template instance with default allocator
using DetectionsArray =
  custom_msgs::msg::DetectionsArray_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_msgs

#endif  // CUSTOM_MSGS__MSG__DETAIL__DETECTIONS_ARRAY__STRUCT_HPP_

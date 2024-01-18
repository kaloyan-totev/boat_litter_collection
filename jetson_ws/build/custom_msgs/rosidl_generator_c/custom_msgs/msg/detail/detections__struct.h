// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_msgs:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_H_
#define CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
// Member 'id'
// Member 'location_x'
// Member 'location_y'
// Member 'screen_size_x'
// Member 'screen_size_y'
#include "std_msgs/msg/detail/string__struct.h"

// Struct defined in msg/Detections in the package custom_msgs.
typedef struct custom_msgs__msg__Detections
{
  std_msgs__msg__String name;
  std_msgs__msg__String id;
  std_msgs__msg__String location_x;
  std_msgs__msg__String location_y;
  std_msgs__msg__String screen_size_x;
  std_msgs__msg__String screen_size_y;
} custom_msgs__msg__Detections;

// Struct for a sequence of custom_msgs__msg__Detections.
typedef struct custom_msgs__msg__Detections__Sequence
{
  custom_msgs__msg__Detections * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_msgs__msg__Detections__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_H_

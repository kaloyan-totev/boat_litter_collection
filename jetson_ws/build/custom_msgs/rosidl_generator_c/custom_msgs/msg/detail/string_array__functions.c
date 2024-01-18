// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_msgs:msg/StringArray.idl
// generated code does not contain a copyright notice
#include "custom_msgs/msg/detail/string_array__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `detections`
#include "custom_msgs/msg/detail/detections__functions.h"

bool
custom_msgs__msg__StringArray__init(custom_msgs__msg__StringArray * msg)
{
  if (!msg) {
    return false;
  }
  // detections
  if (!custom_msgs__msg__Detections__Sequence__init(&msg->detections, 0)) {
    custom_msgs__msg__StringArray__fini(msg);
    return false;
  }
  return true;
}

void
custom_msgs__msg__StringArray__fini(custom_msgs__msg__StringArray * msg)
{
  if (!msg) {
    return;
  }
  // detections
  custom_msgs__msg__Detections__Sequence__fini(&msg->detections);
}

bool
custom_msgs__msg__StringArray__are_equal(const custom_msgs__msg__StringArray * lhs, const custom_msgs__msg__StringArray * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // detections
  if (!custom_msgs__msg__Detections__Sequence__are_equal(
      &(lhs->detections), &(rhs->detections)))
  {
    return false;
  }
  return true;
}

bool
custom_msgs__msg__StringArray__copy(
  const custom_msgs__msg__StringArray * input,
  custom_msgs__msg__StringArray * output)
{
  if (!input || !output) {
    return false;
  }
  // detections
  if (!custom_msgs__msg__Detections__Sequence__copy(
      &(input->detections), &(output->detections)))
  {
    return false;
  }
  return true;
}

custom_msgs__msg__StringArray *
custom_msgs__msg__StringArray__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_msgs__msg__StringArray * msg = (custom_msgs__msg__StringArray *)allocator.allocate(sizeof(custom_msgs__msg__StringArray), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_msgs__msg__StringArray));
  bool success = custom_msgs__msg__StringArray__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_msgs__msg__StringArray__destroy(custom_msgs__msg__StringArray * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_msgs__msg__StringArray__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_msgs__msg__StringArray__Sequence__init(custom_msgs__msg__StringArray__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_msgs__msg__StringArray * data = NULL;

  if (size) {
    data = (custom_msgs__msg__StringArray *)allocator.zero_allocate(size, sizeof(custom_msgs__msg__StringArray), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_msgs__msg__StringArray__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_msgs__msg__StringArray__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_msgs__msg__StringArray__Sequence__fini(custom_msgs__msg__StringArray__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_msgs__msg__StringArray__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_msgs__msg__StringArray__Sequence *
custom_msgs__msg__StringArray__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_msgs__msg__StringArray__Sequence * array = (custom_msgs__msg__StringArray__Sequence *)allocator.allocate(sizeof(custom_msgs__msg__StringArray__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_msgs__msg__StringArray__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_msgs__msg__StringArray__Sequence__destroy(custom_msgs__msg__StringArray__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_msgs__msg__StringArray__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_msgs__msg__StringArray__Sequence__are_equal(const custom_msgs__msg__StringArray__Sequence * lhs, const custom_msgs__msg__StringArray__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_msgs__msg__StringArray__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_msgs__msg__StringArray__Sequence__copy(
  const custom_msgs__msg__StringArray__Sequence * input,
  custom_msgs__msg__StringArray__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_msgs__msg__StringArray);
    custom_msgs__msg__StringArray * data =
      (custom_msgs__msg__StringArray *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_msgs__msg__StringArray__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          custom_msgs__msg__StringArray__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_msgs__msg__StringArray__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

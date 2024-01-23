// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_msgs:msg/Detection.idl
// generated code does not contain a copyright notice
#include "custom_msgs/msg/detail/detection__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `name`
// Member `id`
#include "std_msgs/msg/detail/string__functions.h"
// Member `location_x`
// Member `location_y`
// Member `screen_size_x`
// Member `screen_size_y`
// Member `confidence`
#include "std_msgs/msg/detail/float32__functions.h"

bool
custom_msgs__msg__Detection__init(custom_msgs__msg__Detection * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!std_msgs__msg__String__init(&msg->name)) {
    custom_msgs__msg__Detection__fini(msg);
    return false;
  }
  // id
  if (!std_msgs__msg__String__init(&msg->id)) {
    custom_msgs__msg__Detection__fini(msg);
    return false;
  }
  // location_x
  if (!std_msgs__msg__Float32__init(&msg->location_x)) {
    custom_msgs__msg__Detection__fini(msg);
    return false;
  }
  // location_y
  if (!std_msgs__msg__Float32__init(&msg->location_y)) {
    custom_msgs__msg__Detection__fini(msg);
    return false;
  }
  // screen_size_x
  if (!std_msgs__msg__Float32__init(&msg->screen_size_x)) {
    custom_msgs__msg__Detection__fini(msg);
    return false;
  }
  // screen_size_y
  if (!std_msgs__msg__Float32__init(&msg->screen_size_y)) {
    custom_msgs__msg__Detection__fini(msg);
    return false;
  }
  // confidence
  if (!std_msgs__msg__Float32__init(&msg->confidence)) {
    custom_msgs__msg__Detection__fini(msg);
    return false;
  }
  return true;
}

void
custom_msgs__msg__Detection__fini(custom_msgs__msg__Detection * msg)
{
  if (!msg) {
    return;
  }
  // name
  std_msgs__msg__String__fini(&msg->name);
  // id
  std_msgs__msg__String__fini(&msg->id);
  // location_x
  std_msgs__msg__Float32__fini(&msg->location_x);
  // location_y
  std_msgs__msg__Float32__fini(&msg->location_y);
  // screen_size_x
  std_msgs__msg__Float32__fini(&msg->screen_size_x);
  // screen_size_y
  std_msgs__msg__Float32__fini(&msg->screen_size_y);
  // confidence
  std_msgs__msg__Float32__fini(&msg->confidence);
}

bool
custom_msgs__msg__Detection__are_equal(const custom_msgs__msg__Detection * lhs, const custom_msgs__msg__Detection * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!std_msgs__msg__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // id
  if (!std_msgs__msg__String__are_equal(
      &(lhs->id), &(rhs->id)))
  {
    return false;
  }
  // location_x
  if (!std_msgs__msg__Float32__are_equal(
      &(lhs->location_x), &(rhs->location_x)))
  {
    return false;
  }
  // location_y
  if (!std_msgs__msg__Float32__are_equal(
      &(lhs->location_y), &(rhs->location_y)))
  {
    return false;
  }
  // screen_size_x
  if (!std_msgs__msg__Float32__are_equal(
      &(lhs->screen_size_x), &(rhs->screen_size_x)))
  {
    return false;
  }
  // screen_size_y
  if (!std_msgs__msg__Float32__are_equal(
      &(lhs->screen_size_y), &(rhs->screen_size_y)))
  {
    return false;
  }
  // confidence
  if (!std_msgs__msg__Float32__are_equal(
      &(lhs->confidence), &(rhs->confidence)))
  {
    return false;
  }
  return true;
}

bool
custom_msgs__msg__Detection__copy(
  const custom_msgs__msg__Detection * input,
  custom_msgs__msg__Detection * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!std_msgs__msg__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // id
  if (!std_msgs__msg__String__copy(
      &(input->id), &(output->id)))
  {
    return false;
  }
  // location_x
  if (!std_msgs__msg__Float32__copy(
      &(input->location_x), &(output->location_x)))
  {
    return false;
  }
  // location_y
  if (!std_msgs__msg__Float32__copy(
      &(input->location_y), &(output->location_y)))
  {
    return false;
  }
  // screen_size_x
  if (!std_msgs__msg__Float32__copy(
      &(input->screen_size_x), &(output->screen_size_x)))
  {
    return false;
  }
  // screen_size_y
  if (!std_msgs__msg__Float32__copy(
      &(input->screen_size_y), &(output->screen_size_y)))
  {
    return false;
  }
  // confidence
  if (!std_msgs__msg__Float32__copy(
      &(input->confidence), &(output->confidence)))
  {
    return false;
  }
  return true;
}

custom_msgs__msg__Detection *
custom_msgs__msg__Detection__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_msgs__msg__Detection * msg = (custom_msgs__msg__Detection *)allocator.allocate(sizeof(custom_msgs__msg__Detection), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_msgs__msg__Detection));
  bool success = custom_msgs__msg__Detection__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_msgs__msg__Detection__destroy(custom_msgs__msg__Detection * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_msgs__msg__Detection__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_msgs__msg__Detection__Sequence__init(custom_msgs__msg__Detection__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_msgs__msg__Detection * data = NULL;

  if (size) {
    data = (custom_msgs__msg__Detection *)allocator.zero_allocate(size, sizeof(custom_msgs__msg__Detection), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_msgs__msg__Detection__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_msgs__msg__Detection__fini(&data[i - 1]);
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
custom_msgs__msg__Detection__Sequence__fini(custom_msgs__msg__Detection__Sequence * array)
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
      custom_msgs__msg__Detection__fini(&array->data[i]);
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

custom_msgs__msg__Detection__Sequence *
custom_msgs__msg__Detection__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_msgs__msg__Detection__Sequence * array = (custom_msgs__msg__Detection__Sequence *)allocator.allocate(sizeof(custom_msgs__msg__Detection__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_msgs__msg__Detection__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_msgs__msg__Detection__Sequence__destroy(custom_msgs__msg__Detection__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_msgs__msg__Detection__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_msgs__msg__Detection__Sequence__are_equal(const custom_msgs__msg__Detection__Sequence * lhs, const custom_msgs__msg__Detection__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_msgs__msg__Detection__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_msgs__msg__Detection__Sequence__copy(
  const custom_msgs__msg__Detection__Sequence * input,
  custom_msgs__msg__Detection__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_msgs__msg__Detection);
    custom_msgs__msg__Detection * data =
      (custom_msgs__msg__Detection *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_msgs__msg__Detection__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          custom_msgs__msg__Detection__fini(&data[i]);
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
    if (!custom_msgs__msg__Detection__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

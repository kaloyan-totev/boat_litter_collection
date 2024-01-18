// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from custom_msgs:msg/Detections.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "custom_msgs/msg/detail/detections__struct.h"
#include "custom_msgs/msg/detail/detections__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__string__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__string__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__string__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__string__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__string__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__string__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__string__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__string__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__string__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__string__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__string__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__string__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool custom_msgs__msg__detections__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[39];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("custom_msgs.msg._detections.Detections", full_classname_dest, 38) == 0);
  }
  custom_msgs__msg__Detections * ros_message = _ros_message;
  {  // name
    PyObject * field = PyObject_GetAttrString(_pymsg, "name");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__string__convert_from_py(field, &ros_message->name)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // id
    PyObject * field = PyObject_GetAttrString(_pymsg, "id");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__string__convert_from_py(field, &ros_message->id)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // location_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "location_x");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__string__convert_from_py(field, &ros_message->location_x)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // location_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "location_y");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__string__convert_from_py(field, &ros_message->location_y)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // screen_size_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "screen_size_x");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__string__convert_from_py(field, &ros_message->screen_size_x)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // screen_size_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "screen_size_y");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__string__convert_from_py(field, &ros_message->screen_size_y)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * custom_msgs__msg__detections__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Detections */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("custom_msgs.msg._detections");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Detections");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  custom_msgs__msg__Detections * ros_message = (custom_msgs__msg__Detections *)raw_ros_message;
  {  // name
    PyObject * field = NULL;
    field = std_msgs__msg__string__convert_to_py(&ros_message->name);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // id
    PyObject * field = NULL;
    field = std_msgs__msg__string__convert_to_py(&ros_message->id);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // location_x
    PyObject * field = NULL;
    field = std_msgs__msg__string__convert_to_py(&ros_message->location_x);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "location_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // location_y
    PyObject * field = NULL;
    field = std_msgs__msg__string__convert_to_py(&ros_message->location_y);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "location_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // screen_size_x
    PyObject * field = NULL;
    field = std_msgs__msg__string__convert_to_py(&ros_message->screen_size_x);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "screen_size_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // screen_size_y
    PyObject * field = NULL;
    field = std_msgs__msg__string__convert_to_py(&ros_message->screen_size_y);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "screen_size_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#include <python3.12/Python.h>

static PyObject *add_function(PyObject *self, PyObject *args) {
    float a, b;
    if (!PyArg_ParseTuple(args, "ff", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("f", a + b);
}

static PyObject *sub_function(PyObject *self, PyObject *args) {
    float a, b;
    if (!PyArg_ParseTuple(args, "ff", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("f", a - b);
}

static PyObject *mul_function(PyObject *self, PyObject *args) {
    float a, b;
    if (!PyArg_ParseTuple(args, "ff", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("f", a * b);
}

static PyObject *div_function(PyObject *self, PyObject *args) {
    float a, b;
    if (!PyArg_ParseTuple(args, "ff", &a, &b)) {
        return NULL;
    }
    if (b == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero.");
        return NULL;
    }
    return Py_BuildValue("f", a / b);
}

static PyMethodDef calculator_methods[] = {
    {"add", (PyCFunction)add_function, METH_VARARGS, "Add two numbers"},
    {"sub", (PyCFunction)sub_function, METH_VARARGS, "Subtract two numbers"},
    {"mul", (PyCFunction)mul_function, METH_VARARGS, "Multiply two numbers"},
    {"div", (PyCFunction)div_function, METH_VARARGS, "Divide two numbers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef calculator_module = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    "simple calculator",
    -1,
    calculator_methods
};

PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculator_module);
}

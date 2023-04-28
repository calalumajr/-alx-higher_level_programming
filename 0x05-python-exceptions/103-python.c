#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[*] Python list info\n");
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

#include <Python.h>

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[*] Python bytes info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    if (size < 10)
        printf("  first %ld bytes: ", size + 1);
    else
        printf("  first 10 bytes: ");

    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx%s", str[i], i == 9 ? "\n" : " ");
}

#include <Python.h>

void print_python_float(PyObject *p) {
    double value;

    if (!PyFloat_Check(p)) {
        printf("[*] Python float info\n");
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    printf("  value: %.17g\n", value);
}



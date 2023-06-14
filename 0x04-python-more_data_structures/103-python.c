#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Prints information about a Python bytes object
* @p: Pointer to the Python bytes object
*/
void print_python_bytes(PyObject *p)
{
if (p == NULL || !PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
return;
}

Py_ssize_t size = PyBytes_Size(p);
printf("[.] bytes object info\n");
printf("  size: %ld\n", size);

char *str = PyBytes_AsString(p);
printf("  trying string: %s\n", str);

printf("  first 10 bytes:");
for (Py_ssize_t i = 0; i < size && i < 10; i++)
{
printf(" %02x", (unsigned char) str[i]);
}
printf("\n");
}

/**
* print_python_list - Prints information about a Python list object
* @p: Pointer to the Python list object
*/
void print_python_list(PyObject *p)
{
if (p == NULL || !PyList_Check(p))
{
printf("[ERROR] Invalid List Object\n");
return;
}

Py_ssize_t size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *elem = PyList_GetItem(p, i);
printf("Element %ld: ", i);

if (PyBytes_Check(elem))
{
print_python_bytes(elem);
}
else
{
printf("%s\n", Py_TYPE(elem)->tp_name);
}
}
}

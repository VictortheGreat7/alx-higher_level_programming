#include <Python.h>
#include <stdio.h>

/**
* print_python_list - Prints information about a Pythonl list object
* @p: Pointer to the Python list object
* Description: This function prints the size and allocation details of a
*		Python list, as well as the type of each element in the list.
*/
void print_python_list(PyObject *p)
{
	/* Check if the given object is a Python list */
	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	/* Get the size and allocation of the list */
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	/* Iterate over each element and print out its type */
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type);
	}
}

/**
* print_python_bytes - Prints information about a Python bytes object
* @p: Pointer to the Python bytes object
* Description: This function prints the size, string representation,
*		and the hexadecimal representation of the first 10
*		bytes of a Python bytes object.
*/
void print_python_bytes(PyObject *p)
{
	/* Check if the given object is a Python bytes object */
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Get the size and string representation of the bytes object */
	Py_ssize_t size = PyBytes_Size(p);
	const char *string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	/* Print the hexadecimal representation of the first 10 bytes */
	printf("  first %d bytes:", (size < 10 ? (int)size : 10));
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}

/**
* print_python_float - Prints information about a Python float object
* @p: Pointer to the Python float object
* Description: This function prints the value of a Python float object.
*/
void print_python_float(PyObject *p)
{
	/* Check if the given object is a Python float object */
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	/* Get the value of the float object */
	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}


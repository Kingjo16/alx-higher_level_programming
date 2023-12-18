#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);
/**
 * print_python_bytes - Prints info/
 * @p: PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t k;
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		Py_ssize_t byte_size = PyBytes_Size(p);
		printf("  size: %ld\n", byte_size);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first %ld bytes:", byte_size + 1 > 10 ? 10 : byte_size + 1);
		for (k = 0; k < byte_size + 1 && k < 10; k++)
		{
			printf(" %02hhx", *((char *)PyBytes_AsString(p) + k));
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Prints Info/
 * @p: PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t k, list_size;
	PyObject *list_element;

	list_size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (k = 0; k < list_size; k++)
	{
		list_element = PyList_GetItem(p, k);
		printf("Element %ld: %s\n", k, Py_TYPE(list_element)->tp_name);
		if (PyBytes_Check(list_element))
			print_python_bytes(list_element);
		else if (PyFloat_Check(list_element))
			print_python_float(list_element);
	}
}

/**
 * print_python_float - Prints Info/
 * @p: PyObject
 */

void print_python_float(PyObject *p)
{
	double float_value;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		float_value = ((PyFloatObject *)p)->ob_fval;
		printf("  value: %.*g\n", 17, float_value);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
}

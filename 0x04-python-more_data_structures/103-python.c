#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This pritns info abt the py byts
 * @obj: Pyobject This is a py byts object
 */

void print_python_bytes(PyObject *obj)
{
	char *byte_str;
	Py_ssize_t byte_size, idx;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = PyBytes_Size(obj);
	byte_str = PyBytes_AsString(obj);

	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", byte_str);
	printf("  first %ld bytes: ", byte_size < 10 ? byte_size + 1 : 10);

	for (idx = 0; idx <= byte_size && idx < 10; idx++)
		printf("%02x%s", (unsigned char)byte_str[idx], idx == byte_size ||
				idx == 9 ? "" : " ");
	printf("\n");
}

/**
 * print_python_list - This also Pritn info abt the py list
 * @obj: Pyobject this the list of the obj
 */

void print_python_list(PyObject *obj)
{
	Py_ssize_t list_size, alloc_size, idx;
	PyObject *item;

	printf("[*] Python list info\n");

	list_size = PyList_Size(obj);
	alloc_size = ((PyListObject *)obj)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", alloc_size);

	for (idx = 0; idx < list_size; idx++)
	{
		item = PyList_GetItem(obj, idx);
		printf("Element %ld: %s\n", idx, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

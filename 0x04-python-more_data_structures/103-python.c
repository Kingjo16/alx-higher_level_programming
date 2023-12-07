#include <stdio.h>
#include <stdlib.h>

struct timespec;

#include <time.h>
#include <Python.h>

/**
 * print_python_bytes - This pritns info abt the py byts
 * @p: Pyobject This is a py byts object
 */

void print_python_bytes(PyObject *p)
{
	char *byte_str;
	long int byte_size, idx, byte_limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = ((PyVarObject *)(p))->ob_size;
	byte_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", byte_str);

	if (byte_size >= 10)
		byte_limit = 10;
	else
		byte_limit = byte_size + 1;

	printf("  first %ld bytes: ", byte_limit);

	for (idx = 0; idx < byte_limit; idx++)
		if (byte_str[idx] >= 0)
			printf(" %02x", byte_str[idx]);
		else
			printf(" %02x", 256 + byte_str[idx]);

	printf("\n");
}

/**
 * print_python_list - This also Pritn info abt the py list
 * @p: Pyobject this the list of the obj
 */

void print_python_list(PyObject *p)
{
	long int list_size, idx;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");

	list_size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < list_size; idx++)
	{
		item = ((PyListObject *)p)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

#include <stdio.h>

struct timespec;

#include <time.h>
#include <Python.h>

/**
 * print_python_bytes - This pritns info abt the py byts
 * @obj: Pyobject This is a py byts object
 */

void print_python_bytes(PyObject *obj)
{
	char *byte_str;
	long int byte_size, idx, byte_limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = ((PyVarObject *)(obj))->ob_size;
	byte_str = ((PyBytesObject *)obj)->ob_sval;

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
 * @obj: Pyobject this the list of the obj
 */

void print_python_list(PyObject *obj)
{
	long int list_size, idx;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");

	list_size = ((PyVarObject *)(obj))->ob_size;
	list = (PyListObject *)obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < list_size; idx++)
	{
		item = ((PyListObject *)obj)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

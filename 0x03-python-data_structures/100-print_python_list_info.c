#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints a python ifo list form c and alloc
 * @p: A pointer for
 * pyobjext
 * Return: Void
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int m;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (m = 0; m < size; m++)
		printf("Element %i: %s\n", m, Py_TYPE(obj->ob_item[m])->tp_name);
}

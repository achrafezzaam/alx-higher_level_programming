#include <Python.h>
/**
 * print_python_list_info - Print basic info of a list
 * @p: list to get the info of
 */
void print_python_list_info(PyObject *p)
{
	int size, i, n;
	PyObject *elem;

	size = Py_SIZE(p);
	n = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", n);
	for (i = 0; i < size; i++)
	{
		elem = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(elem)->tp_name);
	}
}

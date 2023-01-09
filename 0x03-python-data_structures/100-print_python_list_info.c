#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
        PyObject *obj;
        int i, size, alloc;

        alloc = ((PyListObject *)p)->allocated;
        size = Py_SIZE(p);

        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", alloc);

        for (i = 0; i < size; i++)
        {
                printf("Element %d: ", i);

                obj = PyList_GetItem(p, i);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}

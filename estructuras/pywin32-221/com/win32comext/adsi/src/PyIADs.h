// This file declares the IADs Interface and Gateway for Python.
// Generated by makegw.py
// ---------------------------------------------------
//
// Interface Declaration

class PyIADs : public PyIDispatch
{
public:
	MAKE_PYCOM_CTOR(PyIADs);
	static IADs *GetI(PyObject *self);
	static PyComTypeObject type;

	// The Python methods
	static PyObject *GetInfo(PyObject *self, PyObject *args);
	static PyObject *SetInfo(PyObject *self, PyObject *args);
	static PyObject *Get(PyObject *self, PyObject *args);
	static PyObject *Put(PyObject *self, PyObject *args);
	static PyObject *GetEx(PyObject *self, PyObject *args);
	static PyObject *PutEx(PyObject *self, PyObject *args);
	static PyObject *GetInfoEx(PyObject *self, PyObject *args);

protected:
	PyIADs(IUnknown *pdisp);
	~PyIADs();
};

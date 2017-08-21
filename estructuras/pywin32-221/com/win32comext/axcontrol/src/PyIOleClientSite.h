// This file declares the IOleClientSite Interface and Gateway for Python.
// Generated by makegw.py
// ---------------------------------------------------
//
// Interface Declaration

class PyIOleClientSite : public PyIUnknown
{
public:
	MAKE_PYCOM_CTOR(PyIOleClientSite);
	static IOleClientSite *GetI(PyObject *self);
	static PyComTypeObject type;

	// The Python methods
	static PyObject *SaveObject(PyObject *self, PyObject *args);
	static PyObject *GetMoniker(PyObject *self, PyObject *args);
	static PyObject *GetContainer(PyObject *self, PyObject *args);
	static PyObject *ShowObject(PyObject *self, PyObject *args);
	static PyObject *OnShowWindow(PyObject *self, PyObject *args);
	static PyObject *RequestNewObjectLayout(PyObject *self, PyObject *args);

protected:
	PyIOleClientSite(IUnknown *pdisp);
	~PyIOleClientSite();
};
// ---------------------------------------------------
//
// Gateway Declaration

class PyGOleClientSite : public PyGatewayBase, public IOleClientSite
{
protected:
	PyGOleClientSite(PyObject *instance) : PyGatewayBase(instance) { ; }
	PYGATEWAY_MAKE_SUPPORT(PyGOleClientSite, IOleClientSite, IID_IOleClientSite)

	// IOleClientSite
	STDMETHOD(SaveObject)(
		void);

	STDMETHOD(GetMoniker)(
		DWORD dwAssign,
		DWORD dwWhichMoniker,
		IMoniker __RPC_FAR *__RPC_FAR * ppmk);

	STDMETHOD(GetContainer)(
		IOleContainer __RPC_FAR *__RPC_FAR * ppContainer);

	STDMETHOD(ShowObject)(
		void);

	STDMETHOD(OnShowWindow)(
		BOOL fShow);

	STDMETHOD(RequestNewObjectLayout)(
		void);

};

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""'pysu2' module"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pysu2
else:
    import _pysu2

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class SwigPyIterator(object):
    r"""Proxy of C++ swig::SwigPyIterator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pysu2.delete_SwigPyIterator

    def value(self):
        r"""value(SwigPyIterator self) -> PyObject *"""
        return _pysu2.SwigPyIterator_value(self)

    def incr(self, n=1):
        r"""incr(SwigPyIterator self, size_t n=1) -> SwigPyIterator"""
        return _pysu2.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        r"""decr(SwigPyIterator self, size_t n=1) -> SwigPyIterator"""
        return _pysu2.SwigPyIterator_decr(self, n)

    def distance(self, x):
        r"""distance(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t"""
        return _pysu2.SwigPyIterator_distance(self, x)

    def equal(self, x):
        r"""equal(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _pysu2.SwigPyIterator_equal(self, x)

    def copy(self):
        r"""copy(SwigPyIterator self) -> SwigPyIterator"""
        return _pysu2.SwigPyIterator_copy(self)

    def next(self):
        r"""next(SwigPyIterator self) -> PyObject *"""
        return _pysu2.SwigPyIterator_next(self)

    def __next__(self):
        r"""__next__(SwigPyIterator self) -> PyObject *"""
        return _pysu2.SwigPyIterator___next__(self)

    def previous(self):
        r"""previous(SwigPyIterator self) -> PyObject *"""
        return _pysu2.SwigPyIterator_previous(self)

    def advance(self, n):
        r"""advance(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        r"""__eq__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _pysu2.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        r"""__ne__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _pysu2.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        r"""__iadd__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        r"""__isub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        r"""__add__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _pysu2.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        r"""
        __sub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator
        __sub__(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t
        """
        return _pysu2.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _pysu2:
_pysu2.SwigPyIterator_swigregister(SwigPyIterator)

SU2_COMPONENT_SU2_CFD = _pysu2.SU2_COMPONENT_SU2_CFD

SU2_COMPONENT_SU2_DEF = _pysu2.SU2_COMPONENT_SU2_DEF

SU2_COMPONENT_SU2_DOT = _pysu2.SU2_COMPONENT_SU2_DOT

SU2_COMPONENT_SU2_GEO = _pysu2.SU2_COMPONENT_SU2_GEO

SU2_COMPONENT_SU2_SOL = _pysu2.SU2_COMPONENT_SU2_SOL

class CPyWrapperMatrixView(object):
    r"""Proxy of C++ CPyWrapperMatrixView class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(CPyWrapperMatrixView self) -> CPyWrapperMatrixView
        __init__(CPyWrapperMatrixView self, su2activematrix & mat, std::string const & name, bool read_only) -> CPyWrapperMatrixView
        """
        _pysu2.CPyWrapperMatrixView_swiginit(self, _pysu2.new_CPyWrapperMatrixView(*args))

    def Shape(self):
        r"""Shape(CPyWrapperMatrixView self) -> std::pair< unsigned long,unsigned long >"""
        return _pysu2.CPyWrapperMatrixView_Shape(self)

    def IsReadOnly(self):
        r"""IsReadOnly(CPyWrapperMatrixView self) -> bool"""
        return _pysu2.CPyWrapperMatrixView_IsReadOnly(self)

    def __call__(self, row, col):
        r"""__call__(CPyWrapperMatrixView self, unsigned long row, unsigned long col) -> passivedouble"""
        return _pysu2.CPyWrapperMatrixView___call__(self, row, col)

    def Get(self, *args):
        r"""
        Get(CPyWrapperMatrixView self, unsigned long row, unsigned long col) -> passivedouble
        Get(CPyWrapperMatrixView self, unsigned long row) -> std::vector< passivedouble,std::allocator< passivedouble > >
        """
        return _pysu2.CPyWrapperMatrixView_Get(self, *args)

    def Set(self, *args):
        r"""
        Set(CPyWrapperMatrixView self, unsigned long row, unsigned long col, passivedouble val)
        Set(CPyWrapperMatrixView self, unsigned long row, std::vector< passivedouble,std::allocator< passivedouble > > vals)
        """
        return _pysu2.CPyWrapperMatrixView_Set(self, *args)
    __swig_destroy__ = _pysu2.delete_CPyWrapperMatrixView

# Register CPyWrapperMatrixView in _pysu2:
_pysu2.CPyWrapperMatrixView_swigregister(CPyWrapperMatrixView)
cvar = _pysu2.cvar
MESH_0 = cvar.MESH_0
MESH_1 = cvar.MESH_1
ZONE_0 = cvar.ZONE_0
ZONE_1 = cvar.ZONE_1

class CPyWrapperMarkerMatrixView(object):
    r"""Proxy of C++ CPyWrapperMarkerMatrixView class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(CPyWrapperMarkerMatrixView self) -> CPyWrapperMarkerMatrixView
        __init__(CPyWrapperMarkerMatrixView self, su2activematrix & mat, CVertex const *const * vertices, unsigned long n_vertices, std::string const & name, bool read_only) -> CPyWrapperMarkerMatrixView
        """
        _pysu2.CPyWrapperMarkerMatrixView_swiginit(self, _pysu2.new_CPyWrapperMarkerMatrixView(*args))

    def Shape(self):
        r"""Shape(CPyWrapperMarkerMatrixView self) -> std::pair< unsigned long,unsigned long >"""
        return _pysu2.CPyWrapperMarkerMatrixView_Shape(self)

    def IsReadOnly(self):
        r"""IsReadOnly(CPyWrapperMarkerMatrixView self) -> bool"""
        return _pysu2.CPyWrapperMarkerMatrixView_IsReadOnly(self)

    def __call__(self, row, col):
        r"""__call__(CPyWrapperMarkerMatrixView self, unsigned long row, unsigned long col) -> passivedouble"""
        return _pysu2.CPyWrapperMarkerMatrixView___call__(self, row, col)

    def Get(self, *args):
        r"""
        Get(CPyWrapperMarkerMatrixView self, unsigned long row, unsigned long col) -> passivedouble
        Get(CPyWrapperMarkerMatrixView self, unsigned long row) -> std::vector< passivedouble,std::allocator< passivedouble > >
        """
        return _pysu2.CPyWrapperMarkerMatrixView_Get(self, *args)

    def Set(self, *args):
        r"""
        Set(CPyWrapperMarkerMatrixView self, unsigned long row, unsigned long col, passivedouble val)
        Set(CPyWrapperMarkerMatrixView self, unsigned long row, std::vector< passivedouble,std::allocator< passivedouble > > vals)
        """
        return _pysu2.CPyWrapperMarkerMatrixView_Set(self, *args)
    __swig_destroy__ = _pysu2.delete_CPyWrapperMarkerMatrixView

# Register CPyWrapperMarkerMatrixView in _pysu2:
_pysu2.CPyWrapperMarkerMatrixView_swigregister(CPyWrapperMarkerMatrixView)

class CDriverBase(object):
    r"""Proxy of C++ CDriverBase class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        r"""__init__(CDriverBase self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CDriverBase"""
        _pysu2.CDriverBase_swiginit(self, _pysu2.new_CDriverBase(confFile, val_nZone, MPICommunicator))
    __swig_destroy__ = _pysu2.delete_CDriverBase

    def Run(self):
        r"""Run(CDriverBase self)"""
        return _pysu2.CDriverBase_Run(self)

    def Finalize(self):
        r"""Finalize(CDriverBase self)"""
        return _pysu2.CDriverBase_Finalize(self)

    def GetOutputNames(self):
        r"""GetOutputNames(CDriverBase self) -> vector< string >"""
        return _pysu2.CDriverBase_GetOutputNames(self)

    def GetOutputValue(self, output_name):
        r"""GetOutputValue(CDriverBase self, std::string const & output_name) -> passivedouble"""
        return _pysu2.CDriverBase_GetOutputValue(self, output_name)

    def GetMarkerOutputNames(self):
        r"""GetMarkerOutputNames(CDriverBase self) -> vector< string >"""
        return _pysu2.CDriverBase_GetMarkerOutputNames(self)

    def GetMarkerMonitoringOutputValue(self, output_name, marker_monitoring):
        r"""GetMarkerMonitoringOutputValue(CDriverBase self, std::string const & output_name, std::string const & marker_monitoring) -> passivedouble"""
        return _pysu2.CDriverBase_GetMarkerMonitoringOutputValue(self, output_name, marker_monitoring)

    def GetMarkerAnalyzeOutputValue(self, output_name, marker_analyze):
        r"""GetMarkerAnalyzeOutputValue(CDriverBase self, std::string const & output_name, std::string const & marker_analyze) -> passivedouble"""
        return _pysu2.CDriverBase_GetMarkerAnalyzeOutputValue(self, output_name, marker_analyze)

    def GetNumberDesignVariables(self):
        r"""GetNumberDesignVariables(CDriverBase self) -> unsigned short"""
        return _pysu2.CDriverBase_GetNumberDesignVariables(self)

    def GetNumberFFDBoxes(self):
        r"""GetNumberFFDBoxes(CDriverBase self) -> unsigned short"""
        return _pysu2.CDriverBase_GetNumberFFDBoxes(self)

    def GetNumberDimensions(self):
        r"""GetNumberDimensions(CDriverBase self) -> unsigned long"""
        return _pysu2.CDriverBase_GetNumberDimensions(self)

    def GetNumberElements(self):
        r"""GetNumberElements(CDriverBase self) -> unsigned long"""
        return _pysu2.CDriverBase_GetNumberElements(self)

    def GetElementGlobalIndex(self, iElem):
        r"""GetElementGlobalIndex(CDriverBase self, unsigned long iElem) -> unsigned long"""
        return _pysu2.CDriverBase_GetElementGlobalIndex(self, iElem)

    def GetElementNodes(self, iElem):
        r"""GetElementNodes(CDriverBase self, unsigned long iElem) -> vector< unsigned long >"""
        return _pysu2.CDriverBase_GetElementNodes(self, iElem)

    def GetNumberNodes(self):
        r"""GetNumberNodes(CDriverBase self) -> unsigned long"""
        return _pysu2.CDriverBase_GetNumberNodes(self)

    def GetNumberHaloNodes(self):
        r"""GetNumberHaloNodes(CDriverBase self) -> unsigned long"""
        return _pysu2.CDriverBase_GetNumberHaloNodes(self)

    def GetNodeGlobalIndex(self, iPoint):
        r"""GetNodeGlobalIndex(CDriverBase self, unsigned long iPoint) -> unsigned long"""
        return _pysu2.CDriverBase_GetNodeGlobalIndex(self, iPoint)

    def GetNodeDomain(self, iPoint):
        r"""GetNodeDomain(CDriverBase self, unsigned long iPoint) -> bool"""
        return _pysu2.CDriverBase_GetNodeDomain(self, iPoint)

    def InitialCoordinates(self):
        r"""InitialCoordinates(CDriverBase self) -> CPyWrapperMatrixView"""
        return _pysu2.CDriverBase_InitialCoordinates(self)

    def MarkerInitialCoordinates(self, iMarker):
        r"""MarkerInitialCoordinates(CDriverBase self, unsigned short iMarker) -> CPyWrapperMarkerMatrixView"""
        return _pysu2.CDriverBase_MarkerInitialCoordinates(self, iMarker)

    def Coordinates(self):
        r"""Coordinates(CDriverBase self) -> CPyWrapperMatrixView"""
        return _pysu2.CDriverBase_Coordinates(self)

    def MarkerCoordinates(self, iMarker):
        r"""MarkerCoordinates(CDriverBase self, unsigned short iMarker) -> CPyWrapperMarkerMatrixView"""
        return _pysu2.CDriverBase_MarkerCoordinates(self, iMarker)

    def GetNumberMarkers(self):
        r"""GetNumberMarkers(CDriverBase self) -> unsigned short"""
        return _pysu2.CDriverBase_GetNumberMarkers(self)

    def GetMarkerIndices(self):
        r"""GetMarkerIndices(CDriverBase self) -> map< string,unsigned short >"""
        return _pysu2.CDriverBase_GetMarkerIndices(self)

    def GetMarkerTypes(self):
        r"""GetMarkerTypes(CDriverBase self) -> map< string,string >"""
        return _pysu2.CDriverBase_GetMarkerTypes(self)

    def GetMarkerTags(self):
        r"""GetMarkerTags(CDriverBase self) -> vector< string >"""
        return _pysu2.CDriverBase_GetMarkerTags(self)

    def GetDeformableMarkerTags(self):
        r"""GetDeformableMarkerTags(CDriverBase self) -> vector< string >"""
        return _pysu2.CDriverBase_GetDeformableMarkerTags(self)

    def GetCHTMarkerTags(self):
        r"""GetCHTMarkerTags(CDriverBase self) -> vector< string >"""
        return _pysu2.CDriverBase_GetCHTMarkerTags(self)

    def GetInletMarkerTags(self):
        r"""GetInletMarkerTags(CDriverBase self) -> vector< string >"""
        return _pysu2.CDriverBase_GetInletMarkerTags(self)

    def GetNumberMarkerElements(self, iMarker):
        r"""GetNumberMarkerElements(CDriverBase self, unsigned short iMarker) -> unsigned long"""
        return _pysu2.CDriverBase_GetNumberMarkerElements(self, iMarker)

    def GetMarkerElementGlobalIndex(self, iMarker, iElem):
        r"""GetMarkerElementGlobalIndex(CDriverBase self, unsigned short iMarker, unsigned long iElem) -> unsigned long"""
        return _pysu2.CDriverBase_GetMarkerElementGlobalIndex(self, iMarker, iElem)

    def GetMarkerElementNodes(self, iMarker, iElem):
        r"""GetMarkerElementNodes(CDriverBase self, unsigned short iMarker, unsigned long iElem) -> vector< unsigned long >"""
        return _pysu2.CDriverBase_GetMarkerElementNodes(self, iMarker, iElem)

    def GetNumberMarkerNodes(self, iMarker):
        r"""GetNumberMarkerNodes(CDriverBase self, unsigned short iMarker) -> unsigned long"""
        return _pysu2.CDriverBase_GetNumberMarkerNodes(self, iMarker)

    def GetMarkerNode(self, iMarker, iVertex):
        r"""GetMarkerNode(CDriverBase self, unsigned short iMarker, unsigned long iVertex) -> unsigned long"""
        return _pysu2.CDriverBase_GetMarkerNode(self, iMarker, iVertex)

    def GetMarkerVertexNormals(self, iMarker, iVertex, normalize=False):
        r"""GetMarkerVertexNormals(CDriverBase self, unsigned short iMarker, unsigned long iVertex, bool normalize=False) -> vector< passivedouble >"""
        return _pysu2.CDriverBase_GetMarkerVertexNormals(self, iMarker, iVertex, normalize)

    def GetMarkerDisplacement(self, iMarker, iVertex):
        r"""GetMarkerDisplacement(CDriverBase self, unsigned short iMarker, unsigned long iVertex) -> vector< passivedouble >"""
        return _pysu2.CDriverBase_GetMarkerDisplacement(self, iMarker, iVertex)

    def SetMarkerCustomDisplacement(self, iMarker, iVertex, values):
        r"""SetMarkerCustomDisplacement(CDriverBase self, unsigned short iMarker, unsigned long iVertex, vector< passivedouble > values)"""
        return _pysu2.CDriverBase_SetMarkerCustomDisplacement(self, iMarker, iVertex, values)

    def GetMarkerMeshVelocity(self, iMarker, iVertex):
        r"""GetMarkerMeshVelocity(CDriverBase self, unsigned short iMarker, unsigned long iVertex) -> vector< passivedouble >"""
        return _pysu2.CDriverBase_GetMarkerMeshVelocity(self, iMarker, iVertex)

    def SetMarkerCustomMeshVelocity(self, iMarker, iVertex, values):
        r"""SetMarkerCustomMeshVelocity(CDriverBase self, unsigned short iMarker, unsigned long iVertex, vector< passivedouble > values)"""
        return _pysu2.CDriverBase_SetMarkerCustomMeshVelocity(self, iMarker, iVertex, values)

    def CommunicateMeshDisplacements(self):
        r"""CommunicateMeshDisplacements(CDriverBase self)"""
        return _pysu2.CDriverBase_CommunicateMeshDisplacements(self)

    def GetSolverIndices(self):
        r"""GetSolverIndices(CDriverBase self) -> map< string,unsigned short >"""
        return _pysu2.CDriverBase_GetSolverIndices(self)

    def GetFEASolutionIndices(self):
        r"""GetFEASolutionIndices(CDriverBase self) -> map< string,unsigned short >"""
        return _pysu2.CDriverBase_GetFEASolutionIndices(self)

    def Solution(self, iSolver):
        r"""Solution(CDriverBase self, unsigned short iSolver) -> CPyWrapperMatrixView"""
        return _pysu2.CDriverBase_Solution(self, iSolver)

    def MarkerSolution(self, iSolver, iMarker):
        r"""MarkerSolution(CDriverBase self, unsigned short iSolver, unsigned short iMarker) -> CPyWrapperMarkerMatrixView"""
        return _pysu2.CDriverBase_MarkerSolution(self, iSolver, iMarker)

    def SolutionTimeN(self, iSolver):
        r"""SolutionTimeN(CDriverBase self, unsigned short iSolver) -> CPyWrapperMatrixView"""
        return _pysu2.CDriverBase_SolutionTimeN(self, iSolver)

    def MarkerSolutionTimeN(self, iSolver, iMarker):
        r"""MarkerSolutionTimeN(CDriverBase self, unsigned short iSolver, unsigned short iMarker) -> CPyWrapperMarkerMatrixView"""
        return _pysu2.CDriverBase_MarkerSolutionTimeN(self, iSolver, iMarker)

    def SolutionTimeN1(self, iSolver):
        r"""SolutionTimeN1(CDriverBase self, unsigned short iSolver) -> CPyWrapperMatrixView"""
        return _pysu2.CDriverBase_SolutionTimeN1(self, iSolver)

    def MarkerSolutionTimeN1(self, iSolver, iMarker):
        r"""MarkerSolutionTimeN1(CDriverBase self, unsigned short iSolver, unsigned short iMarker) -> CPyWrapperMarkerMatrixView"""
        return _pysu2.CDriverBase_MarkerSolutionTimeN1(self, iSolver, iMarker)

    def GetPrimitiveIndices(self):
        r"""GetPrimitiveIndices(CDriverBase self) -> map< string,unsigned short >"""
        return _pysu2.CDriverBase_GetPrimitiveIndices(self)

    def Primitives(self):
        r"""Primitives(CDriverBase self) -> CPyWrapperMatrixView"""
        return _pysu2.CDriverBase_Primitives(self)

    def MarkerPrimitives(self, iMarker):
        r"""MarkerPrimitives(CDriverBase self, unsigned short iMarker) -> CPyWrapperMarkerMatrixView"""
        return _pysu2.CDriverBase_MarkerPrimitives(self, iMarker)

    def Sensitivity(self, iSolver):
        r"""Sensitivity(CDriverBase self, unsigned short iSolver) -> CPyWrapperMatrixView"""
        return _pysu2.CDriverBase_Sensitivity(self, iSolver)

    def SetMarkerCustomTemperature(self, iMarker, iVertex, WallTemp):
        r"""SetMarkerCustomTemperature(CDriverBase self, unsigned short iMarker, unsigned long iVertex, passivedouble WallTemp)"""
        return _pysu2.CDriverBase_SetMarkerCustomTemperature(self, iMarker, iVertex, WallTemp)

    def SetMarkerCustomNormalHeatFlux(self, iMarker, iVertex, WallHeatFlux):
        r"""SetMarkerCustomNormalHeatFlux(CDriverBase self, unsigned short iMarker, unsigned long iVertex, passivedouble WallHeatFlux)"""
        return _pysu2.CDriverBase_SetMarkerCustomNormalHeatFlux(self, iMarker, iVertex, WallHeatFlux)

    def SelectZone(self, iZone):
        r"""SelectZone(CDriverBase self, unsigned short iZone)"""
        return _pysu2.CDriverBase_SelectZone(self, iZone)

    def SelectedZone(self):
        r"""SelectedZone(CDriverBase self) -> unsigned short"""
        return _pysu2.CDriverBase_SelectedZone(self)

    def GetMarkerNormalHeatFlux(self, iSolver, iMarker, iVertex):
        r"""GetMarkerNormalHeatFlux(CDriverBase self, unsigned short iSolver, unsigned short iMarker, unsigned long iVertex) -> passivedouble"""
        return _pysu2.CDriverBase_GetMarkerNormalHeatFlux(self, iSolver, iMarker, iVertex)

    def SetMarkerCustomFEALoad(self, iMarker, iVertex, force):
        r"""SetMarkerCustomFEALoad(CDriverBase self, unsigned short iMarker, unsigned long iVertex, std::vector< passivedouble,std::allocator< passivedouble > > force)"""
        return _pysu2.CDriverBase_SetMarkerCustomFEALoad(self, iMarker, iVertex, force)

    def GetMarkerFlowLoad(self, iMarker, iVertex):
        r"""GetMarkerFlowLoad(CDriverBase self, unsigned short iMarker, unsigned long iVertex) -> vector< passivedouble >"""
        return _pysu2.CDriverBase_GetMarkerFlowLoad(self, iMarker, iVertex)

    def SetMarkerCustomFlowLoadAdjoint(self, iMarker, iVertex, adjointLoad):
        r"""SetMarkerCustomFlowLoadAdjoint(CDriverBase self, unsigned short iMarker, unsigned long iVertex, vector< passivedouble > adjointLoad)"""
        return _pysu2.CDriverBase_SetMarkerCustomFlowLoadAdjoint(self, iMarker, iVertex, adjointLoad)

    def GetMarkerDisplacementSensitivity(self, iMarker, iVertex):
        r"""GetMarkerDisplacementSensitivity(CDriverBase self, unsigned short iMarker, unsigned long iVertex) -> vector< passivedouble >"""
        return _pysu2.CDriverBase_GetMarkerDisplacementSensitivity(self, iMarker, iVertex)

    def GetMarkerFEALoadSensitivity(self, iMarker, iVertex):
        r"""GetMarkerFEALoadSensitivity(CDriverBase self, unsigned short iMarker, unsigned long iVertex) -> vector< passivedouble >"""
        return _pysu2.CDriverBase_GetMarkerFEALoadSensitivity(self, iMarker, iVertex)

    def SetMarkerCustomFEADisplacementAdjoint(self, iMarker, iVertex, adjointDisplacement):
        r"""SetMarkerCustomFEADisplacementAdjoint(CDriverBase self, unsigned short iMarker, unsigned long iVertex, vector< passivedouble > adjointDisplacement)"""
        return _pysu2.CDriverBase_SetMarkerCustomFEADisplacementAdjoint(self, iMarker, iVertex, adjointDisplacement)

    def SetMarkerCustomFEAVelocityAdjoint(self, iMarker, iVertex, adjointVelocity):
        r"""SetMarkerCustomFEAVelocityAdjoint(CDriverBase self, unsigned short iMarker, unsigned long iVertex, vector< passivedouble > adjointVelocity)"""
        return _pysu2.CDriverBase_SetMarkerCustomFEAVelocityAdjoint(self, iMarker, iVertex, adjointVelocity)

# Register CDriverBase in _pysu2:
_pysu2.CDriverBase_swigregister(CDriverBase)

class CDriver(CDriverBase):
    r"""Proxy of C++ CDriver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator, dummy_geo):
        r"""__init__(CDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator, bool dummy_geo) -> CDriver"""
        _pysu2.CDriver_swiginit(self, _pysu2.new_CDriver(confFile, val_nZone, MPICommunicator, dummy_geo))
    __swig_destroy__ = _pysu2.delete_CDriver

    def Run(self):
        r"""Run(CDriver self)"""
        return _pysu2.CDriver_Run(self)

    def StartSolver(self):
        r"""StartSolver(CDriver self)"""
        return _pysu2.CDriver_StartSolver(self)

    def Finalize(self):
        r"""Finalize(CDriver self)"""
        return _pysu2.CDriver_Finalize(self)

    def Preprocess(self, TimeIter):
        r"""Preprocess(CDriver self, unsigned long TimeIter)"""
        return _pysu2.CDriver_Preprocess(self, TimeIter)

    def Monitor(self, TimeIter):
        r"""Monitor(CDriver self, unsigned long TimeIter) -> bool"""
        return _pysu2.CDriver_Monitor(self, TimeIter)

    def Output(self, TimeIter):
        r"""Output(CDriver self, unsigned long TimeIter)"""
        return _pysu2.CDriver_Output(self, TimeIter)

    def DynamicMeshUpdate(self, TimeIter):
        r"""DynamicMeshUpdate(CDriver self, unsigned long TimeIter)"""
        return _pysu2.CDriver_DynamicMeshUpdate(self, TimeIter)

    def Update(self):
        r"""Update(CDriver self)"""
        return _pysu2.CDriver_Update(self)

    def SetInitialMesh(self):
        r"""SetInitialMesh(CDriver self)"""
        return _pysu2.CDriver_SetInitialMesh(self)

    def BoundaryConditionsUpdate(self):
        r"""BoundaryConditionsUpdate(CDriver self)"""
        return _pysu2.CDriver_BoundaryConditionsUpdate(self)

    def GetNumberTimeIter(self):
        r"""GetNumberTimeIter(CDriver self) -> unsigned long"""
        return _pysu2.CDriver_GetNumberTimeIter(self)

    def GetTimeIter(self):
        r"""GetTimeIter(CDriver self) -> unsigned long"""
        return _pysu2.CDriver_GetTimeIter(self)

    def GetUnsteadyTimeStep(self):
        r"""GetUnsteadyTimeStep(CDriver self) -> passivedouble"""
        return _pysu2.CDriver_GetUnsteadyTimeStep(self)

    def GetSurfaceFileName(self):
        r"""GetSurfaceFileName(CDriver self) -> std::string"""
        return _pysu2.CDriver_GetSurfaceFileName(self)

    def SetHeatSourcePosition(self, alpha, pos_x, pos_y, pos_z):
        r"""SetHeatSourcePosition(CDriver self, passivedouble alpha, passivedouble pos_x, passivedouble pos_y, passivedouble pos_z)"""
        return _pysu2.CDriver_SetHeatSourcePosition(self, alpha, pos_x, pos_y, pos_z)

    def SetInletAngle(self, iMarker, alpha):
        r"""SetInletAngle(CDriver self, unsigned short iMarker, passivedouble alpha)"""
        return _pysu2.CDriver_SetInletAngle(self, iMarker, alpha)

    def SetFarFieldAoA(self, alpha):
        r"""SetFarFieldAoA(CDriver self, passivedouble alpha)"""
        return _pysu2.CDriver_SetFarFieldAoA(self, alpha)

    def SetFarFieldAoS(self, beta):
        r"""SetFarFieldAoS(CDriver self, passivedouble beta)"""
        return _pysu2.CDriver_SetFarFieldAoS(self, beta)

    def SetTranslationRate(self, xDot, yDot, zDot):
        r"""SetTranslationRate(CDriver self, passivedouble xDot, passivedouble yDot, passivedouble zDot)"""
        return _pysu2.CDriver_SetTranslationRate(self, xDot, yDot, zDot)

    def SetRotationRate(self, rot_x, rot_y, rot_z):
        r"""SetRotationRate(CDriver self, passivedouble rot_x, passivedouble rot_y, passivedouble rot_z)"""
        return _pysu2.CDriver_SetRotationRate(self, rot_x, rot_y, rot_z)

    def SetMarkerRotationRate(self, iMarker, rot_x, rot_y, rot_z):
        r"""SetMarkerRotationRate(CDriver self, unsigned short iMarker, passivedouble rot_x, passivedouble rot_y, passivedouble rot_z)"""
        return _pysu2.CDriver_SetMarkerRotationRate(self, iMarker, rot_x, rot_y, rot_z)

    def SetMarkerTranslationRate(self, iMarker, vel_x, vel_y, vel_z):
        r"""SetMarkerTranslationRate(CDriver self, unsigned short iMarker, passivedouble vel_x, passivedouble vel_y, passivedouble vel_z)"""
        return _pysu2.CDriver_SetMarkerTranslationRate(self, iMarker, vel_x, vel_y, vel_z)

# Register CDriver in _pysu2:
_pysu2.CDriver_swigregister(CDriver)

class CFluidDriver(CDriver):
    r"""Proxy of C++ CFluidDriver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _pysu2.delete_CFluidDriver

    def StartSolver(self):
        r"""StartSolver(CFluidDriver self)"""
        return _pysu2.CFluidDriver_StartSolver(self)

    def Run(self):
        r"""Run(CFluidDriver self)"""
        return _pysu2.CFluidDriver_Run(self)

    def Update(self):
        r"""Update(CFluidDriver self)"""
        return _pysu2.CFluidDriver_Update(self)

    def Output(self, InnerIter):
        r"""Output(CFluidDriver self, unsigned long InnerIter)"""
        return _pysu2.CFluidDriver_Output(self, InnerIter)

    def Monitor(self, ExtIter):
        r"""Monitor(CFluidDriver self, unsigned long ExtIter) -> bool"""
        return _pysu2.CFluidDriver_Monitor(self, ExtIter)

    def Preprocess(self, Iter):
        r"""Preprocess(CFluidDriver self, unsigned long Iter)"""
        return _pysu2.CFluidDriver_Preprocess(self, Iter)

    def DynamicMeshUpdate(self, TimeIter):
        r"""DynamicMeshUpdate(CFluidDriver self, unsigned long TimeIter)"""
        return _pysu2.CFluidDriver_DynamicMeshUpdate(self, TimeIter)

# Register CFluidDriver in _pysu2:
_pysu2.CFluidDriver_swigregister(CFluidDriver)

class CHBDriver(CFluidDriver):
    r"""Proxy of C++ CHBDriver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        r"""__init__(CHBDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CHBDriver"""
        _pysu2.CHBDriver_swiginit(self, _pysu2.new_CHBDriver(confFile, val_nZone, MPICommunicator))
    __swig_destroy__ = _pysu2.delete_CHBDriver

    def Run(self):
        r"""Run(CHBDriver self)"""
        return _pysu2.CHBDriver_Run(self)

    def Update(self):
        r"""Update(CHBDriver self)"""
        return _pysu2.CHBDriver_Update(self)

# Register CHBDriver in _pysu2:
_pysu2.CHBDriver_swigregister(CHBDriver)

class CSinglezoneDriver(CDriver):
    r"""Proxy of C++ CSinglezoneDriver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        r"""__init__(CSinglezoneDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CSinglezoneDriver"""
        _pysu2.CSinglezoneDriver_swiginit(self, _pysu2.new_CSinglezoneDriver(confFile, val_nZone, MPICommunicator))
    __swig_destroy__ = _pysu2.delete_CSinglezoneDriver

    def StartSolver(self):
        r"""StartSolver(CSinglezoneDriver self)"""
        return _pysu2.CSinglezoneDriver_StartSolver(self)

    def Preprocess(self, TimeIter):
        r"""Preprocess(CSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2.CSinglezoneDriver_Preprocess(self, TimeIter)

    def Run(self):
        r"""Run(CSinglezoneDriver self)"""
        return _pysu2.CSinglezoneDriver_Run(self)

    def Postprocess(self):
        r"""Postprocess(CSinglezoneDriver self)"""
        return _pysu2.CSinglezoneDriver_Postprocess(self)

    def Update(self):
        r"""Update(CSinglezoneDriver self)"""
        return _pysu2.CSinglezoneDriver_Update(self)

    def Output(self, TimeIter):
        r"""Output(CSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2.CSinglezoneDriver_Output(self, TimeIter)

    def DynamicMeshUpdate(self, TimeIter):
        r"""DynamicMeshUpdate(CSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2.CSinglezoneDriver_DynamicMeshUpdate(self, TimeIter)

    def SetInitialMesh(self):
        r"""SetInitialMesh(CSinglezoneDriver self)"""
        return _pysu2.CSinglezoneDriver_SetInitialMesh(self)

    def Monitor(self, TimeIter):
        r"""Monitor(CSinglezoneDriver self, unsigned long TimeIter) -> bool"""
        return _pysu2.CSinglezoneDriver_Monitor(self, TimeIter)

# Register CSinglezoneDriver in _pysu2:
_pysu2.CSinglezoneDriver_swigregister(CSinglezoneDriver)

class CMultizoneDriver(CDriver):
    r"""Proxy of C++ CMultizoneDriver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        r"""__init__(CMultizoneDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CMultizoneDriver"""
        _pysu2.CMultizoneDriver_swiginit(self, _pysu2.new_CMultizoneDriver(confFile, val_nZone, MPICommunicator))
    __swig_destroy__ = _pysu2.delete_CMultizoneDriver

    def StartSolver(self):
        r"""StartSolver(CMultizoneDriver self)"""
        return _pysu2.CMultizoneDriver_StartSolver(self)

    def Preprocess(self, TimeIter):
        r"""Preprocess(CMultizoneDriver self, unsigned long TimeIter)"""
        return _pysu2.CMultizoneDriver_Preprocess(self, TimeIter)

    def Run(self):
        r"""Run(CMultizoneDriver self)"""
        return _pysu2.CMultizoneDriver_Run(self)

    def Postprocess(self):
        r"""Postprocess(CMultizoneDriver self)"""
        return _pysu2.CMultizoneDriver_Postprocess(self)

    def Update(self):
        r"""Update(CMultizoneDriver self)"""
        return _pysu2.CMultizoneDriver_Update(self)

    def Output(self, TimeIter):
        r"""Output(CMultizoneDriver self, unsigned long TimeIter)"""
        return _pysu2.CMultizoneDriver_Output(self, TimeIter)

    def DynamicMeshUpdate(self, TimeIter):
        r"""DynamicMeshUpdate(CMultizoneDriver self, unsigned long TimeIter)"""
        return _pysu2.CMultizoneDriver_DynamicMeshUpdate(self, TimeIter)

    def Monitor(self, TimeIter):
        r"""Monitor(CMultizoneDriver self, unsigned long TimeIter) -> bool"""
        return _pysu2.CMultizoneDriver_Monitor(self, TimeIter)

# Register CMultizoneDriver in _pysu2:
_pysu2.CMultizoneDriver_swigregister(CMultizoneDriver)

class CDiscAdjSinglezoneDriver(CSinglezoneDriver):
    r"""Proxy of C++ CDiscAdjSinglezoneDriver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, confFile, val_nZone, MPICommunicator):
        r"""__init__(CDiscAdjSinglezoneDriver self, char * confFile, unsigned short val_nZone, SU2_Comm MPICommunicator) -> CDiscAdjSinglezoneDriver"""
        _pysu2.CDiscAdjSinglezoneDriver_swiginit(self, _pysu2.new_CDiscAdjSinglezoneDriver(confFile, val_nZone, MPICommunicator))
    __swig_destroy__ = _pysu2.delete_CDiscAdjSinglezoneDriver

    def Preprocess(self, TimeIter):
        r"""Preprocess(CDiscAdjSinglezoneDriver self, unsigned long TimeIter)"""
        return _pysu2.CDiscAdjSinglezoneDriver_Preprocess(self, TimeIter)

    def Run(self):
        r"""Run(CDiscAdjSinglezoneDriver self)"""
        return _pysu2.CDiscAdjSinglezoneDriver_Run(self)

    def Postprocess(self):
        r"""Postprocess(CDiscAdjSinglezoneDriver self)"""
        return _pysu2.CDiscAdjSinglezoneDriver_Postprocess(self)

# Register CDiscAdjSinglezoneDriver in _pysu2:
_pysu2.CDiscAdjSinglezoneDriver_swigregister(CDiscAdjSinglezoneDriver)

class CDeformationDriver(CDriverBase):
    r"""Proxy of C++ CDeformationDriver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, confFile, MPICommunicator):
        r"""__init__(CDeformationDriver self, char * confFile, SU2_Comm MPICommunicator) -> CDeformationDriver"""
        _pysu2.CDeformationDriver_swiginit(self, _pysu2.new_CDeformationDriver(confFile, MPICommunicator))

    def Run(self):
        r"""Run(CDeformationDriver self)"""
        return _pysu2.CDeformationDriver_Run(self)

    def Finalize(self):
        r"""Finalize(CDeformationDriver self)"""
        return _pysu2.CDeformationDriver_Finalize(self)
    __swig_destroy__ = _pysu2.delete_CDeformationDriver

# Register CDeformationDriver in _pysu2:
_pysu2.CDeformationDriver_swigregister(CDeformationDriver)




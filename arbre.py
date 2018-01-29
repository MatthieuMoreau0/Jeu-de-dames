# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_arbre')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_arbre')
    _arbre = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_arbre', [dirname(__file__)])
        except ImportError:
            import _arbre
            return _arbre
        try:
            _mod = imp.load_module('_arbre', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _arbre = swig_import_helper()
    del swig_import_helper
else:
    import _arbre
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _arbre.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _arbre.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _arbre.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _arbre.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _arbre.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _arbre.SwigPyIterator_equal(self, x)

    def copy(self):
        return _arbre.SwigPyIterator_copy(self)

    def next(self):
        return _arbre.SwigPyIterator_next(self)

    def __next__(self):
        return _arbre.SwigPyIterator___next__(self)

    def previous(self):
        return _arbre.SwigPyIterator_previous(self)

    def advance(self, n):
        return _arbre.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _arbre.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _arbre.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _arbre.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _arbre.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _arbre.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _arbre.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _arbre.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Piece(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Piece, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Piece, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _arbre.delete_Piece
    __del__ = lambda self: None

    def getPosition(self):
        return _arbre.Piece_getPosition(self)

    def setPosition(self, arg2):
        return _arbre.Piece_setPosition(self, arg2)

    def Color(self):
        return _arbre.Piece_Color(self)

    def isMan(self):
        return _arbre.Piece_isMan(self)

    def isKing(self):
        return _arbre.Piece_isKing(self)

    def killFreeMove(self, arg2, arg3):
        return _arbre.Piece_killFreeMove(self, arg2, arg3)

    def killingMove(self, arg2, arg3):
        return _arbre.Piece_killingMove(self, arg2, arg3)

    def select(self, arg2, arg3):
        return _arbre.Piece_select(self, arg2, arg3)

    def clone(self):
        return _arbre.Piece_clone(self)
Piece_swigregister = _arbre.Piece_swigregister
Piece_swigregister(Piece)

class Man(Piece):
    __swig_setmethods__ = {}
    for _s in [Piece]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Man, name, value)
    __swig_getmethods__ = {}
    for _s in [Piece]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Man, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _arbre.delete_Man
    __del__ = lambda self: None

    def isMan(self):
        return _arbre.Man_isMan(self)

    def killFreeMove(self, arg2, arg3):
        return _arbre.Man_killFreeMove(self, arg2, arg3)

    def killingMove(self, arg2, arg3):
        return _arbre.Man_killingMove(self, arg2, arg3)

    def select(self, arg2, arg3):
        return _arbre.Man_select(self, arg2, arg3)

    def clone(self):
        return _arbre.Man_clone(self)
Man_swigregister = _arbre.Man_swigregister
Man_swigregister(Man)

class Move(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Move, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Move, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _arbre.new_Move(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __lt__(self, arg2):
        return _arbre.Move___lt__(self, arg2)

    def getStart(self):
        return _arbre.Move_getStart(self)

    def getArrival(self):
        return _arbre.Move_getArrival(self)

    def getKills(self):
        return _arbre.Move_getKills(self)

    def getPath(self):
        return _arbre.Move_getPath(self)

    def extendMove(self, arg2):
        return _arbre.Move_extendMove(self, arg2)
    __swig_destroy__ = _arbre.delete_Move
    __del__ = lambda self: None
Move_swigregister = _arbre.Move_swigregister
Move_swigregister(Move)

class Board(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Board, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Board, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _arbre.new_Board(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def index_man_here(self, arg2):
        return _arbre.Board_index_man_here(self, arg2)

    def isManHere(self, arg2):
        return _arbre.Board_isManHere(self, arg2)

    def isKingHere(self, arg2):
        return _arbre.Board_isKingHere(self, arg2)

    def isPieceHere(self, arg2):
        return _arbre.Board_isPieceHere(self, arg2)

    def playMove(self, arg2, arg3):
        return _arbre.Board_playMove(self, arg2, arg3)

    def killAt(self, arg2):
        return _arbre.Board_killAt(self, arg2)

    def getPiece(self, arg2):
        return _arbre.Board_getPiece(self, arg2)

    def nbPieces(self):
        return _arbre.Board_nbPieces(self)

    def playableMoves(self, arg2):
        return _arbre.Board_playableMoves(self, arg2)

    def evaluate(self, arg2, arg3, arg4):
        return _arbre.Board_evaluate(self, arg2, arg3, arg4)

    def bestMove(self, arg2, arg3, arg4, arg5):
        return _arbre.Board_bestMove(self, arg2, arg3, arg4, arg5)

    def bestMoveAlphaBeta(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        return _arbre.Board_bestMoveAlphaBeta(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    def endGame(self):
        return _arbre.Board_endGame(self)
    __swig_destroy__ = _arbre.delete_Board
    __del__ = lambda self: None
Board_swigregister = _arbre.Board_swigregister
Board_swigregister(Board)

class King(Piece):
    __swig_setmethods__ = {}
    for _s in [Piece]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, King, name, value)
    __swig_getmethods__ = {}
    for _s in [Piece]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, King, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _arbre.delete_King
    __del__ = lambda self: None

    def isMan(self):
        return _arbre.King_isMan(self)

    def killFreeMove(self, arg2, arg3):
        return _arbre.King_killFreeMove(self, arg2, arg3)

    def killingMove(self, arg2, arg3):
        return _arbre.King_killingMove(self, arg2, arg3)

    def select(self, arg2, arg3):
        return _arbre.King_select(self, arg2, arg3)

    def clone(self):
        return _arbre.King_clone(self)
King_swigregister = _arbre.King_swigregister
King_swigregister(King)


def Test(A):
    return _arbre.Test(A)
Test = _arbre.Test
class VectorMove(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorMove, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorMove, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _arbre.VectorMove_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _arbre.VectorMove___nonzero__(self)

    def __bool__(self):
        return _arbre.VectorMove___bool__(self)

    def __len__(self):
        return _arbre.VectorMove___len__(self)

    def __getslice__(self, i, j):
        return _arbre.VectorMove___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _arbre.VectorMove___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _arbre.VectorMove___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _arbre.VectorMove___delitem__(self, *args)

    def __getitem__(self, *args):
        return _arbre.VectorMove___getitem__(self, *args)

    def __setitem__(self, *args):
        return _arbre.VectorMove___setitem__(self, *args)

    def pop(self):
        return _arbre.VectorMove_pop(self)

    def append(self, x):
        return _arbre.VectorMove_append(self, x)

    def empty(self):
        return _arbre.VectorMove_empty(self)

    def size(self):
        return _arbre.VectorMove_size(self)

    def swap(self, v):
        return _arbre.VectorMove_swap(self, v)

    def begin(self):
        return _arbre.VectorMove_begin(self)

    def end(self):
        return _arbre.VectorMove_end(self)

    def rbegin(self):
        return _arbre.VectorMove_rbegin(self)

    def rend(self):
        return _arbre.VectorMove_rend(self)

    def clear(self):
        return _arbre.VectorMove_clear(self)

    def get_allocator(self):
        return _arbre.VectorMove_get_allocator(self)

    def pop_back(self):
        return _arbre.VectorMove_pop_back(self)

    def erase(self, *args):
        return _arbre.VectorMove_erase(self, *args)

    def __init__(self, *args):
        this = _arbre.new_VectorMove(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _arbre.VectorMove_push_back(self, x)

    def front(self):
        return _arbre.VectorMove_front(self)

    def back(self):
        return _arbre.VectorMove_back(self)

    def assign(self, n, x):
        return _arbre.VectorMove_assign(self, n, x)

    def resize(self, *args):
        return _arbre.VectorMove_resize(self, *args)

    def insert(self, *args):
        return _arbre.VectorMove_insert(self, *args)

    def reserve(self, n):
        return _arbre.VectorMove_reserve(self, n)

    def capacity(self):
        return _arbre.VectorMove_capacity(self)
    __swig_destroy__ = _arbre.delete_VectorMove
    __del__ = lambda self: None
VectorMove_swigregister = _arbre.VectorMove_swigregister
VectorMove_swigregister(VectorMove)

class map_int_moves(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_int_moves, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_int_moves, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _arbre.map_int_moves_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _arbre.map_int_moves___nonzero__(self)

    def __bool__(self):
        return _arbre.map_int_moves___bool__(self)

    def __len__(self):
        return _arbre.map_int_moves___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _arbre.map_int_moves___getitem__(self, key)

    def __delitem__(self, key):
        return _arbre.map_int_moves___delitem__(self, key)

    def has_key(self, key):
        return _arbre.map_int_moves_has_key(self, key)

    def keys(self):
        return _arbre.map_int_moves_keys(self)

    def values(self):
        return _arbre.map_int_moves_values(self)

    def items(self):
        return _arbre.map_int_moves_items(self)

    def __contains__(self, key):
        return _arbre.map_int_moves___contains__(self, key)

    def key_iterator(self):
        return _arbre.map_int_moves_key_iterator(self)

    def value_iterator(self):
        return _arbre.map_int_moves_value_iterator(self)

    def __setitem__(self, *args):
        return _arbre.map_int_moves___setitem__(self, *args)

    def asdict(self):
        return _arbre.map_int_moves_asdict(self)

    def __init__(self, *args):
        this = _arbre.new_map_int_moves(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _arbre.map_int_moves_empty(self)

    def size(self):
        return _arbre.map_int_moves_size(self)

    def swap(self, v):
        return _arbre.map_int_moves_swap(self, v)

    def begin(self):
        return _arbre.map_int_moves_begin(self)

    def end(self):
        return _arbre.map_int_moves_end(self)

    def rbegin(self):
        return _arbre.map_int_moves_rbegin(self)

    def rend(self):
        return _arbre.map_int_moves_rend(self)

    def clear(self):
        return _arbre.map_int_moves_clear(self)

    def get_allocator(self):
        return _arbre.map_int_moves_get_allocator(self)

    def count(self, x):
        return _arbre.map_int_moves_count(self, x)

    def erase(self, *args):
        return _arbre.map_int_moves_erase(self, *args)

    def find(self, x):
        return _arbre.map_int_moves_find(self, x)

    def lower_bound(self, x):
        return _arbre.map_int_moves_lower_bound(self, x)

    def upper_bound(self, x):
        return _arbre.map_int_moves_upper_bound(self, x)
    __swig_destroy__ = _arbre.delete_map_int_moves
    __del__ = lambda self: None
map_int_moves_swigregister = _arbre.map_int_moves_swigregister
map_int_moves_swigregister(map_int_moves)

class pair_float_moves(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pair_float_moves, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pair_float_moves, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _arbre.new_pair_float_moves(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["first"] = _arbre.pair_float_moves_first_set
    __swig_getmethods__["first"] = _arbre.pair_float_moves_first_get
    if _newclass:
        first = _swig_property(_arbre.pair_float_moves_first_get, _arbre.pair_float_moves_first_set)
    __swig_setmethods__["second"] = _arbre.pair_float_moves_second_set
    __swig_getmethods__["second"] = _arbre.pair_float_moves_second_get
    if _newclass:
        second = _swig_property(_arbre.pair_float_moves_second_get, _arbre.pair_float_moves_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _arbre.delete_pair_float_moves
    __del__ = lambda self: None
pair_float_moves_swigregister = _arbre.pair_float_moves_swigregister
pair_float_moves_swigregister(pair_float_moves)

# This file is compatible with both classic and new-style classes.



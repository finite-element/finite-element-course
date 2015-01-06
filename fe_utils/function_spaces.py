
class FunctionSpace(object):

    def __init__(self, mesh, element):
        """A finite element space. 
        
        :param mesh: The :class:`~.mesh.Mesh` on which this space is built.
        :param element: The :class:`~.finite_elements.FiniteElement` of this space.

        Most of the implementation of this class is left as an :ref:`exercise
        <ex-function_space>`.
        """
        self.mesh = mesh
        self.element = mesh
        
        raise NotImplementedError

        # Implement global numbering in order to produce the global
        # cell node list for this space.
        #: The global cell node list. This is a two-dimensional in which each row
        #: lists the global nodes incident to the corresponding cell.
        self.cell_nodes = None

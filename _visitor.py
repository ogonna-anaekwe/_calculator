from abc import ABC
from abc import abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_binary_expr(self, Binary):
        raise NotImplementedError

    @abstractmethod
    def visit_literal_expr(self, Literal):
        raise NotImplementedError

    @abstractmethod
    def visit_group_expr(self, Group):
        raise NotImplementedError

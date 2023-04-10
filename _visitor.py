from abc import ABC
from abc import abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_binary_expr(self):
        raise NotImplementedError

    @abstractmethod
    def visit_literal_expr(self):
        raise NotImplementedError

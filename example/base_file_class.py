from abc import ABC, abstractmethod


class BaseFileClass(ABC):

  @abstractmethod
  def do_something_file(self):
    pass


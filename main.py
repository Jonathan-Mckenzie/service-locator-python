from abc import ABC, abstractmethod
from service_locator import ServiceLocator
from base_file_class import BaseFileClass
from sub_file_class_a import SubFileClassA
from sub_file_class_b import SubFileClassB


# Define some interface for subclasses to provide an implementation for
class BaseClass(ABC):

  @abstractmethod
  def do_something(self):
    pass


# This can switch at runtime to inject
USE_CLASS_A: bool = True

# Inject only one subclass:

# Conditionally define one subclass
if USE_CLASS_A is True:

  class SubClassA(BaseClass):

    def do_something(self):
      print("SubClassA: Doing something...")
else:

  class SubClassB(BaseClass):

    def do_something(self):
      print("SubClassB: Doing something...")


# experiments:
service_locator = ServiceLocator()

# should resolve SubClassA given the BaseClass "interface"
service_locator.get_service(BaseClass).do_something()

# instead of resolving by subclass definitions, explicitly register an interface with a concrete implementation
service_locator.register_service(BaseFileClass, SubFileClassB)
baseFileClassImpl = service_locator.get_service(BaseFileClass)
baseFileClassImpl.do_something_file()


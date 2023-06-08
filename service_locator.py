class ServiceLocator:

  def __init__(self) -> None:
    self.__service_map = {}

  def get_service(self, interface):

    if interface in self.__service_map:
      # service already registered
      return self.__service_map[interface]

    # subclass definition search
    subclasses = interface.__subclasses__()
    if len(subclasses) == 0:
      raise ValueError("No subclasses found for the given base class.")

    if len(subclasses) != 1:
      raise ValueError(
        "More than one subclass found for the given base class.")

    implementation = subclasses[0]

    # lazy register and load on discovery
    self.__service_map[interface] = implementation()
    return self.__service_map[interface]

  def register_service(self, interface, implementation):
    # register and load
    # note: allows overriding previously registered subclasses
    self.__service_map[interface] = implementation()


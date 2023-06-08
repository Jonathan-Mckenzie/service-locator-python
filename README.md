# Service Locator Python

Proof of concept by implementing the [Service Locator Pattern](https://en.wikipedia.org/wiki/Service_locator_pattern) using [Abstract Base Class](https://docs.python.org/3/library/abc.html) in Python

The goal is to have a single service that provides the implementation of any specified interface.

## Example

```python
from abc import ABC, abstractmethod

class AuthInterface(ABC):
  @abstractmethod
  def verify(self):
    pass

class AuthInterface(ABC):
  @abstractmethod
  def verify(self):
    pass

class OAuth2(AuthInterface):
  def verify(self):
    print("verifying auth w/ oauth2 protocol...")

# instantiate service locator
service_locator = ServiceLocator()

# register auth to be performed by OAuth2
service_locator.register_service(AuthInterface, OAuth2)

# get the auth implementation
auth_service = service_locator.get_service(AuthInterface)

# execute provided implementation
auth_service.verify()
```

### Note
Although it supports the __subclass__ search of a given interface, I find it more effectively to explicitly register the implementations at runtime.

# vboxwebber
The purpose of this project is to provide a <b>Python3</b> client for the VirtualBox remote <b>webservices</b> API. It is standalone in the way that it does not depend on the python libraries distributed with VirtualBox SDK (which to date only supports Python2 via the ancient ZSI library).

The client is generated from an XSL stylesheet and contains vbox API wrapper functions that uses zeep as SOAP-library under the hood for remote access.

The XSL stylesheet is based on the websrv-python.xsl file from the VirtualBox source package, but somewhat improved and modified to use zeep instead of ZSI. Documentation for classes and methods are also generated, hopefully removing the need of sitting with the SDK reference alongside when coding.

## Installation
```
pip install vboxwebber
```

## Usage
Initialize a web session manager by specifying the URL for the VirtualBox web service, and optionally the URL for the wsdl file. For older web services, I didn't manage to get the remote server's wsdl file, so it can be specified as a local file, e.g. "file:///tmp/vboxweb.wsdl".

The service and interface methods should be the same as when using the official SDK, so porting old code should be easy. Classes are generated for enums etc., but it is recommended to combine with the VirtualBox_constants.py from the SDK (which is also generated from the constants-python.xsl stylesheet - encorporating this into the same file is a TODO).

```python
from vboxwebber import *

# Initiate the client
mgr = IWebsessionManager2("http://localhost:18083")

# Logon, get the IVirtualBox object
vbox = mgr.logon("username", "password")

# Print API version
print(vbox.getAPIVersion())

# Find machine
machine = vbox.findMachine("kali2019.4")

# Get the session object
session =  mgr.getSessionObject(vbox)

# Lock the machine to the session
machine.lockMachine(session, SessionType.WriteLock)

# Get the display
display = session.console.display

# Get screen resolution info
width, height, _bpp, _xo, _yo, _status = display.getScreenResolution(0)

# Take a screenshot
screenshot = display.takeScreenShotToArray(0, width, height, "PNG")

# Write data to file
with open("/tmp/screenshot.png", "wb") as f:
    f.write(screenshot)

# Log off, cleaning up resources (implicit, at least for newer vbox versions)
mgr.logoff(vbox)
```

## Generating new API wrappers
The VirtualBox API doesn't change much, but should the need arise, it is easy to generate a new wrapper based on a specific VirtualBox release. Just download the VirtualBox source code package, put the xsl stylesheet in src/VBox/Main/webservice and run:
```
xsltproc websrv-zeep.xsl ../idl/VirtualBox.xidl > vboxwebber.py
```

## TODO's
  * Conditionalize the generation of documentation?
  * Modify the VirtualBox glue code to include this as a platform?
  * Generate even better documentation with docstring syntax etc.
    
## Help
Improvements are welcome.

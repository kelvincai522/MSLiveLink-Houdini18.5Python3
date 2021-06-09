# MSLiveLink-Houdini18.5Python3
Houdini 18.5 Python 3 Megascan Bridge LiveLink

Since Houdini 18.5 (and Python 3) is not officially supported by Quixel, I have modified the official MSLiveLink v4.4 to be able to run inside Houdini 18.5 Python 3.

Currently, I only tested it to load 3d assets for Mantra successfully, but nothing else.  There might be other Python 3 modifications that I missed.  Please report if any issues.

The Python 3 modifications are the following:

1.  Updated all implicit modules import to explicit
```python
from Utilities.SettingsManager import SettingsManager
```
--->
```python
from .Utilities.SettingsManager import SettingsManager
```
<p>&nbsp;</p>

2.  Updated all metaclass declaration
```python
class SettingsManager:
      __metaclass__ = Singleton 
```
--->
```python
class SettingsManager(metaclass = Singleton):
```
<p>&nbsp;</p>

3.  Updated SocketListener.py to emit string instead of bytes
```python
self.Bridge_Call.emit(self.TotalData)
```
--->
```pyton
self.Bridge_Call.emit(self.TotalData.decode('UTF-8')
```

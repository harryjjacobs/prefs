# prefs
Simple python module for storing user preferences.

Usage example:
```python
>>> import prefs
>>> prefs.add('name', 'harry')
>>> prefs.get('name')
'harry'
>>> prefs.update('name', 'larry')
>>> prefs.remove('name')
```

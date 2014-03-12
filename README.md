paleocore
=========

## This is the codebase for the paleocore project.

### Note regarding settings.py:

This project does not store sensitive information (passwords etc) in settings.py as this is clearly not secure.  Instead, there is a file called secrets.py that is ignored by git (because it is listed in the .gitignore file) in which these sensitive data are stored.  settings.py imports these variables from secrets.py, and thus these data are only stored locally, rather than being made public on github. 

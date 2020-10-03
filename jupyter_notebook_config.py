c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False


# setting up the password
from IPython.lib import passwd
password = passwd("000")
c.NotebookApp.password = password
c.NotebookApp.port = 8888

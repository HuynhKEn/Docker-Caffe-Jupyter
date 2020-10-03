c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 5000

# setting up the password
from IPython.lib import passwd
password = passwd("000")
c.NotebookApp.password = password

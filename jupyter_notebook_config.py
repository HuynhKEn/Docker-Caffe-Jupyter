from IPython.lib import passwd
password_ = passwd("000")
c.NotebookApp.ip = '*'
c.NotebookApp.password = password_
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888

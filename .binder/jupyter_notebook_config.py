c = get_config()

c.FileContentsManager.delete_to_trash=False

c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

c.NotebookApp.notebook_dir = '/workspace'
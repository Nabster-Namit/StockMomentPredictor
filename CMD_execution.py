import os
from time import sleep
import subprocess

from subprocess import Popen

activate_dir = "C:/Users/namit/PycharmProjects/StockMarket/venv/Scripts/"
os.chdir(activate_dir)
os.system("activate;python -V")

cal_dir = "C:/Users/namit/PycharmProjects/StockMarket/venv/NewsExtraction"
os.chdir(cal_dir)
os.system('cmd /c "scrapy crawl news -o newstest.json"')





#
# os.system('cmd /c "cd C:/Users/namit/PycharmProjects/StockMarket/venv/Scripts/"')
# sleep(1)
# os.system('cmd /c "dir"')
# os.system('cmd /c "activate.bat"')
# sleep(1)
#
# os.system('cmd /c "cd C:/Users/namit/PycharmProjects/StockMarket/venv/NewsExtraction"')
# sleep(1)
# os.system('cmd /c "dir"')
#
# os.system('cmd /c "scrapy"')
#
# # list_files= subprocess.Popen("dir")
# # list_files.wait()
# # # print("the exit code was: %d" %list_files.returncode)
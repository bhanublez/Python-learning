import shutil
du=shutil.disk_usage("/")
print(du)
print(du.free/du.total*100)

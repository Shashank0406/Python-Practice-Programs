import os,glob



files = glob.glob("*.py")

files.sort(key=os.path.getctime)


print("\n".join(files))
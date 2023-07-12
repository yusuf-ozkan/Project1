import os

git_directory = os.getcwd()  # Get the current working directory
desktop_dir = '/'.join(git_directory.split("\\")[:-2]) + "/Masaüstü/" # Get the desktop directory

input_location = desktop_dir + "Training4D@_V50.7.0.9.9.icdb"
output_location = desktop_dir + "Training4D_test"

print(input_location)
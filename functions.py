import subprocess


def SendNotification(message):
    message=str(message)
    command = "notify-send -u normal -t 6000"
    command_list = command.split()
    command_list.append(message)
    try:
        subprocess.check_output(command_list)
    except subprocess.CalledProcessError as e:
        error = (e.output)
        return error

def makeDirectory(directory):
    directory = str(directory)
    command = "sudo mkdir -p"
    command_list = command.split()
    command_list.append(directory)
    try:
        subprocess.check_output(command_list)
    except subprocess.CalledProcessError as e:
        error = (e.output)
        return error
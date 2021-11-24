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

def mountUSB():
    mounpoint ="/media/ubuntu/WriteTo"
    command = "sudo mkdir -p"
    command_list = command.split()
    command_list.append(mounpoint)
    try:
        subprocess.check_output(command_list)
    except subprocess.CalledProcessError as e:
        error = (e.output)
        return error

def installPackage(package):
    directory = str(package)
    command = "sudo apt-get install -y"
    command_list = command.split()
    command_list.append(package)
    try:
        subprocess.check_output(command_list)
    except subprocess.CalledProcessError as e:
        error = (e.output)
        return error

def runZerofree():
    command = "sudo zerofree -v /dev/sda2"
    command_list = command.split()
    try:
        subprocess.check_output(command_list)
    except subprocess.CalledProcessError as e:
        error = (e.output)
        return error

def cloneDisk():

    try:
        diskDup = subprocess.run(
            ['sudo', 'dd', 'if=/home/test/diskdupe/test.txt', 'conv=sync,noerror', 'status=progress', 'bs=64K'],
            check=True, capture_output=True)
        compression = subprocess.run(['gzip', '-c', ' >' '/home/test/diskdupe/test.txt.gz'],
                                     input=diskDup.stdout, capture_output=True)
        print(diskDup.stderr)
    except subprocess.CalledProcessError as e:
        error = (e.output)
        return error
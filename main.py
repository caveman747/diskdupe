import functions

def main ():


    #Making directory if not already present
    #functions.SendNotification("Creating /media/ubuntu/WriteTo directory and mounting USB drive there")

    mkdir_exit = functions.makeDirectory("/media/ubuntu/WriteTo")

    if mkdir_exit != None:
        print(mkdir_exit)

    #functions.SendNotification("It works!")


    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)
    #
    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)
    #
    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)
    #
    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)


if __name__ == "__main__":
    main()
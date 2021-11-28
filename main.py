import tkinter
import functions

def main():

   # functions.SendNotification("Starting Disk Dupe")
   # functions.SendNotification("Creating and mounting USB drive to /media/ubuntu/WriteTo")
   # functions.makeDirectory("/media/ubuntu/WriteTo")
   # functions.mountUSB()
   # functions.SendNotification("Installing and running zerofree on root partition")
   # functions.installPackage("zerofree")
   # functions.runZerofree()
    functions.cloneDisk()

    top = tkinter.Tk()
    top.mainloop()


if __name__ == "__main__":
    main()

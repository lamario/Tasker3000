######################## Task CLASS ########################
class TTask :
    pendingCount = 0
    doneCount = 0
    def __init__ ( self, ID, Name, Day ) :
        self.ID = ID
        self.Name = Name
        self.Day = Day
######################## getFileInfo () FUNCTION ########################
def getFileInfo ( Tasks_file ) :
    line = Tasks_file.readline ()
    line = Tasks_file.readline ()
    line = Tasks_file.readline ()
    FileType = str ( line.rstrip ('\n') )
    return FileType
######################## getTaskCount () FUNCTION ########################
def getTaskCount ( Tasks_file ) :
    line = Tasks_file.readline ()
    line = Tasks_file.readline ()
    TaskCount = int ( line.rstrip ('\n') )
    line = Tasks_file.readline ()
    return TaskCount
######################## readFile () FUNCTION ########################
def readFile ( Tasks_file ) :
    FileType = getFileInfo ( Tasks_file )
    TaskCount = getTaskCount ( Tasks_file ) 
    Tasks_list = []
    # loading the newTasks File and saving line elements into Task objects of a list
    for loop in range ( 0, TaskCount ) :
        line = Tasks_file.readline ().rstrip ( '\n' )
        # this is not a nice way, but works for now
        helpList = [ 0, 0, 0 ]
        helpList[0], helpList[1], helpList[2] = line.split ( '|', 3 )
        Task = TTask ( helpList[0], helpList[1], helpList[2] )         #ID|Name|Day
        # this ^^ can be fixed by knowing how to input more variables easier
        if FileType == 'Pending' :
            TTask.pendingCount += 1
            Task.Type = 'Pending'
        elif FileType == 'Done' :
            TTask.doneCount += 1
            Task.Type = 'Done'
        Tasks_list.insert ( loop, Task )
    return Tasks_list
######################## loadFiles() FUNCTION ########################
def loadFiles () : #loading files into lists of Task:TTask
    # opening files and creating lists
    pendingTasks_file = open ( 'pendingTasks.txt', 'r' )
    pending = readFile ( pendingTasks_file )
    pendingTasks_file.close ()

    doneTasks_file = open ( 'doneTasks.txt', 'r' )
    done = readFile ( doneTasks_file )
    doneTasks_file.close ()

    # return filled lists with Tasks
    return pending, done
######################## printList () FUNCTION ########################
def printList ( Tasks ) :
    if Tasks[0].Type == 'Pending' :
        for loop in range ( 0, TTask.pendingCount ) :
            print (Tasks[loop].ID +' '+ Tasks[loop].Name +' '+ Tasks[loop].Day )
        print ()
    elif Tasks[0].Type == 'Done' :
        for loop in range ( 0, TTask.doneCount ) :
            print (Tasks[loop].ID +' '+ Tasks[loop].Name +' '+ Tasks[loop].Day )
        print ()
########################  ########################
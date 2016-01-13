######################################################
#
#   Tasker3000
#   Richard Beno (rbnext@gmail.com)
#   v1.0    2016-01-13
#
######################################################
import tasker3000DATA, tasker3000UI
# LIST OF FUNCTIONS: 

# DEFINING FUNCTIONS

# defining the main () function
def main () :
    pendingTasks, doneTasks = tasker3000DATA.loadFiles ()
    tasker3000DATA.printList ( pendingTasks ) 
    tasker3000DATA.printList ( doneTasks ) 
# THIS IS THE MAIN BODY / START OF THE PROGRAM
main () 
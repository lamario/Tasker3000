######################################################
#
#   Tasker3000
#   Richard Beno (rbnext@gmail.com)
#   v1.0    2016-01-13
#
######################################################
import module2
# LIST OF FUNCTIONS: 

# DEFINING FUNCTIONS

# defining the main () function
def main () :
    new = []
    done = []
    new, done = module2.loadFiles ()
    print (new[0].ID +' '+ new[0].Name +' '+ new[0].Day )
# THIS IS THE MAIN BODY / START OF THE PROGRAM
main ()
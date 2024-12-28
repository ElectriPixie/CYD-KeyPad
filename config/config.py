Import("env")
import os

board_name = env.get("BOARD")

User_Setup = env.get("PROJECT_INCLUDE_DIR")+"/User_Setup.h"
User_Setup_Link = env.get("PROJECT_DIR")+"/.pio/libdeps/"+board_name+"/TFT_eSPI/User_Setup.h"
if not os.path.islink(User_Setup_Link) and not os.path.isfile(User_Setup_Link):
    os.symlink(User_Setup, User_Setup_Link)
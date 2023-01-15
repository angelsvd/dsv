**Bee swarm python macro installation and instructions**

Made and tested on mac, currently untested for windows/linux
*Due to  the code, it is unlikely to work on windows/linux thanks to the retina display.*
I can release a window-compatible one, but ~im lazy~

**Set your display resolution to default and colour profile to colour LCD. For roblox, play in fullscreen and set the graphics quality to 1**

**Installation**


0. Install python v3.9.5: https://www.python.org/downloads/release/python-395/
**Check "Add python to path"  in the installation window**

1. Create a folder anywhere (it will be where the macro files are stored)


2.Open terminal/command line
   (Optional: Create a python venv)
   

3.Run the following command:
   *pip install pyautogui pillow opencv-python python-imagesearch discord-webhook*

   *If you have python installed previously, use python3 -m pip install pyautogui pillow opencv-python python-imagesearch discord-webhook*

**Setup**

4. Download the files in the git repo into the folder made in step 1.
5. Go to save.txt and edit the resolution. You can find it by clicking on the apple icon on the top bar menu -> about this mac -> displays
 *if you cant find save.txt, that means that I have updated the code. You can adjust the resolution at settings.txt*
 
 **Launching the program**

6. Navigate to the folder created in step 1 using the "cd" command:

   *eg cd desktop/bee_swarm_macro*

7. run the program with the following command:

   *python e_macro.py*

   *If you have multiple versions of python installed, use python3 e_macro.py*

*During the runtime, you may be prompted to enable certain permissions in your system and security settings. Do enable those.*
Currently, it seems like you have to give terminal permissions under the accessibility and screen recording sections. Do let me know if there is any permissions I missed

Credits:

Natro macro for some of the techniques

**Exiting the macro:**
Ensure the terminal window is focused and press ctrl c to quit (not cmd c)


**Bugs and fixes:**


1. The player keeps rotating at the hive before walking
   - The code is not able to detect the hive. To fix this, take a screenshot of the hive area under your hotbar. Reset your character, then press "." 4        times, then press pgup (fn+ up arrow) until you cant go up anymore. Than press "o" until you stop zooming out. 
   - Disable your shift lock switch and using cmd+shift+4, take a screenshot of the area under your hotbar. 
   - Here is an example: https://imgur.com/a/pvWYaWP You can take the screenshot anywhere in the red box. Try to keep the screenshot small                    https://imgur.com/a/FlcxKVl
   - Replace hive1.png in the images folder with your new image

2. The dock is brought up during the macro, interrupting the key inputs.
   - This can be solved by manually clicking on the screen when the macro is ran
3. *ImportError: dlopen/import cv2* in the terminal when the code is ran.
   - This is most likely caused by an outdated macOS version. For a work around, check out https://github.com/existancepy/bss-macro-py-no-cv2
   - A better fix would just be to update your mac OS software
4. Enable dictionary menu is brought up during the macro
   - Fix:  system preferences -> keyboard -> shortcuts -> app shortcuts
   - click the '+' sign and put roblox as the application
   - Under Menu Title, input 'Start Dictation…'  without the single quotes of course. The three periods are actually an ellipsis, which is one character which you can type by pressing option and the [ ; ] key, or just copy and paste what I typed above. 
   - I set the shortcut to Option + Command + E for that one.
   - Add it
   - Sample image: https://imgur.com/a/hzbsM5e
   - Credit: https://www.dofus.com/en/forum/1151-general-problems-solutions/339448-issue-with-macos-keyboard-keys


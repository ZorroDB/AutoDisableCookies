import webbrowser
import os

def block_cookies_and_hide():
    # Open command prompt and notify user that the script is active
    os.system("start cmd.exe /k echo Cookies blocked and hidden /Q")

    # Block cookies in the web browser
    browser = webbrowser.get()
    browser.set_cookie("block=true")

    # Notify user that cookies have been removed
    os.system("start cmd.exe /k echo Cookies removed /Q")

# Call the function to activate the script
block_cookies_and_hide()
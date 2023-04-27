import platform

def getOS():
    osName = platform.system()
    arch = platform.machine()
    
    return osName, arch

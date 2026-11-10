#lock_tools.py
#It's check if the account is locked
def is_locked(failed,max_tries=3):
    """Return True if failed reaches max_tries,else false"""
    return failed>=max_tries
def tries_left(failed,max_tries=3):
    """return 0 if locked,elseremainig tries"""
    if is_locked(failed,max_tries):
        return 0
    return max_tries - failed
def status(failed):
    if is_locked(failed):
        return "locked"
    return f"active({tries_left(failed)} tries_left)"
print (is_locked(2))
print (is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))




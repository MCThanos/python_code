import signal


def myHandler(signum, frame):
    print('Signal handler called with signal', signum)


signal.signal(signal.SIGINT,myHandler)
signal.alarm(3)
signal.pause()
print('End of Signal Demo')

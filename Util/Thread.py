import threading;

# list các luồng sẽ sử dụng
threads = []

def CreateThreadForLoopFunc(loopfunc, loopAmount, num_thread, workbook):
    thread = threading.Thread(target=loopfunc, args=(loopAmount,num_thread,workbook));
    threads.append(thread);

def StartAllThread():
    for thread in threads:
        thread.start();

def JoinAllThreads():
    for thread in threads:
        thread.join();
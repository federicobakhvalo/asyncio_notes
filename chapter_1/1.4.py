import multiprocessing
import os


def hello_from_process():
    print(f'Привет от дочернего процесса {os.getpid()}!')


def new_process():
    print('New process is ',os.getpid())


if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process1 = multiprocessing.Process(target=new_process)
    hello_process.start()
    hello_process1.start()
    print(f'Привет от родительского процесса {os.getpid()}')
    hello_process.join()
    hello_process1.join()

from multiprocessing import Process
import threading


class Ps:
    @staticmethod
    def bg_run_task_on_thread(target: callable, args: iter):
        t = threading.Thread(target=target, args=args)
        t.daemon = True
        t.start()

    @staticmethod
    def bg_run_task_on_process(target: callable, args=()):
        t = Process(target=target, args=args)
        t.start()

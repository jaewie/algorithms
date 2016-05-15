from threading import Semaphore


class Barrier(object):
    def __init__(self, num_threads, before_barrier_func, after_barrier_func):
        self.num_threads = num_threads
        self.mutex = Semaphore(1)
        self.turnstile0 = Semaphore(0)
        self.turnstile1 = Semaphore(1)
        self.count = 0
        self.before_barrier_func = before_barrier_func
        self.after_barrier_func = after_barrier_func


    def phase1(self):
        self.mutex.acquire()
        self.count += 1
        if self.count == self.num_threads:
            self.turnstile1.acquire() # Close turnstile 1
            self.turnstile0.release() # Open turnstile 0
        self.mutex.release()

        self.turnstile0.acquire()
        self.turnstile0.release()

    def phase2(self):
        self.mutex.acquire()
        self.count -= 1
        if not self.count:
            self.turnstile0.acquire() # Close turnstile 0
            self.turnstile1.release() # Open turnstile 1
        self.mutex.release()
        self.turnstile1.acquire()
        self.turnstile1.release()


class LightSwitch(object):
    def __init__(self):
        self.count = 0
        self.mutex = Semaphore(1)

    def lock(self, semaphore):
        self.mutex.acquire()
        self.count += 1
        if self.count == 1:
            semaphore.acquire()
        self.mutex.release()


    def unlock(self, semaphore):
        self.mutex.acquire()
        self.count -= 1
        if self.count == 0:
            semaphore.release()
        self.mutex.release()

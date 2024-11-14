# sync_database.py
from file_database import FileDatabase
from threading import Lock, Semaphore, Thread
from multiprocessing import Process, Lock as ProcessLock, Semaphore as ProcessSemaphore


class SyncDatabase(FileDatabase):
    def __init__(self, filename, mode='threads'):
        super().__init__(filename)
        self.mode = mode
        self.write_lock = Lock() if mode == 'threads' else ProcessLock()
        self.read_semaphore = Semaphore(10) if mode == 'threads' else ProcessSemaphore(10)

    def start_read(self):
        self.read_semaphore.acquire()

    def end_read(self):
        self.read_semaphore.release()

    def start_write(self):
        self.write_lock.acquire()

    def end_write(self):
        self.write_lock.release()

    def value_set(self, key, value):
        self.start_write()
        try:
            return super().value_set(key, value)
        finally:
            self.end_write()

    def value_get(self, key):
        self.start_read()
        try:
            return super().value_get(key)
        finally:
            self.end_read()

    def value_delete(self, key):
        self.start_write()
        try:
            return super().value_delete(key)
        finally:
            self.end_write()

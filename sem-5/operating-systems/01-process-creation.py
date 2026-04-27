# Practical 01: Process Creation and Management
# Demonstrates process creation using fork(), exec(), and wait() system calls

import os
import sys
import subprocess

def run_posix():
    print(f"Parent process: PID = {os.getpid()}")
    try:
        pid = os.fork()
    except OSError as e:
        print(f"fork failed: {e}")
        sys.exit(1)

    if pid == 0:
        # Child process
        print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
        print("Child executing 'ls -l' using execlp:")
        try:
            os.execlp("ls", "ls", "-l")
        except OSError as e:
            print(f"exec failed: {e}")
            os._exit(1)
    else:
        # Parent process
        print(f"Parent waiting for child (PID = {pid}) to finish...")
        _, status = os.wait()
        if os.WIFEXITED(status):
            print(f"Child exited with status {os.WEXITSTATUS(status)}")
        print("Parent process resumes and exits.")

def run_windows():
    print(f"Parent process: PID = {os.getpid()}")
    print("Simulating child process creation using subprocess (Windows environment):")
    
    # Spawn child process
    cmd = ["cmd.exe", "/c", "echo Child process running under parent PID: " + str(os.getpid()) + " && dir /b"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Parent waiting for child process (PID = {process.pid}) to finish...")
    
    stdout, stderr = process.communicate()
    print("--- Child Process Output ---")
    print(stdout.strip())
    print(f"Child exited with return code {process.returncode}")
    print("Parent process resumes and exits.")

def main():
    print("=" * 60)
    print("       PROCESS CREATION (fork, exec, wait)")
    print("=" * 60)
    if hasattr(os, "fork"):
        run_posix()
    else:
        run_windows()
    print("=" * 60)

if __name__ == "__main__":
    main()

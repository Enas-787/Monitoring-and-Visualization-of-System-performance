
import os, subprocess, time

# start server in background
srv = subprocess.Popen(["iperf3","-s"])
time.sleep(1)
os.system("iperf3 -c 127.0.0.1 -t 20")  # run client test for 20s
srv.terminate()

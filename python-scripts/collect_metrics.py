import psutil, csv, time, datetime, os

os.makedirs("output", exist_ok=True)
csv_file = "output/metrics_idle.csv"
log_file = "output/alerts_idle.log"

thresholds = {"cpu": 85, "mem": 85}  # change if needed

fields = ["ts", "cpu_percent", "mem_percent", "disk_read", "disk_write", "net_sent", "net_recv"]

with open(csv_file, "w", newline="") as cf, open(log_file, "w") as lf:
    writer = csv.writer(cf)
    writer.writerow(fields)
    prev_disk = psutil.disk_io_counters()
    prev_net = psutil.net_io_counters()
    while True:
        ts = datetime.datetime.now(datetime.UTC).isoformat()

        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_io_counters()
        net = psutil.net_io_counters()

        disk_r = disk.read_bytes - prev_disk.read_bytes
        disk_w = disk.write_bytes - prev_disk.write_bytes
        net_s = net.bytes_sent - prev_net.bytes_sent
        net_r = net.bytes_recv - prev_net.bytes_recv

        writer.writerow([ts, cpu, mem, disk_r, disk_w, net_s, net_r])
        cf.flush()

        if cpu >= thresholds["cpu"]:
            lf.write(f"{ts} ALERT: CPU {cpu}%\n")
        if mem >= thresholds["mem"]:
            lf.write(f"{ts} ALERT: MEM {mem}%\n")
        lf.flush()

        prev_disk, prev_net = disk, net

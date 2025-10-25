echo "Timestamp,Container ID,Name,CPU %,Mem Usage / Limit,Mem %,Net I/O,Block I/O,PIDs" > docker_stats_log.csv
while true; do \
    echo "$(date +%Y-%m-%d\ %H:%M:%S),$(docker stats --no-stream --format '{{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}' cacf3d5d7fd8 | tr '\t' ',')"; \
    sleep 1; \
done >> docker_stats_log.csv
# Monitoring Docker Statistics

Shell Script for Periodic Logging

You can use a simple shell script employing a while loop, the date command for a timestamp, and output redirection (>>) to append the output. You should use the --no-stream flag on docker stats to get a single snapshot on each execution.

Here is a general command structure for a Linux/macOS shell, logging every 10 seconds. You should replace &lt;CONTAINER_NAME_OR_ID&gt; with your container's name or ID.

[dockerstats.sh](dockerstats.sh)

Breakdown of the Command

    while true; do ... done: Creates an infinite loop.

    docker stats --no-stream: Forces docker stats to print a single, non-streaming snapshot of the metrics, which is essential for a periodic script.

    --format '...': This flag is crucial for structuring the output in a consistent, machine-readable format.

        `{{.Container}}`, `{{.Name}}`, `{{.CPUPerc}}`, `{{.MemUsage}}`, `{{.MemPerc}}`, etc., are Go template placeholders for the metrics you requested.

        The values are separated by tabs (\t) initially, as it's a character less likely to appear in the metric values than a space.

    date +%Y-%m-%d\ %H:%M:%S: Captures the current timestamp and formats it.

    echo "...": Prints the timestamp, a comma, and the formatted docker stats output.

    | tr '\t' ',': Pipes the docker stats output to the tr command, which translates (replaces) all tabs (\t) with commas (,) to create a proper CSV record.

    sleep 10: Pauses the script for 10 seconds before the next snapshot. Adjust this value for your desired sampling frequency.

    >> docker_stats_log.csv: Appends the entire output of the loop to the specified CSV file.

```bash
./dockerstats.sh
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/monitoring-docker-statistics](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/monitoring-docker-statistics)

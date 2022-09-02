import os
import subprocess


def run_command(command, replace_newline=True):
    """
    Run a command and return the output and error code.
    """
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, error = process.communicate()
    if error:
        print(error.decode("utf-8"))
        exit(1)
    output = output.decode("utf-8")
    if replace_newline:
        output = output.strip().replace("\n", "")
    return output


last_commit_cmd = [
    "git",
    "log",
    "-1",
    "--pretty=format:%h",
]

last_commit = run_command(last_commit_cmd)


last_tag_cmd = [
    "git",
    "describe",
    "--tags",
    "--abbrev=0",
]
last_tag = run_command(last_tag_cmd)

current_date_cmd = [
    "date",
    "+%d-%m-%Y_%H_%M_%S",
]
current_date = run_command(current_date_cmd)

database_backup_id = f"{last_tag}__{last_commit}__{current_date}.sql"

database_backup_cmd = [
    "docker-compose",
    "-f",
    "docker-compose.prod.yml",
    "exec",
    "-T",
    "db",
    "pg_dumpall",
    "-c",
    "-U",
    "postgres",
]

out = run_command(database_backup_cmd, replace_newline=False)
database_backup = open(database_backup_id, "w")
database_backup.write(out)
database_backup.close()
print("Backup created ", database_backup_id)

aws_backup_cmd = [
    "aws",
    "--endpoint-url=https://storage.yandexcloud.net/",
    "s3",
    "cp",
    database_backup_id,
    f"s3://postgre-backups/{database_backup_id}",
]

aws_backup = run_command(aws_backup_cmd)
print(aws_backup)

remove_local_backup_cmd = [
    "rm",
    database_backup_id,
]
run_command(remove_local_backup_cmd)

print("Local backup removed")

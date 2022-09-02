import argparse
import subprocess
import os


def run_command(command):
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
    output = output.strip().replace("\n", "")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parsing parameters")
    params = [
        (
            "--database_backup_id",
            {"dest": "database_backup_id", "type": str, "default": ""},
        )
    ]

    for name, param in params:
        parser.add_argument(name, **param)

    args = parser.parse_args()
    args = args._get_kwargs()
    args = {arg[0]: arg[1] for arg in args}
    database_backup_id = args["database_backup_id"]
    print(database_backup_id)

    restore_db_cmd = [
        "aws",
        "--endpoint-url=https://storage.yandexcloud.net/",
        "s3",
        "cp",
        f"s3://postgre-backups/{database_backup_id}",
        f"./database/{database_backup_id}",
    ]

    restore_db = run_command(restore_db_cmd)
    print(restore_db)

    # docker_restore_db_cmd = [
    #     "cat",
    #     f"./database/{database_backup_id}",
    #     "|",
    #     "docker-compose",
    #     "-f",
    #     "docker-compose.prod.yml",
    #     "exec",
    #     "-T",
    #     "db",
    #     "psql",
    #     "-U",
    #     "postgres",
    # ]
    # TODO: разобраться как сделать через run_command
    # docker_restore_db = run_command(docker_restore_db_cmd)

    docker_restore_db_cmd = f"cat ./database/{database_backup_id} | docker-compose -f docker-compose.prod.yml exec -T db psql -U postgres > /dev/null"
    restore_code = os.system(docker_restore_db_cmd)
    if restore_code != 0:
        print("Restore failed")
        exit(1)

    print("Database restored")

    rm_backup_cmd = ["rm", f"./database/{database_backup_id}"]
    run_command(rm_backup_cmd)
    print("Backup removed")

# aws --endpoint-url=https://storage.yandexcloud.net/ s3 cp s3://postgre-backups/v0.0.2__524af41__02-09-2022_13_47_15.sql v0.0.2__524af41__02-09-2022_13_47_15.sql
import argparse
import subprocess


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
    print(args.get("database_backup_id"))

    restore_db_cmd = [
        "aws",
        "--endpoint-url=https://storage.yandexcloud.net/",
        "s3",
        "cp",
        f"s3://postgre-backups/{args.get('database_backup_id')}",
        f"{args.get('database_backup_id')}",
    ]

    restore_db = run_command(restore_db_cmd)
    print(restore_db)

    docker_restore_db_cmd = [
        "docker-compose",
        "-f",
        "docker-compose.prod.yml",
        "exec",
        "-T",
        "db",
        "psql",
        "-U",
        "postgres",
        "-f",
        f"{args.get('database_backup_id')}",
    ]

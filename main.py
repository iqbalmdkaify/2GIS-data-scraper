from runner import Runner
from utils import initiate_cli_parser, initiate_logger


def main() -> None:
    args = initiate_cli_parser()
    initiate_logger(args.log)

    runner = Runner(config=args)
    runner.run()


if __name__ == "__main__":
    main()

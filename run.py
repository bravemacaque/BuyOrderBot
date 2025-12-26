import asyncio

from buy_order_bot import load_config, setup_logging, SteamAccount, AccountManager

def main():
    config = load_config()
    setup_logging()
    
    accounts = [SteamAccount(acc) for acc in config['accounts']]
    manager = AccountManager(accounts=accounts)
    
    try:
        asyncio.run(manager.main())
    except KeyboardInterrupt:
        raise SystemExit(1)
    
if __name__ == "__main__":
    main()
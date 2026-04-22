from pages.accounts_overview_page import AccountsOverview

def test_new_account_creation(logged_in_driver, config, logger):
    
    accounts_overview = AccountsOverview(logged_in_driver)

    logger.info("Fetching real-time account IDs...")
    existing_ids = accounts_overview.get_all_accounts_ids()

    active_id = existing_ids[0] 
    logger.info(f"Using dynamic Account ID: {active_id}") 

    logger.info("Opening New Account...")
    open_new_acc_page = accounts_overview.select_service("open new account")

    open_new_acc_page.open_new_account(config["ACCOUNT_TYPE"], active_id)

    logger.info("Navigating to Accounts Overview...")
    accounts_overview = open_new_acc_page.select_service("Accounts overview")

    existing_accounts = accounts_overview.get_all_accounts_ids()

    logger.info("Printing Accounts Overview...")
    logger.info("\nAccount | Balance |               Amount Available")
    for account in existing_accounts:
        logger.info(f"{account} | {accounts_overview.get_balance(account)} | \
              {accounts_overview.get_available_amount(account)}")

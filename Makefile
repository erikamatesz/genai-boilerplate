## help: Show this help info.
help: Makefile
	@printf "\n\033[1mUsage: make <command> ...\033[0m\n\n\033[1mCommands:\033[0m\n\n"
	@sed -n 's/^## //p' $< | awk -F':' '{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort | sed -e 's/^/  /'
	@printf "\n"

## start_aws: Create main.py and requirements.txt from boilerplate/main_aws.py and requirements_aws.txt.
start_aws:
	@if [ -f src/main.py ]; then \
		mv src/main.py src/main_old.py; \
		echo "main.py exists. Renamed to main_old.py"; \
	fi
	@if [ -f requirements.txt ]; then \
		mv requirements.txt requirements_old.txt; \
		echo "requirements.txt exists. Renamed to requirements_old.txt"; \
	fi
	cp boilerplate/main_aws.py src/main.py
	cp boilerplate/requirements_aws.txt requirements.txt
	cp boilerplate/config_aws.py src/config.py
	echo "main.py, requirements.txt, and config.py created from AWS files."

	@if [ -f boilerplate/.env.aws ]; then \
		cp boilerplate/.env.aws .env; \
		echo ".env.aws copied to .env"; \
	fi

	@if [ -d ".awsvenv" ]; then \
		rm -rf .awsvenv; \
		echo "Existing virtual environment '.awsvenv' deleted."; \
	fi
	@python3 -m venv .awsvenv
	@echo "Virtual environment '.awsvenv' created."
	@.awsvenv/bin/pip install -r requirements.txt
	@echo "Dependencies installed."

	@echo "\033[1;32mVirtual environment '.awsvenv' created successfully!\033[0m"
	@echo "\033[1;33mBefore continuing, please deactivate any existing virtual environment by running the command:\033[0m"
	@echo "\033[1;34mdeactivate\033[0m"
	@echo "\033[1;33mOnce deactivated, you can continue with the setup.\033[0m"
	@echo "\033[1;33mThe basic dependencies have been installed, but you need to activate the virtual environment.\033[0m"
	@echo "\033[1;33mTo activate the virtual environment, use the following command:\033[0m"
	@echo "\033[1;34mFor Mac/Linux: source .awsvenv/bin/activate\033[0m"
	@echo "\033[1;34mFor Windows: .\\.awsvenv\\Scripts\\activate\033[0m"
	@echo "\033[1;33mAfter activating the environment, you can run your project!\033[0m"

## start_google: Create main.py and requirements.txt from boilerplate/main_google.py and requirements_google.txt.
start_google:
	@if [ -f src/main.py ]; then \
		mv src/main.py src/main_old.py; \
		echo "main.py exists. Renamed to main_old.py"; \
	fi
	@if [ -f requirements.txt ]; then \
		mv requirements.txt requirements_old.txt; \
		echo "requirements.txt exists. Renamed to requirements_old.txt"; \
	fi
	cp boilerplate/main_google.py src/main.py
	cp boilerplate/requirements_google.txt requirements.txt
	cp boilerplate/config_google.py src/config.py
	echo "main.py, requirements.txt, and config.py created from Google files."

	@if [ -f boilerplate/.env.google ]; then \
		cp boilerplate/.env.google .env; \
		echo ".env.google copied to .env"; \
	fi

	@if [ -d ".googlevenv" ]; then \
		rm -rf .googlevenv; \
		echo "Existing virtual environment '.googlevenv' deleted."; \
	fi
	@python3 -m venv .googlevenv
	@echo "Virtual environment '.googlevenv' created."
	@.googlevenv/bin/pip install -r requirements.txt
	@echo "Dependencies installed."

	@echo "\033[1;32mVirtual environment '.googlevenv' created successfully!\033[0m"
	@echo "\033[1;33mBefore continuing, please deactivate any existing virtual environment by running the command:\033[0m"
	@echo "\033[1;34mdeactivate\033[0m"
	@echo "\033[1;33mOnce deactivated, you can continue with the setup.\033[0m"
	@echo "\033[1;33mThe basic dependencies have been installed, but you need to activate the virtual environment.\033[0m"
	@echo "\033[1;33mTo activate the virtual environment, use the following command:\033[0m"
	@echo "\033[1;34mFor Mac/Linux: source .googlevenv/bin/activate\033[0m"
	@echo "\033[1;34mFor Windows: .\\.googlevenv\\Scripts\\activate\033[0m"
	@echo "\033[1;33mAfter activating the environment, you can run your project!\033[0m"

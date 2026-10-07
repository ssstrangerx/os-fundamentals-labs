PYTHON ?= python3

all:
	$(PYTHON) scripts/run_all_demos.py

processes:
	$(PYTHON) -c "from src.process_observer import display_process_table; display_process_table(limit=15)"

schedule:
	$(PYTHON) -c "from src.scheduling_simulator import demo_scheduling; demo_scheduling()"

threads:
	$(PYTHON) -c "from src.thread_demo import run_thread_demo; run_thread_demo()"

ipc:
	$(PYTHON) -c "from src.ipc_demo import run_ipc_demo; run_ipc_demo()"

check:
	pytest -q

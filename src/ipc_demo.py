import multiprocessing as mp
from multiprocessing import Pipe


def child_process(conn):
    msg = conn.recv()
    print(f"[child] received: {msg}")
    response = {"status": "ok", "message": "Hello from child", "payload": msg['payload'] * 2}
    conn.send(response)
    conn.close()


def run_ipc_demo() -> None:
    parent_conn, child_conn = Pipe()
    process = mp.Process(target=child_process, args=(child_conn,))
    process.start()

    payload = {"payload": 7, "request": "compute"}
    parent_conn.send(payload)
    result = parent_conn.recv()
    print(f"[parent] received result: {result}")

    process.join()
    print("IPC demonstration complete.")


if __name__ == "__main__":
    run_ipc_demo()

import select
import socket

read_socket = select.select(CONNECTION_LIST,[],[])
write_socket = select.select(CONNECTION_LIST,[],[])
error_socket = select.select(CONNECTION_LIST,[],[])
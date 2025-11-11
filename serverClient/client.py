import zmq

# def main():
#     context = zmq.Context()
#     socket = context.socket(zmq.REQ)
#     socket.connect("tcp://localhost:42069")

#     print("Connected to server at tcp://localhost:5555")
#     print("Type messages to send. Type 'exit' to quit.\n")

#     try:
#         while True:
#             message = input("> ")
#             # Send message to server
#             # cannot send again unless reply is received
#             socket.send_string(message)

#             if message.lower() in ("exit", "quit"):
#                 print("Exiting...")
#                 break
#             # Wait for server reply
#             reply = socket.recv_string()
#             print(f"Server replied: {reply}\n")

#     except KeyboardInterrupt:
#         print("\nInterrupted by user.")
#     finally:
#         socket.close()
#         context.term()


def main():
    with zmq.Context() as context:
        with context.socket(zmq.REQ) as socket:
            socket.connect("tcp://localhost:42069")

            #prompt user for input
            print("Connected to server at tcp://localhost:42069")
            print("Type messages to send. Type 'exit' to quit.\n")
            try:
                while True:
                    message = input("> ")
                    # Send message to server
                    # cannot send again unless reply is received
                    #can be interrupted by context.term()
                    #when block is exited context is terminated
                    socket.send_string(message)

                    if message.lower() in ("exit", "quit"):
                        print("Exiting...")
                        break
                    # Wait for server reply
                    reply = socket.recv_string()
                    print(f"Server replied: {reply}\n")

            except KeyboardInterrupt:
                print("\nInterrupted by user.")

if __name__ == "__main__":
    main()

# Assignment-2
# Server file
In this server file. Server is connected to client by adding IP addresses.Then used vgencmd statement. Once the data is gathered, it organizes it into a dictionary named data, creating JSON-like objects for each data point. The server then sends this data as bytes to the connected client.The client-side code connects to the server, receives the transmitted data, decodes it from bytes to a JSON-like format, and prints each piece of system information separately in the console.The code establishes a communication channel where the server continuously provides system information to any connected clients upon request.


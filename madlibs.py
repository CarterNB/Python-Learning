adj = [None] * 10
noun = [None] * 10
pnoun = [None] * 10

for i in range(0, 2):
    adj[i] = input("Enter an adjective:")

for i in range(0, 3):
    noun[i] = input("Enter a noun:")

pnoun = input("Enter a plural noun:")

print("There are many", adj[0], "ways to choose a", noun[0],
      "to read. First, you could ask for recommendations from your friends and " + pnoun + ". Just don't ask your",
      noun[1],
      "she only reads", adj[1], "books with " + noun[2] + "-ripping goddesses on the cover.")

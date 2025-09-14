# spam filter
s1="buy now!"
s2="click this link"
s3="lottery winner"
s4="free gift"
s5="limited time offer"

message = input("Enter your message: ").lower()
if (s1 in message) or (s2 in message) or (s3 in message) or (s4 in message) or (s5 in message):
    print("This message is spam")
else:
    print("This message is not spam")

format = input("File name: ").strip().lower()

if format.endswith(('.jpeg', '.jpg')):
    print("image/jpeg")
elif format.endswith('.gif'):
    print("image/gif")
elif format.endswith('.png'):
    print("image/png")
elif format.endswith('.pdf'):
    print("application/pdf")
elif format.endswith('.txt'):
    print("text/plain")
elif format.endswith('.zip'):
    print("application/zip")
else:
    print("octet-stream")

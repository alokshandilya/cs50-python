def extensions(str):
    if str.endswith(".gif"):
        print("image/gif")
    elif str.endswith(".jpeg") or str.endswith(".jpg"):
        print("image/jpeg")
    elif str.endswith(".png"):
        print("image/png")
    elif str.endswith(".pdf"):
        print("application/pdf")
    elif str.endswith(".txt"):
        print("text/plain")
    elif str.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


def main():
    fileName = input("Enter File Name : ").strip().casefold()
    extensions(fileName)


main()

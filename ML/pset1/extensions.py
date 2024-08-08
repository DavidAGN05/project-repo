file = str.casefold(input("File name: ")).rsplit(".", 1)
suffix = file[1]

match suffix:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("applciations/octet-stream")

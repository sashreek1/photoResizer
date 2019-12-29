from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_queries =['Galaxy','satelite']


def downloadimages(query):
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 50,
                 "print_urls": True,
                 "size": "medium"}
    try:
        response.download(arguments)

        # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 50,
                     "print_urls": True,
                     "size": "medium"}

        try:
            response.download(arguments)
        except:
            pass


for query in search_queries:
    downloadimages(query)
    print()
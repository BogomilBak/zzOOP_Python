from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.create_album()

    def create_album(self):
        result = []
        for page in range(self.pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for number, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                index = len(page)
                self.photos[number].append(label)
                return f"{label} photo added successfully on page {number + 1} slot {index + 1}"
        return "No more free slots"

    def display(self):
        delimiter = '-' * 11
        result = delimiter + "\n"
        for number, page in enumerate(self.photos):
            page_str = ' '.join(['[]' if photo is not None else '' for photo in page])
            result += f"{page_str}\n" + f"{delimiter}\n"
        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())





# 300 followers
from base64 import b64encode, b64decode
from zlib import compress, decompress
three = [
    "                                 ...",
    " ,,,,,,,,,,,,,,,,,,.,,,   .,,,,,,.,,,     ..,,,,,,,,,",
    "            .,,,,.,,...,,,,.       .,,,,,...       ,,,",
    "       .,,,,.  . ...,,.           .,,.             ,,,",
    "     ..,,,,,,,,,,.,,,,        .,, ,,          .,,,,",
    "                 ,,,,,....,,...   ,,,,,,,,,,,...",
    "             .,,,,,,..,,,,.     .. .  ,. ..,.. .",
    "          .,,,.                .  . ,.....,",
    "       .,,...                 .    ,  ., .",
    "    .,.                 . .      ... .         .",
    "  ,                        .",
    "                     .",
    "       Celebrating 300 followers on SoloLearn!"]

message = "\n".join(three)
stream = message.encode("utf-8")
comp = compress(stream)
dec = b64encode(comp)
print(dec)

msg = b'eJyFUEEKAjEQu/cV472EBZ/g1ZsvWKGKUFqogt+3qd3tDBUsuzCTJmlmRP4cAE78dFB/3pqO7J3hjEtn4UuAhgn2Xsk2HqRpYM10q2Tq+ZbJK4mMrrubhJtRi4MtlJ6Yi5hmIj4mqppaeGb2rJ1l29QE+bUHoQcfCzHU6szrbovZTiAdA/aSnWvS3wfzGgx8CjFcy/p6pLscl0VuOcb8DuUpOcklx3wOa0mHDx7UW7Y='
print(decompress(b64decode(msg)).decode('utf-8'))
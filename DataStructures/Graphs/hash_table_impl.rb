friends = {
    "Alibaba" => "Baba",
    "Baba" => "Alibaba",
    "AMAZ" => ["Alibaba", "Baba"],
    "MEDA" => ["Deepa", "Deepak"],
    "Deepa" => ["AMAZ", "MEDA"],
    "Deepak" => ["AMAZ", "MEDA"]
}

# print friends

print friends["Deepa"]

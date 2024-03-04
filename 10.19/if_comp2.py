address = ["福岡市南区","北九州市八幡南区","東京都千代田区", "福岡県久留米市","福岡市西区","福岡市東区","福岡市中央区","福岡市早良区"]
fukuoka = [town[3:] for town in address if town.startswith( "福岡市")]

print( fukuoka)

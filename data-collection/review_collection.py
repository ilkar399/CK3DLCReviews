#required packages: steamreviews
#downloading review JSON data from Steam using Steam API
#data is saved into JSON in data folder

import steamreviews

app_ids = [1158310, 1303182]
#1303182 Crusader Kings III: Royal Court
#1158310 Crusader Kings III

steamreviews.download_reviews_for_app_id_batch(app_ids)


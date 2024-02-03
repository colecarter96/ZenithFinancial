from discordwebhook import Discord

discordBase = Discord(url='https://discord.com/api/webhooks/1203449126495461436/cWLuvdOd5e-vdgcelfq9zJ3u3sCkkEKSuuUJGL0gRYC39RLCGVGy032-WpIv-JJ-LniM')
discordFirstTier = Discord(url='https://discord.com/api/webhooks/1203451064020508682/pXJS3CMeUqAMsrtNgKrfeU9mnqthLkkBQrqXXD9xVbGnioP7syTZS3cGq6jaZ9qzbLTv')
discordFinalTier = Discord(url='https://discord.com/api/webhooks/1203451465604268072/3qe9KI9wpAS3hukY7JVD4DtLE7FbYAd2KURKr1cie-qI7Cq3sfDoh5Hj7ZnpE5H7pzTD')

discordBase.post(content="Hello! Welcome to the free tier of Zenith Trading, enjoy trades that are announced 30 days after the trade was made!")
discordFirstTier.post(content="Hello! Welcome to the Entry tier of Zenith Trading, enjoy trades that are announced 15 days after the trade was made!")
discordFinalTier.post(content="Hello! Welcome to the Entry tier of Zenith Trading, enjoy trades all the posted trades!")

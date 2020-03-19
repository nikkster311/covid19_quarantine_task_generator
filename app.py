import random

ideasList = ["Try to grow an avocado: it will die in a few weeks, but at least you can say you tried.",
"Plan your next vacation down to the very last detail. We can’t know when it will happen, that’s up to the fates, but we can at least envision how it will take place and what we want to see when we’re there. Ah, Google Images.",
"Discover the weird and wonderful world of absurd tutorials on YouTube. There are a lot of them.",
"Research volunteering opportunities in your city and mark down the most interesting ones. When the quarantines and isolation ends, we’ll still be in a pretty precarious situation. Making a personal contribution is the best way to show the world you care.",
"But also, take this time to learn something that’s… not exactly essential in life, like juggling. Three balls minimum.",
"Overwhelmed by the news? Sign up for a link curating service like refind.com and read the articles it recommends as most relevant to you (or just as many as you can manage).",
"Create a shared playlist on Spotify and ask all the people you love to add a few songs to listen to in moments of melancholy.",
"Keep a quarantine diary: it will be 'fun' to read it again in a few years. Probably?",
"Make a list of all the annoying tasks you’ve got coming up in the next few months, and try to schedule them: appointments with the notary, checkups for moles, blood tests. Like with your fantasy holiday (but considerably less fun), you may not know when it will be possible to book them, but at least you’ll have a clearer picture of the situation. Gotta love the semblance of control!",
"Watch some films that you wouldn’t normally pick, ones that you’ve been avoiding because they’re too “demanding”, niche or simply not really “your thing”. Maybe this article can help you expand your horizons.",
"Transfer photos from your phone to an external hard drive. This is your chance to banish the 'full memory' warning for at least a month.",
"Choose 10 photos that represent 2019 for you and put them on a USB stick. As soon as the situation improves, you can take them to a print shop, but in the meantime you can relive all the good memories.",
"Are you ready to face the family photo box? Maybe put a few albums together and have a little nostalgic cry, it will do you good.",
"Are you far from your loved ones? Send them an email to tell them what everyday life is like without them.",
"Learn a poem off by heart.",
"Start keeping a dream journal, especially if it’s something you’ve wanted to do for a while, but you always put off.",
"Call. Your. Grandmother.",
"Call. Your. Mother.",
"Call. All. Your. Relatives.",
"If you have international friends, tell them about your individual experience in quarantine where you are, and try not to be too dramatic. Give them basic advice (washing their hands, etc.) to prevent the virus from spreading further.",
"Write an email to your future self.",
"If you live with your partner, have sex. If you’re long distance, have phone sex. If you don't have a partner, take the opportunity to fix up that Tinder profile.",
"Start a 19th-Century correspondence with your partner, even if you live together. Young Werther-style roleplays could be just what your relationship was missing.",
"Choose at least five people that you haven't heard from in over a month on WhatsApp and write them a message to find out how they’re doing.",
"Open a Google Doc and share it with all your friends: turn it into a sort of logbook where you can share articles, videos, songs, or even just stray thoughts.",
"Throw away that pile of newspapers, magazines and random papers that has been building up in a corner for months. You don't need them, trust me.",
"Before throwing everything in the trash though, consider repurposing them into a nice collage.",
"If you have a creative hobby like photography, painting, sculpture, writing, or graphic design, consider entering a competition. For example, the Palm* Photo Prize is open until the end of March.",
"Update your resume and portfolio, so the next time you see a job listing that inspires you, you can be the first to apply. Here are some pointers for writing the perfect CV.",
"If you have a dog, teach him something he can't do. Fetching a ball won’t cut it.",
"If you can stomach it, try to observe the crisis from several points of view: read foreign newspapers, or maybe even some longform reports.",
"For a more global look at the news than you might be getting, have a look at the CNN International newsletter.",
"In fact, try signing up for at least five newsletters, and then actually read them when they come through.",
"In the same spirit, unsubscribe from all the newsletters clogging your inbox that you never, ever open.",
"If you're under quarantine, visit your local government's website to see what free goods and services companies have made available for you.",
"You've likely already started reading a bit more than usual these days. Why not get into the personal history of your favourite authors, through articles, videos and documentaries.",
"On that note, have a look at your personal library and pull out a book that you’ve never managed to get round to. That way, the next time you’re at the bookshop you can buy a couple without feeling guilty. Now is as good a time as ever to face Infinite Jest or The Count of Monte Cristo.",
"While you’re at it, put aside three books to lend to your friends when you see them next.",
"Reading is nice, but talking about the books you've read is even better: join an online book club. And if none of them are piquing your interest, start your own!",
"Go through your closet and pick at least three items that you no longer wear to sell on sites like Depop or Vestiaire Collective. Take some nice photos, describe the product, and wait for the cash to roll in.",
"Pick three more items of clothing that you no longer use, and set them aside to give or give them to friends.",
"Fix up the clothes you’ve shoved to the back of your wardrobe, the ones with pesky holes or loose buttons.",
"Rearrange your underwear drawers. Especially the one with all the mismatched socks.",
"Tidy up your Instagram profile: are you sure that Valencia filter photo you took in Ibiza in 2016 should still be up there for the world to see?",
"Why not take some shears to your Instagram feed too, and unfollow all the boring people you've accumulated there over the years.",
"Now that your Instagram profile resembles the room of a cloistered monk, start repopulating it with some really interesting people: maybe artists, psychologists and other experts in their respective fields.",
"Open a second, themed IG account. Now is the time to get creative.",
"Browse through the most absurd IG filters and, if you have the design chops, try to create one yourself! Your follower count will grow like never before.",
"If you haven't already done so, download TikTok and start exploring.",
"Film a TikTok. It’s not that hard!",
"Google your name in quotation marks and see what comes up. It might be time to delete the old Habbo Hotel account you’d forgotten about.",
"Google the name of your partner (or crush!) in quotation marks and see if anything interesting pops up. It could potentially be fun and maybe even a bit embarrassing.",
"Download some games for your iPhone and have a friend download them that you can't see these days, so you can challenge yourself online. We recommend Ruzzle (yes, it still exists) and Fight List.",
"Have you spent the summer humming songs you don't know the meaning of? Maybe it's time to study those texts, or at least skim them.",
"Karaoke is always a great idea, especially if you want to get to know your neighbours by… arguing with them.",
"Sooner or later after all this, we’ll return to our usual frenzied rhythms. Why not meal prep for those days, cooking and filling up your freezer to its limit?",
"Clean every washable surface in your home, especially the ones you usually ignore. You will feel better afterwards, it’s science.",
"Learn how to crochet: you will get so pissed off at the tutorial you’ll forget about anything else for a good half hour at least.",
"Give yourself a manicure, do a hair mask, or anything else you can think of that can be plausibly passed off as “self-care”.",
"Experiment with your nail polishes at home. You can't go to the salon, so it’s time to get DIY with it.",
"Put together one of those disgusting homemade face masks, the ones that only require basic kitchen ingredients. It will splatter everywhere and, in a similar way to crocheting, the self-created frustration will help take your mind off things for a while.",
"Watch a yoga tutorial and get the whole sun salutation sequence down.",
"Download a meditation app, try it, and then tell all your friends that it doesn't work (or maybe it does and you can come for us via DM).",
"Study. It’s now possible to take thousands of top-level courses online, completely free. Here are a few of them.",
"Go to https://theuselessweb.com/, a useless site that will take you to other random, useless sites.",
"Take out a drawer of your bedside table and empty it onto the floor: it’s a safe bet that at least 50 percent of the things you will find inside it are completely useless.",
"Put your jewelry in order. And throw away the pieces you no longer wear. Yes, even the ones you got in elementary school with your Happy Meal.",
"Start vlogging your quarantine. It’s up to you whether you want to publish them or not, it will still make for entertaining personal viewing in the future. We recommend you don’t follow in the footsteps of this YouTuber.",
"Document what is happening, how you feel, and what you do during the day, because despite how scary it all is, we are in the middle of a unique historical moment.",
"Is your bookcase full to bursting? Try to come up with a new cataloging method for it.",
"Switch up the arrangement of the furniture in your room. Move the bed, put the carpet somewhere else, go crazy.",
"Get a vase out of storage and put the flowers you left to dry in the closet (or, er, forgot about) six months ago.",
"Make a savings plan, you know, to get yourself on track for the vacation we were talking about before. You can use finance apps like Mint or GoodBudget.",
"Find out different ways to make your home more sustainable. (You didn't do it before simply because you didn't have time, or so you said). We recommend @storiesfuse for inspiration.",
"Make not only your home, but also your shopping more eco-sustainable. Start to familiarise yourself with the concept of draught products in supermarkets and get used to the idea of doing groceries (when it’s possible again) with not only a reusable shopping bag, but also with a few jars and containers for non-packaged products.",
"Now that you have the time, try to rethink your food waste. Open the cupboard and check to see which foods are about to expire, and use them up in the next few days.",
"See which old creams and make-up are going bad - use them up in the next few days.",
"Go through your medicine drawer, throw out the expired ones, and check that your first aid kit is up to scratch.",
"Don't have a first aid kit? Order one online now.",
"While you're at it, have a shop around online for your grandmother. And do it with a smile.",
"If you are young and healthy, make yourself useful to the elderly and those with young children in your apartment building. Go to the pharmacy for them, or bring them their shopping on the landing.",
"Just, think. Take a few minutes every day to rethink your life and experiences, redefine your goals and devise strategies for how to achieve them. You'll come back stronger than ever.",
"Knowledge is power, always. Learn about topics you know little to nothing about by watching documentaries and studying online. ResearchGate and Academia.edu are two great places to start.",
"Have you always dreamed of learning how to use the Adobe package? Now’s your time. Turn boredom into 3D Art on Skillshare",
"If you miss the cinema, try to recreate its atmosphere at home. Popcorn, total darkness except for the screen, and maybe there’s a projector you forgot about lying around somewhere?",
"Watch Jane Fonda's iconic aerobics classes on YouTube. Let her knitted socks, one piece swimsuits and leg-warmer combos take you back in time to the 80s for an hour.",
"Dust off the old Nintendo and finish off all the games you left incomplete when you were younger.",
"Ten minutes of stretching a day can only do you good. That's what Youtube tutorials are for.",
"Watch an old cartoon you used to like when you were a kid, and ask yourself: did I really go crazy over this stuff? Yes, yes, you did.",
"Watch your favourite TV series from start to finish again. There's nothing wrong with that. If you want to feel less guilty and more productive, try watching it in another language.",
"If you stopped opening up the Facebook app a while ago, create a calendar with all your family and friends' birthdays.",
"Read your horoscope.",
"Send at least two of your friends their horoscope of the day. You might need to warn them.",
"Try to quit smoking.",
"Most of the above activities can be done while listening to podcasts. Listen to podcasts.",
"Whatever you decide to do, don't open Twitter: it's especially bad these days.",
"And if you're really bored: Take a shower, fix your hair, dress up, and snap a selfie. It's time to change all the horrible profile pictures you’ve kept since 2016."]

print("\n\n****************************************************************")
print("Ideas for COVID-19 self-quarantine, from https://i-d.vice.com/")
print("****************************************************************\n\n")


run = True #we are running the while loop

while run:
    task = random.choice(ideasList) #chooses a random idea from the list
    print("\n~~~~~")
    print(task) #prints idea
    print("~~~~~\n")
    print("Want another idea? (Y/N)")
    yn = input().lower() #makes everything lowrcase, takes input of above print statement
    result = yn.startswith("y")
    if result:
        continue
    else:
        print("****************************************************************")
        print("Good luck out there, and wash your hands.")
        print("****************************************************************\n")
        run = False

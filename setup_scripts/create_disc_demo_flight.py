import random

from django.conf import settings
from django.contrib.auth.models import Group, User

from discussions.models import Comment, Post, Vote


def create_demo(subjects, instructors):
    """Creates posts and comments for demo purposes when
    called in Django's manage.py shell
    """

    # Create some user accounts to serve as authors
    # for our comments
    usernames = ['BobMcBobberson', 'YomboElite', 'xxEMO_BOIxx',
                 'sandwich_king', 'pm_me_a_panini', 'millivanilli4eva',
                 'ringo', 'paul', 'john', 'george', 'padma_lakshmi',
                 'emoji_roboto', 'm_thatcher', 'xi_j', 'j_trudeau']
    password = 'password'

    print("Loading student user data to db")
    # retrieving instructors from data

    users = []
    for username in usernames:
        try:
            # avoiding duplicate users
            User.objects.get(username=username)
        except User.DoesNotExist:
            # instructor with username does not exists, let's create it
            email = '{}@gmail.com'.format(username)
            password = 'password'
            user_entity = User.objects.create_user(
                username, email, password)

            user_entity.first_name = "Somename"
            user_entity.last_name = "Lastname"
            user_entity.save()
            users.append(user_entity)

            # adding instructor to instructor group
            student_group = Group.objects.get(name=settings.GROUPS["STUDENTS"])
            student_group.user_set.add(user_entity)

    post_content = [('Is everyone doing their flight practice? I hope so',
                     '...cause some of those landings I saw were pretty NOT SO GOOD.'),
                    ('Way Cool Flight School in the news.',
                     "It's true - check out the NTSB report regarding the crash of flight WCFS9876."),
                    ("Big time F.L.Y. champion coming to Milwaulkee",
                     "I have no idea what Friendly Looping Yolos involves, but it sounds interesting"),
                    ("Large cat alert in Milwaulkee!",
                     "This mini monster is going to eat a human if we don't band together and keep our wits about us."),
                    ("Did anyone see Top Gun?",
                     "If not, what are you doing with your life? It's pretty good."),
                    ("Congratulations!!",
                     "Congratulations! ConGRATulations. Congradulashuuuuns. Congratulations!"),
                    ("Seeking a copilot in life",
                     "Who doesn't like flying, seriously??"),
                    ("Autopilot - this is a real thing?!",
                     "Do you WANT to destory our employability!? Unbelievable."),
                    ("Best flying trick in my opinion is...",
                      "The BARREL ROLL obviously"),
                    ("Did anyone lose a Cessna somewhere in Lake Michigan?",
                     "It's been left with the front desk if you are looking for it.")
                    ]
    comment_content = ["Well, I never!",
                       "I have to disagree completely",
                       "lol ok",
                       "first thing's first - you're wrong.  second, your opinon is garbage-elite ",
                       "That's some pleasant content if I've ever seen it.",
                       "Yoga engagement is off the CHARTS",
                       "The rent is too darn high",
                       "Each day / I greet the day like a newborn bird / flying high",
                       "Personally, I'm at liberty to discuss nothing",
                       "Thanks, friendo.",
                       "I get misty-eyed when that commercial comes on",
                       "Time to make the doughnuts!",
                       "I honestly don't understand what red black trees are for",
                       "I heard that 'Fresh Prince of Bel Air' is in the public domain.",
                       "It is possible to get an A",
                       "Thank you for the vote of confidence!",
                       "This.  A million times this.",
                       "Facebook stole my data!",
                       "Go Highlanders!",
                       "Please, be a little more civil",
                       "I binge watch The Great British Baking Show",
                       "YOOOOOOOooooooOOOoooo",
                       "I'm more a dog person than a cat person",
                       "I'm more of a cat person than a dog person",
                       "meh",
                       "I am a CONTENT MASTER, with MILLIONS of likes on twitter!!",
                       "No, Richard, it's 'Linux', not 'GNU/Linux'.",
                       "A statue of a Highlander could be a big boost to school spirit",
                       "I should have been a liberal arts major",
                       "I still hope to jump the Snake River Canyon at some point",
                       "Is wario a libertarian?",
                       "normal type pokemon are a waste of time",
                       "ehh, I can't really disagree",
                       "well, to each their own",
                       "not that I can tell",
                       "the only video game I've ever played was final fantasy vii",
                       "I love a quality discussion fueled by mutual respect",
                       "Do you want to make friendship bracelets?",
                       "Yikes :(",
                       "thanks for the tip",
                       "i've been thinking about mixing ketchup with vanilla ice cream as of late",
                       "anytime my friendo",
                       "frankly, i was disappointed to see this",
                       "alas, such is life",
                       "no one really knows the difference between greek and non-greek yogurt",
                       "thanks for your input",
                       "This person knows their stuff!",
                       "Yeah, maybe if I had unlimited money and unlimited time",
                       "Actually, I have to agree"
                      ]


    # Create three posts for each subject
    posts = []
    for subj in subjects:
        for x in range(3):
            content = random.choice(post_content)
            author = random.choice(instructors)
            post = Post.create(subject=subj,
                               title=content[0],
                               body=content[1],
                               author=author)
            post.save()
            posts.append(post)

    # For each post, create a comment tree:
    for post in posts:
        #Direct responses
        author = random.choice(users)
        comm1 = Comment.create(post=post,
                               body=random.choice(comment_content),
                               author=author)
        comm1.save()
        Vote.create(voter=author, value=1, comment=comm1)

        author = random.choice(users)
        comm2 = Comment.create(post=post,
                               body=random.choice(comment_content),
                               author=author)
        comm2.save()
        Vote.create(voter=author, value=1, comment=comm2)

        # Responses to comm1
        author = random.choice(users)
        comm3 = Comment.create(parent=comm1,
                               body=random.choice(comment_content),
                               author=author)
        comm3.save()
        Vote.create(voter=author, value=1, comment=comm3)

        author = random.choice(users)
        comm4 = Comment.create(parent=comm1,
                               body=random.choice(comment_content),
                               author=author)
        comm4.save()
        Vote.create(voter=author, value=1, comment=comm4)

        # Responses to comm2
        author = random.choice(users)
        comm5 = Comment.create(parent=comm2,
                               body=random.choice(comment_content),
                               author=author)
        comm5.save()
        Vote.create(voter=author, value=1, comment=comm5)

        author = random.choice(users)
        comm6 = Comment.create(parent=comm2,
                               body=random.choice(comment_content),
                               author=author)
        comm6.save()
        Vote.create(voter=author, value=1, comment=comm6)

        # Response to comm3
        author = random.choice(users)
        comm7 = Comment.create(parent=comm3,
                               body=random.choice(comment_content),
                               author=author)
        comm7.save()
        Vote.create(voter=author, value=1, comment=comm7)

        # Response to comm4
        author = random.choice(users)
        comm8 = Comment.create(parent=comm4,
                               body=random.choice(comment_content),
                               author=author)
        comm8.save()
        Vote.create(voter=author, value=1, comment=comm8)

        # Response to comm5
        author = random.choice(users)
        comm9 = Comment.create(parent=comm5,
                               body=random.choice(comment_content),
                               author=author)
        comm9.save()
        Vote.create(voter=author, value=1, comment=comm9)

        # Response to comm6
        author = random.choice(users)
        comm10 = Comment.create(parent=comm6,
                                body=random.choice(comment_content),
                                author=author)
        comm10.save()
        Vote.create(voter=author, value=1, comment=comm10)

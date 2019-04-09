COST_FOR_TWO = (
    ('$', '100'),
    ('$$', '100 - 400'),
    ('$$$', '400 - 800'),
    ('$$$$', '800 - 1500'),
    ('$$$$$', '1500+')
)

CUISINES = (
    ('Af', 'Afghan'), ('Ar', 'African'), ('Am', 'American'), ('An', 'Andhra'), ('Aa', 'Arabian'),
    ('Ae', 'Armenian'), ('As', 'Asian'), ('Ai', 'Asian Fusion'), ('A', 'Assamese'), ('Au', 'Australian'),
    ('Aw', 'Awadhi'), ('BB', 'BBQ'), ('Ba', 'Bakery'), ('Bn', 'Bangladeshi'), ('Br', 'Bar Food'),
    ('Be', 'Belgian'), ('Bg', 'Bengali'), ('Bv', 'Beverages'), ('Bi', 'Bihari'), ('By', 'Biryani'),
    ('Bo', 'Bohri'), ('Bz', 'Brazilian'), ('Bt', 'British'), ('Bu', 'Bubble Tea'), ('B', 'Burger'),
    ('Bm', 'Burmese'), ('Ca', 'Cafe'), ('Cn', 'Cantonese'), ('Ch', 'Charcoal Chicken'), ('Ce', 'Chettinad'),
    ('Ci', 'Chili'), ('Cs', 'Chinese'), ('Co', 'Colombian'), ('Ct', 'Continental'), ('Cr', 'Crepes'),
    ('Cu', 'Cuisine Varies'), ('De', 'Deli'), ('Ds', 'Desserts'), ('Dr', 'Drinks Only'), ('Du', 'Dumplings'),
    ('Eg', 'Egyptian'), ('Et', 'Ethiopian'), ('Eu', 'European'), ('Fa', 'Falafel'), ('Fs', 'Fast Food'),
    ('Fi', 'Filipino'), ('Fn', 'Finger Food'), ('Fh', 'Fish and Chips'), ('Fr', 'French'), ('Fo', 'Frozen Yogurt'),
    ('Fu', 'Fusion'), ('Ge', 'German'), ('Go', 'Goan'), ('Gr', 'Greek'), ('Gi', 'Grill'), ('Gu', 'Gujarati'),
    ('He', 'Healthy Food'), ('Ho', 'Hot Pot'), ('Hy', 'Hyderabadi'), ('Ic', 'Ice Cream'), ('In', 'Indonesian'),
    ('It', 'International'), ('Ir', 'Iranian'), ('Ii', 'Irish'), ('Is', 'Israeli'), ('Ia', 'Italian'),
    ('Ja', 'Japanese'), ('Je', 'Jewish'), ('Ju', 'Juices'), ('Ka', 'Kashmiri'), ('Ke', 'Kebab'), ('Kr', 'Kerala'),
    ('Ko', 'Konkan'), ('Kn', 'Korean'), ('La', 'Latin American'), ('Le', 'Lebanese'), ('Lu', 'Lucknowi'),
    ('Ma', 'Maharashtrian'), ('Ml', 'Malaysian'), ('Mw', 'Malwani'), ('Mn', 'Mangolorean'), ('Me', 'Mediterranean'),
    ('Mx', 'Mexican'), ('Mi', 'Middle Eastern'), ('Ms', 'Mishti'), ('Mt', 'Mithai'), ('Mo', 'Modern Australian'),
    ('Md', 'Modern European'), ('Mr', 'Modern Indian'), ('Mg', 'Mongolian'), ('Mc', 'Moroccan'), ('Mu', 'Mughlai'),
    ('Mcu', 'Multi-Cuisine'), ('Na', 'Naga'), ('Ne', 'Nepalese'), ('No', 'North Eastern'), ('Nr', 'North Indian'),
    ('Or', 'Oriental'), ('Oi', 'Oriya'), ('Ot', 'Other'), ('Pa', 'Pakistani'), ('Pn', 'Pan Asian'), ('Pi', 'Panini'),
    ('Pr', 'Parsi'), ('Ps', 'Pastry'), ('Pt', 'Patisserie'), ('Pe', 'Peruvian'), ('Pz', 'Pizza'), ('Po', 'Portugese'),
    ('Ra', 'Rajashthani'), ('Rm', 'Ramen'), ('Rw', 'Raw Meats'), ('Ro', 'Roast Chicken'), ('Rl', 'Rolls'),
    ('Ru', 'Russian'), ('Sa', 'Sandwich'), ('St', 'Satay'), ('Se', 'Seafood'), ('Si', 'Sichuan'), ('Sn', 'Sindhi'),
    ('Sg', 'Singaporean'), ('So', 'South American'), ('Su', 'South Indian'), ('Sh', 'South-Western'), ('Sp', 'Spanish'),
    ('Sr', 'Sri Lankan'), ('Sk', 'Steak'), ('S ', 'Street Food'), ('Ss', 'Sushi'), ('Sw', 'Swiss'), ('Te', 'Tea'),
    ('Tx', 'Tex-Mex'), ('Th', 'Thai'), ('Ti', 'Tibetan'), ('Tu', 'Turkish'), ('Ve', 'Vegan'), ('Vg', 'Vegetarian'),
    ('Vi', 'Vietnamese'), ('We', 'West Indian'), ('Wr', 'Wraps'), ('Yu', 'Yun Cha'), ('Ind', 'Indian'),
)

ESTABLISHMENTS = (
    ('Ca', 'Casual Dining'), ('Fi', 'Fine Dining'), ('Fo', 'Food Court'), ('Qu', 'Quick Bites'),
    ('De', 'Dessert Parlor'), ('Ba', 'Bakery'), ('Sw', 'Sweet Shop'), ('Cf', 'Cafe'), ('Dh', 'Dhaba'),
    ('Br', 'Bar'), ('Me', 'Meat Shop'), ('Be', 'Beverage Shop'), ('Pu', 'Pub'), ('Ki', 'Kiosk'), ('Lo', 'Lounge'),
    ('Mi', 'Microbrewery'), ('Cl', 'Club'), ('Fd', 'Food Truck'), ('Co', 'Confectionery'), ('Cc', 'Cocktail'),
    ('Ir', 'Irani Cafe'), ('Ms', 'Mess'), ('Ju', 'Juice'), ('Wi', 'Wine Bar'), ('Po', 'Pop Up')
)

IMAGE_TYPES = [('Re', 'Restaurant'), ('Ki', 'Kitchen'), ('La', 'Landmark'), ('Fo', 'Food')]
RESTAURANT = 'Re'

ORDER_STATUS = (
    ('Pe', 'Pending'), ('Ac', 'Accepted'), ('Pr', 'Preparing'), ('R', 'Ready'), ('Di', 'Dispatched'),
    ('D', 'Delivered'), ('R', 'Rejected'), ('C', 'Cancelled')
)

DELIVERED = "D"
PENDING = 'Pe'

BUSINESS = (
    ('H', 'Headquarters'),
    ('F', 'Franchise')
)


PAN = "P"
AADHAR = "A"
DRIVING_LICENSE = "D"
VOTER_ID = "V"
PREVIOUS_EMPLOYER_CERTIFICATE = "PEC"
EDUCATION_CERTIFICATE = "EDU"
OFFER_LETTER = "OFR"
NON_DISCLOSURE_AGREEMENT = "NDA"
PICTURE = "PIC"

EMPLOYEE_DOCUMENT_CHOICES = (
    (PAN, "Pan Card"),
    (AADHAR, "AADHAR Card"),
    (DRIVING_LICENSE, "Driving License"),
    (VOTER_ID, "Voter ID"),
    (PREVIOUS_EMPLOYER_CERTIFICATE, "Previous Employer Certificate"),
    (EDUCATION_CERTIFICATE, "Education Certificate"),
    (OFFER_LETTER, "Offer Letter"),
    (NON_DISCLOSURE_AGREEMENT, "Non Disclosure Agreement"),
    (PICTURE, "Picture")
)

DESIGNATIONS = (
    ('DB', "Delivery Boy"),
    ('M', "Manager"),
    ('CEO', "Chief Executive Officer"),
    ('PM', "Project Manager"),
    ('D', "Director"),
    ('DM', "Delivery Manager")
)

# taken = []
#
#
# def check(st, a, b, c, d):
#     string = st[a:b] + st[c:d]
#     while string in taken:
#         c += 1
#         d += 1
#         string = st[a:b] + st[c:d]
#     taken.append(string)
#     return string
#
#
# for i in Order:
#     s1 = check(i, 0, 1, 1, 2)
#     ORDER_STATUS.append((s1, i))
#
# print(ORDER_STATUS)



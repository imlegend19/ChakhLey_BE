COST_FOR_TWO = (
    ('$', '100'),
    ('$$', '100 - 400'),
    ('$$$', '400 - 800'),
    ('$$$$', '800 - 1500'),
    ('$$$$$', '1500+')
)

CUISINES = (
    ('As', 'Asian'), ('C', 'Cafe'), ('Ch', 'Chinese'), ('Co', 'Continental'), ('Ff', 'Fast Food'),
    ('Fi', 'Finger Food'), ('G', 'Grill'), ('In', 'Indian'), ('It', 'Italian'), ('Ja', 'Japanese'),
    ('Le', 'Lebanese'), ('Mi', 'Mithai'), ('Mu', 'Mughlai'), ('Ni', 'North Indian'), ('Ra', 'Rajasthani'),
    ('Si', 'South Indian'), ('Sf', 'Street Food'), ('Su', 'Sushi')
)

CUISINES_DICT = {
    'As': 'Asian', 'C': 'Cafe', 'Ch': 'Chinese', 'Co': 'Continental', 'Ff': 'Fast Food', 'Fi': 'Finger Food',
    'G': 'Grill', 'In': 'Indian', 'It': 'Italian', 'Ja': 'Japanese', 'Le': 'Lebanese', 'Mi': 'Mithai', 'Mu': 'Mughlai',
    'Ni': 'North Indian', 'Ra': 'Rajasthani', 'Si': 'South Indian', 'Sf': 'Street Food', 'Su': 'Sushi'
}

ESTABLISHMENTS = (
    ('Ca', 'Casual Dining'), ('Fi', 'Fine Dining'), ('Fo', 'Food Court'), ('Qu', 'Quick Bites'),
    ('De', 'Dessert Parlor'), ('B', 'Bakery'), ('Sw', 'Sweet Shop'), ('Cf', 'Café'), ('Dh', 'Dhaba'),
    ('Br', 'Bar'), ('Me', 'Meat Shop'), ('Be', 'Beverage Shop'), ('Pu', 'Pub'), ('Ki', 'Kiosk'), ('Lo', 'Lounge'),
    ('Mi', 'Microbrewery'), ('Cl', 'Club'), ('Fd', 'Food Truck'), ('Co', 'Confectionery'), ('Cc', 'Cocktail'),
    ('Ir', 'Irani Café'), ('Ms', 'Mess'), ('Ju', 'Juice'), ('Wi', 'Wine Bar'), ('Po', 'Pop Up')
)

IMAGE_TYPES = [('Re', 'Restaurant'), ('Ki', 'Kitchen'), ('La', 'Landmark'), ('Fo', 'Food'), ('L', 'Logo')]
IMAGE_TYPES_DICT = {'Re': 'Restaurant', 'Ki': 'Kitchen', 'La': 'Landmark', 'Fo': 'Food', 'L': 'Logo'}
RESTAURANT = 'Re'

ORDER_STATUS = (
    ('Pe', 'Pending'), ('Ac', 'Accepted'), ('Pr', 'Preparing'), ('R', 'Ready'), ('Di', 'Dispatched'),
    ('D', 'Delivered'), ('C', 'Cancelled')
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

COD = "COD"
ONLINE = "O"

PAYMENT_TYPE_CHOICES = (
    (COD, "Cash On Delivery"),
    (ONLINE, "Online"),
)

CREDIT_CARD = "CC"
DEBIT_CARD = "DC"
PAYTM = "PTM"
CASH = "C"
INSTAMOJO = "IMJ"
PAYTM_GATEWAY = "PTMG"

PAYMENT_MODE_CHOICES = (
    (CREDIT_CARD, "Credit Card"),
    (DEBIT_CARD, "Debit Card"),
    (PAYTM, "PayTM"),
    (CASH, "Cash"),
    (INSTAMOJO, "Instamojo"),
    (PAYTM_GATEWAY, "PayTM Payment Gateway"),
)

ORDER_FEEDBACK = (
    ('C', 'Complaint'),
    ('F', 'Feedback'),
    ('S', 'Suggestion')
)

COMPLAINT = 'C'

URL = "http://127.0.0.1:8000/"

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

# Generated by Django 2.2 on 2019-04-06 06:42

from django.db import migrations, models
import django.db.models.deletion
import restaurant.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('pincode', models.CharField(max_length=6, verbose_name='ZIP (Primary Location')),
                ('unit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Unit No')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('website', models.URLField(blank=True, max_length=255, verbose_name='Website / Online Listing Link')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('cost_for_two', models.CharField(choices=[('1', '100'), ('2', '100 - 400'), ('3', '400 - 800'), ('4', '800 - 1500'), ('5', '1500+')], default='100', max_length=255, verbose_name='Cost For Two')),
                ('cuisine', models.CharField(choices=[('Af', 'Afghan'), ('Ar', 'African'), ('Am', 'American'), ('An', 'Andhra'), ('Aa', 'Arabian'), ('Ae', 'Armenian'), ('As', 'Asian'), ('Ai', 'Asian Fusion'), ('A', 'Assamese'), ('Au', 'Australian'), ('Aw', 'Awadhi'), ('BB', 'BBQ'), ('Ba', 'Bakery'), ('Bn', 'Bangladeshi'), ('Br', 'Bar Food'), ('Be', 'Belgian'), ('Bg', 'Bengali'), ('Bv', 'Beverages'), ('Bi', 'Bihari'), ('By', 'Biryani'), ('Bo', 'Bohri'), ('Bz', 'Brazilian'), ('Bt', 'British'), ('Bu', 'Bubble Tea'), ('B', 'Burger'), ('Bm', 'Burmese'), ('Ca', 'Cafe'), ('Cn', 'Cantonese'), ('Ch', 'Charcoal Chicken'), ('Ce', 'Chettinad'), ('Ci', 'Chili'), ('Cs', 'Chinese'), ('Co', 'Colombian'), ('Ct', 'Continental'), ('Cr', 'Crepes'), ('Cu', 'Cuisine Varies'), ('De', 'Deli'), ('Ds', 'Desserts'), ('Dr', 'Drinks Only'), ('Du', 'Dumplings'), ('Eg', 'Egyptian'), ('Et', 'Ethiopian'), ('Eu', 'European'), ('Fa', 'Falafel'), ('Fs', 'Fast Food'), ('Fi', 'Filipino'), ('Fn', 'Finger Food'), ('Fh', 'Fish and Chips'), ('Fr', 'French'), ('Fo', 'Frozen Yogurt'), ('Fu', 'Fusion'), ('Ge', 'German'), ('Go', 'Goan'), ('Gr', 'Greek'), ('Gi', 'Grill'), ('Gu', 'Gujarati'), ('He', 'Healthy Food'), ('Ho', 'Hot Pot'), ('Hy', 'Hyderabadi'), ('Ic', 'Ice Cream'), ('In', 'Indonesian'), ('It', 'International'), ('Ir', 'Iranian'), ('Ii', 'Irish'), ('Is', 'Israeli'), ('Ia', 'Italian'), ('Ja', 'Japanese'), ('Je', 'Jewish'), ('Ju', 'Juices'), ('Ka', 'Kashmiri'), ('Ke', 'Kebab'), ('Kr', 'Kerala'), ('Ko', 'Konkan'), ('Kn', 'Korean'), ('La', 'Latin American'), ('Le', 'Lebanese'), ('Lu', 'Lucknowi'), ('Ma', 'Maharashtrian'), ('Ml', 'Malaysian'), ('Mw', 'Malwani'), ('Mn', 'Mangolorean'), ('Me', 'Mediterranean'), ('Mx', 'Mexican'), ('Mi', 'Middle Eastern'), ('Ms', 'Mishti'), ('Mt', 'Mithai'), ('Mo', 'Modern Australian'), ('Md', 'Modern European'), ('Mr', 'Modern Indian'), ('Mg', 'Mongolian'), ('Mc', 'Moroccan'), ('Mu', 'Mughlai'), ('Mcu', 'Multi-Cuisine'), ('Na', 'Naga'), ('Ne', 'Nepalese'), ('No', 'North Eastern'), ('Nr', 'North Indian'), ('Or', 'Oriental'), ('Oi', 'Oriya'), ('Ot', 'Other'), ('Pa', 'Pakistani'), ('Pn', 'Pan Asian'), ('Pi', 'Panini'), ('Pr', 'Parsi'), ('Ps', 'Pastry'), ('Pt', 'Patisserie'), ('Pe', 'Peruvian'), ('Pz', 'Pizza'), ('Po', 'Portugese'), ('Ra', 'Rajashthani'), ('Rm', 'Ramen'), ('Rw', 'Raw Meats'), ('Ro', 'Roast Chicken'), ('Rl', 'Rolls'), ('Ru', 'Russian'), ('Sa', 'Sandwich'), ('St', 'Satay'), ('Se', 'Seafood'), ('Si', 'Sichuan'), ('Sn', 'Sindhi'), ('Sg', 'Singaporean'), ('So', 'South American'), ('Su', 'South Indian'), ('Sh', 'South-Western'), ('Sp', 'Spanish'), ('Sr', 'Sri Lankan'), ('Sk', 'Steak'), ('S ', 'Street Food'), ('Ss', 'Sushi'), ('Sw', 'Swiss'), ('Te', 'Tea'), ('Tx', 'Tex-Mex'), ('Th', 'Thai'), ('Ti', 'Tibetan'), ('Tu', 'Turkish'), ('Ve', 'Vegan'), ('Vg', 'Vegetarian'), ('Vi', 'Vietnamese'), ('We', 'West Indian'), ('Wr', 'Wraps'), ('Yu', 'Yun Cha')], max_length=255, verbose_name='Type of Cuisine')),
                ('establishment', models.CharField(choices=[('Ca', 'Casual Dining'), ('Fi', 'Fine Dining'), ('Fo', 'Food Court'), ('Qu', 'Quick Bites'), ('De', 'Dessert Parlor'), ('Ba', 'Bakery'), ('Sw', 'Sweet Shop'), ('Cf', 'Cafe'), ('Dh', 'Dhaba'), ('Br', 'Bar'), ('Me', 'Meat Shop'), ('Be', 'Beverage Shop'), ('Pu', 'Pub'), ('Ki', 'Kiosk'), ('Lo', 'Lounge'), ('Mi', 'Microbrewery'), ('Cl', 'Club'), ('Fd', 'Food Truck'), ('Co', 'Confectionery'), ('Cc', 'Cocktail'), ('Ir', 'Irani Cafe'), ('Ms', 'Mess'), ('Ju', 'Juice'), ('Wi', 'Wine Bar'), ('Po', 'Pop Up')], max_length=255, verbose_name='Establishment')),
                ('delivery_time', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Delivery Time')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.Area', verbose_name='Area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.City', verbose_name='City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.Country', verbose_name='Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.State', verbose_name='State')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Re', 'Restaurant'), ('Ki', 'Kitchen'), ('La', 'Landmark'), ('Fo', 'Food')], default='Restaurant', max_length=255, verbose_name='Image Name')),
                ('image', models.ImageField(upload_to=restaurant.utils.outlet_image_upload)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.Restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Restaurant Image',
                'verbose_name_plural': 'Restaurant Images',
            },
        ),
    ]

from lingcod.common.test_settings_manager import SettingsTestCase as TestCase
from lingcod.array.models import MpaArray
from lingcod.mpa.models import Mpa, MpaDesignation
from lingcod.mpa.tests import TestMpa, MpaTestForm
from lingcod.common import utils 
from django.contrib.auth.models import *
from lingcod.sharing.models import ShareableContent
from lingcod.sharing.utils import *
from django.conf import settings
from django.test.client import Client
from django.contrib.gis.geos import GEOSGeometry 
from django.core.urlresolvers import reverse


# These classes are each given these strange names because there are already
# models named TestMpa and TestArray in lingcod.mpa.tests
# class ArrayTestMpa(Mpa):
#     extra_attr = models.CharField(max_length=255, blank=True)

class ArrayTestArray(MpaArray):
    extra_attr = models.CharField(max_length=255, blank=True)
    # 
    # objects = MpaArray.objects

        
from lingcod.features.forms import FeatureForm as UserForm

class ArrayTestForm(UserForm):
    class Meta:
        model = ArrayTestArray
        fields = ('user', 'name')


# class ArrayTestMpaForm(UserForm):
#     class Meta:
#         model = ArrayTestMpa
#         fields = ('user', 'name')

geom_final = "POLYGON ((-43400.4080995302720112 -441971.8250028975307941, -48197.4152425660649897 -441946.7300011259503663, -48201.3515400686301291 -441915.5937885036692023, -48211.9140400925243739 -441819.0624885042198002, -48220.7187400722614257 -441722.5312884929589927, -48227.9375400851859013 -441626.0312884924933314, -48233.3906400316918734 -441529.0937884994782507, -48237.0820400692900876 -441432.1562884994782507, -48239.1914400970126735 -441335.2499885042198002, -48239.5390400373144075 -441238.3437884934246540, -48238.1211400237007183 -441141.4374884963035583, -48235.1250401027136832 -441044.5624884986318648, -48230.3632400292990496 -440947.6874885009601712, -48224.0156400414634845 -440850.8124885028228164, -48215.9101400449580979 -440753.9374885009601712, -48206.2226400989384274 -440657.5312884985469282, -48194.7773400653313729 -440561.5312884966842830, -48181.5664400270470651 -440465.1249885051511228, -48166.7773400392252370 -440369.5624885009601712, -48166.4062400808834354 -440366.5937884929589927, -48231.5312400479670032 -440360.7499885032884777, -48327.9804400598222855 -440351.3124885056167841, -48424.2421400321400142 -440339.7812884943559766, -48520.3203400332349702 -440326.5624884977005422, -48616.0351400343934074 -440311.6562885004095733, -48711.5625400531207561 -440295.0312884966842830, -48806.9062400844049989 -440276.7187885036692023, -48901.7109401015040930 -440257.1562885046005249, -48996.3320400435914053 -440235.4687884957529604, -49090.5898400549122016 -440212.4999885023571551, -49184.3086400421016151 -440187.4374885009601712, -49277.4882400809801766 -440161.0937884990125895, -49370.3086400377651444 -440133.0937884952872992, -49387.7109400995614124 -440127.4687884957529604, -49395.6250400826174882 -440125.3124885051511228, -49488.8046400712628383 -440098.9687884934246540, -49581.6250400985372835 -440070.9374884990975261, -49673.9023400512523949 -440041.2187884990125895, -49765.8242400659582927 -440010.2499884958378971, -49857.0273400220103213 -439977.1249884977005422, -49947.6953400414495263 -439942.7499884958378971, -49978.0898400666410453 -439930.7499884944409132, -50066.9882400937640341 -439895.1249884953722358, -50156.3984400727931643 -439857.3749885032884777, -50245.1015400628093630 -439818.3437884883023798, -50333.0859400418994483 -439777.6249884953722358, -50420.5351400802683202 -439735.2499884990975261, -50506.9179400620050728 -439691.5624884963035583, -50592.7617400274539250 -439646.6562884957529604, -50677.7148400902442518 -439599.5937885059975088, -50761.7812400736875134 -439551.3124885037541389, -50845.1289400504319929 -439501.7187884924933314, -50927.5898400892110658 -439450.4687884952872992, -51008.9843400696117897 -439397.9374885000288486, -51089.4921400187813560 -439344.1562884966842830, -51169.1093400639074389 -439288.6874884911812842, -51247.8359400481931516 -439231.9374884981662035, -51325.4961400233733002 -439173.9374885009601712, -51402.0937400288239587 -439114.6562884948216379, -51477.6211400512547698 -439053.7187884943559766, -51552.0859400549816201 -438991.4687884957529604, -51625.4882400358910672 -438927.9999885042198002, -51697.6484400276531233 -438863.6874885023571551, -51768.7421400842576986 -438797.6562884920276701, -51838.7695400698794401 -438730.3749884958378971, -51907.5586400373358629 -438662.2812885008752346, -51975.1054400944703957 -438592.4687884976156056, -52041.5898400809746818 -438521.8124884902499616, -52106.6601400679573999 -438449.9374884972348809, -52170.4882400950809824 -438377.1874884874559939, -52209.4726400675353943 -438331.2499884963035583, -52260.8711400781830889 -438269.9999885004945099, -52322.0429400872526458 -438195.1562884943559766, -52381.9726400371728232 -438118.6249885014258325, -52440.6640400256583234 -438041.6874885009601712, -52497.9375400509161409 -437963.0624884883873165, -52553.8007400359711028 -437883.9999885009601712, -52608.2461400925603812 -437803.6874885060824454, -52661.2734400284534786 -437722.5624884967692196, -52712.8906400437772390 -437640.5624885014258325, -52763.0937400657057879 -437557.7499884981662035, -52811.8750400708813686 -437473.6562885032035410, -52859.2500400502467528 -437389.1562884855084121, -52905.0312400554321357 -437303.4062884985469282, -52949.2226400560539332 -437217.2187884999439120, -52992.0000400674980483 -437130.2187884962186217, -53033.3632400237256661 -437042.3749885000288486, -53072.9648400627993396 -436954.0937884985469282, -53111.1484400291956263 -436864.9999884981662035, -53147.7461400776301161 -436775.0624884925782681, -53182.9296400708190049 -436684.7187884948216379, -53191.9375400861754315 -436660.5312885046005249, -53219.9843400254758308 -436583.7812884990125895, -53251.9921400536768488 -436492.1874884958378971, -53282.2343400941390428 -436399.7499884972348809, -53310.8906400510168169 -436307.3124885014258325, -53337.7812400747498032 -436214.0312884962186217, -53363.2578400396960205 -436120.3749884893186390, -53386.9765400918768137 -436026.6874884990975261, -53409.1054400381326559 -435932.1874885056167841, -53429.6484400464687496 -435837.2812884976156056, -53448.4257400744536426 -435741.9374885028228164, -53465.4453400447164313 -435646.6249885028228164, -53481.0507400840288028 -435550.8749885023571551, -53494.7226400382205611 -435455.1562885004095733, -53500.2734400675326469 -435413.2187884906306863, -53510.1679400822831667 -435333.1874884977005422, -53520.6679400512293796 -435237.0624884958378971, -53529.4062400252660154 -435140.5312884976156056, -53536.5546400482489844 -435043.5624884930439293, -53541.9453400665443041 -434946.6249884916469455, -53545.5781401011190610 -434850.1249884925782681, -53547.6211400544343633 -434752.7499884958378971, -53547.9101401053776499 -434655.8437885022722185, -53546.4375400312492275 -434558.9374885051511228, -53543.3789400722525897 -434462.0624884963035583, -53538.5625400620047003 -434365.1874884925782681, -53532.1640400840842631 -434268.3124884977005422, -53524.0039400753521477 -434171.8749885046854615, -53514.2656400909254444 -434075.4374885046854615, -53502.7656400445484906 -433979.0312885022722185, -53489.5078400862330454 -433883.0312884887680411, -53474.6679400921129854 -433787.0624885014258325, -53458.0703400739002973 -433691.5312884962186217, -53439.8945400351294666 -433596.4062885041348636, -53420.1328400653292192 -433501.3124884963035583, -53398.6132400445785606 -433406.6562885008752346, -53375.3437400747134234 -433312.8437884938903153, -53365.7890400561009301 -433275.6562884938903153, -53347.7812400203983998 -433208.0624884986318648, -53321.3515400995966047 -433115.1249885000288486, -53293.3359400891204132 -433022.1874884972348809, -53263.7382400901624351 -432929.6874884995631874, -53232.3906400422129082 -432838.0312884980812669, -53199.6367400534581975 -432746.8437884994782507, -53165.1289400789173669 -432656.0624885014258325, -53129.0390400466203573 -432566.1249884981662035, -53091.5507400858041365 -432476.6562885022722185, -53052.3046400345774600 -432387.9999885009601712, -53011.6562400353941484 -432299.8124884977005422, -52969.4296400599123444 -432212.4687884990125895, -52925.6250400623393944 -432125.9687884938903153, -52880.4218400399040547 -432040.3437885013408959, -52833.6367400422241190 -431955.1249885004945099, -52785.4531400951018441 -431871.1874884990975261, -52735.8632400725473417 -431787.7187885041348636, -52684.7031400482737808 -431705.4999885032884777, -52632.1367400796152651 -431624.1249884953722358, -52578.1718400405807188 -431543.6249885028228164, -52522.8086400540341856 -431463.9687884971499443, -52466.0390400176984258 -431385.1562884952872992, -52408.0507400941787637 -431307.6562884999439120, -52348.4804400421635364 -431230.9687885036692023, -52287.6914400554014719 -431155.1562884976156056, -52225.6757400630813208 -431081.0624884995631874, -52162.2617400649032788 -431007.3749884949065745, -52097.6211400660467916 -430934.9687884948216379, -52031.7617400483941310 -430863.8437885022722185, -51964.6757400610367768 -430793.9999884995631874, -51896.1914400763052981 -430725.4062885032035410, -51826.6601401032676222 -430657.6874884949065745, -51756.0820400918237283 -430591.2499885014258325, -51684.2812400481925579 -430526.0624884907156229, -51611.2539400545574608 -430462.1562884962186217, -51537.1836400278043584 -430399.5312884948216379, -51462.0664400933965226 -430338.6249885000288486, -51423.7187400386537774 -430307.9687884948216379, -51363.9921400771418121 -430261.3437884985469282, -51286.7812400655020610 -430202.5312884962186217, -51208.5234400813933462 -430145.4374884981662035, -51129.2226400514337001 -430089.6249885014258325, -51049.0468400982063031 -430035.0624884977005422, -50967.8281400352061610 -429981.7812884999439120, -50885.9140400636824779 -429930.2187885032035410, -50802.9531400201012730 -429879.9062884994782507, -50719.1250400392891606 -429831.3124885023571551, -50634.4257400560600217 -429783.9687884966842830, -50549.0312400672919466 -429738.3437884878367186, -50462.7656400646519614 -429693.9687884985469282, -50375.8086400240863441 -429651.3124884935095906, -50287.9804400547654950 -429609.9062884985469282, -50199.4609400979607017 -429570.2187884929589927, -50110.4218400549216312 -429531.8124885046854615, -50020.6875400368589908 -429495.4999884935095906, -49930.2617400623421418 -429460.4687884924933314, -49839.1406400292253238 -429426.6874885056167841, -49747.6796400897655985 -429395.0624884990975261, -49655.5234400511108106 -429364.6874884944409132, -49562.8476400682775420 -429335.9999885000288486, -49469.8320401023593149 -429309.0312885008752346, -49376.3007400780843454 -429283.7499884995631874, -49282.2461400321117253 -429259.7187884929589927, -49187.8515400564720039 -429237.8124885056167841, -49093.1171400799576077 -429217.1874884990975261, -49074.6289400486712111 -429213.4999885028228164, -49073.3945400877928478 -429213.0624885060824454, -48978.3164400279783877 -429194.1562884892337024, -48882.8984400868721423 -429177.3124884930439293, -48787.1367400196613744 -429161.7812884915620089, -48691.2109400416375138 -429147.9374884963035583, -48594.9375400304707000 -429135.7499884986318648, -48498.5039400420064339 -429125.2812884924933314, -48402.0781400409614434 -429116.5312885008752346, -48305.3086400254615000 -429109.4374885000288486, -48208.5468400518147973 -429104.0312884943559766, -48111.6211400562970084 -429100.3437884976156056, -48014.7070400824886747 -429098.3437885008752346, -47941.8906400635096361 -429097.9062884985469282, -47902.6718400989193469 -429098.1249884953722358, -47805.6015400928445160 -429099.4999885009601712, -47708.7109400907866075 -429102.5624885042198002, -47611.8320400988741312 -429107.3124885042198002, -47515.1367400690141949 -429113.7812884980812669, -47418.6289400781170116 -429121.9062884910963476, -47322.1289400198220392 -429131.7499884972348809, -47225.8125400641074521 -429143.2812884962186217, -47129.8554400646462454 -429156.4687885036692023, -47033.9101400347135495 -429171.3749884921126068, -46938.4961401008549728 -429187.5624884967692196, -46843.2734400464469218 -429205.8437884938903153, -46748.2304400838693255 -429225.8124884986318648, -46653.7265400833566673 -429247.4999884949065745, -46559.5781400803098222 -429270.4062885004095733, -46465.7968400683676009 -429295.4687884962186217, -46372.5468400544777978 -429321.7812884990125895, -46279.8320400908996817 -429349.7812884957529604, -46187.4765400862961542 -429379.4687884929589927, -46095.6601401021616766 -429410.8437885008752346, -46004.5507400328424410 -429443.4999884958378971, -45938.5507400978240184 -429468.3749885009601712, -45902.7421400350067415 -429482.1249884981662035, -45812.7070400969096227 -429518.1249884972348809, -45723.3789400896203006 -429555.8437885004095733, -45634.7656400991472765 -429595.2499885070137680, -45546.6836400302781840 -429635.9062885064631701, -45459.4882400500719086 -429677.8437885004095733, -45372.8320400244265329 -429721.8749885084107518, -45287.0586400324391434 -429767.1874885037541389, -45205.5039400383466273 -429812.0312884980812669, -45152.8750400918870582 -429838.5624885004945099, -45067.1015400711257826 -429883.8437884929589927, -44982.2148400630539982 -429930.8437884990125895, -44898.0351400932413526 -429978.6874885004945099, -44835.6093400592508260 -430015.8124884939752519, -44788.0898400521764415 -430044.4062885027378798, -44705.6796401006722590 -430095.6249885000288486, -44624.1601400378203834 -430148.0937884971499443, -44543.5234400895424187 -430202.2499884958378971, -44463.9531400467676576 -430257.6562884924933314, -44385.4375400615172111 -430314.3437884948216379, -44307.8086400950851385 -430372.3124884986318648, -44231.0703400959610008 -430431.9374885000288486, -44155.5664400601963280 -430492.8437885046005249, -44081.1171400382881984 -430554.5937884976156056, -44007.7343400219469913 -430617.9999885009601712, -43935.4140400999967824 -430682.6874884972348809, -43864.3281400916021084 -430748.6562885013408959, -43794.3046400425810134 -430815.8749884935095906, -43725.5156400457490236 -430884.3437884948216379, -43657.9609400664994610 -430953.6874885023571551, -43614.0390400568940095 -431000.0312884910963476, -43586.3945400485608843 -431029.7812885004095733, -43521.3125400204662583 -431101.6249885056167841, -43457.4687400815455476 -431174.7499884967692196, -43394.8593400535974069 -431249.0937884920276701, -43376.2484680958878016 -431271.8445084043778479, -43376.2493994807155104 -431271.9883027430623770, -43400.4080995302720112 -441971.8250028975307941))"

class ArrayTest(TestCase):
    fixtures = ['example_data']
    
    def setUp(self):
        self.settings_manager.set(ARRAY_CLASS = 'lingcod.array.tests.ArrayTestArray')

    def test_create_array(self):
        """
        Simple array creation
        """
        user = User.objects.all()[0]
        self.assertTrue(user != None)
        array = ArrayTestArray(user=user, name="New Test Array")
        array.save()
        self.assertEquals(array.name, 'New Test Array')
        
    def test_get_array_class(self):
        """
        Tests function that retrieves the MpaArray class using the ARRAY_CLASS
        setting.
        """
        from lingcod.common.utils import get_array_class
        self.assertEquals(ArrayTestArray, get_array_class())


    def test_add_mpa(self):
        """Make sure MPAs can be added to Arrays"""
        user = User.objects.all()[0]
        mpa = TestMpa.objects.create(
            name='Test MPA',
            user=user,
            designation=MpaDesignation.objects.create(name="Test",acronym="T"),
            geometry_final=geom_final
        )
        array = ArrayTestArray.objects.create(name='My new array', user=user)
        array.add_mpa(mpa)
        self.assertEquals(mpa.array, array)
    
    def test_remove_mpa(self):
        """Make sure MPAs can be added to Arrays"""
        user = User.objects.all()[0]
        mpa = TestMpa.objects.create(
            name='Test MPA',
            user=user,
            designation=MpaDesignation.objects.create(name="Test",acronym="T"),
            geometry_final=geom_final
        )
        array = ArrayTestArray.objects.create(name='My new array', user=user)
        array.add_mpa(mpa)
        self.assertEquals(mpa.array, array)
        array.remove_mpa(mpa)
        self.assertEqual(mpa.array, None)
        self.assertEqual(array.mpa_set.count(), 0)
        self.assertRaises(Exception, array.remove_mpa, mpa)
    
    def test_mpa_set(self):
        self.settings_manager.set(ARRAY_CLASS='lingcod.array.tests.ArrayTestArray')
        self.settings_manager.set(MPA_CLASS='lingcod.mpa.tests.TestMpa')
        user = User.objects.all()[0]
        designation = MpaDesignation.objects.create(name="Test",acronym="T")
        mpa = TestMpa.objects.create(
            name='Test MPA',
            user=user,
            designation=designation,
            geometry_final=geom_final
        )
        mpa2 = TestMpa.objects.create(
            name='Test MPA 2',
            user=user,
            designation=designation,
            geometry_final=geom_final
        )
        array = ArrayTestArray.objects.create(name='My new array', user=user)
        array.add_mpa(mpa)
        array.add_mpa(mpa2)
        self.assertTrue(mpa in array.mpa_set.all())
        self.assertEquals(array.mpa_set.count(), 2)
        self.assertTrue(mpa2 in array.mpa_set.filter(name='Test MPA 2'))
        self.assertEqual(array.mpa_set.filter(user=user).count(), 2)

class ArrayManagerTest(TestCase):
    fixtures = ['example_data']
    
    def test_manager_empty(self):
        self.settings_manager.set(ARRAY_CLASS = 'lingcod.array.tests.ArrayTestArray')
        self.settings_manager.set(MPA_CLASS = 'lingcod.mpa.tests.TestMpa')
        user = User.objects.all()[0]
        old_count = ArrayTestArray.objects.empty().count()
        designation = MpaDesignation.objects.create(name="Test",acronym="T")
        # Create an Array that is not empty
        mpa = TestMpa.objects.create(
            name='Test MPA',
            user=user,
            designation=designation,
            geometry_final=geom_final
        )
        mpa2 = TestMpa.objects.create(
            name='Test MPA 2',
            user=user,
            designation=designation,
            geometry_final=geom_final
        )
        array = ArrayTestArray.objects.create(name='My new array', user=user)
        array.add_mpa(mpa)
        array.add_mpa(mpa2)
        self.assertEqual(old_count, ArrayTestArray.objects.empty().count())
        array = ArrayTestArray.objects.create(name='My new array', user=user)
        self.assertEqual(old_count + 1, ArrayTestArray.objects.empty().count())
        mpa3 = TestMpa.objects.create(
            name='Test MPA 3',
            user=user,
            designation=designation,
            geometry_final=geom_final
        )
        array.add_mpa(mpa3)
        self.assertEqual(old_count, ArrayTestArray.objects.empty().count())
        

class ArrayResourcesTestCase(TestCase):
    fixtures = ['example_data']

    #Uncomment to override the ROOT_URLCONF 
    #urls = 'lingcod.array.test_urls'

    def test_array_resources(self):
        from lingcod.rest.tests import assertImplementsRestInterface
        from lingcod.common.utils import get_array_class
        from lingcod.rest.utils import rest_uid
        self.settings_manager.set(
            ARRAY_FORM = 'lingcod.array.tests.ArrayTestForm', 
            ARRAY_CLASS = 'lingcod.array.tests.ArrayTestArray', 
            MPA_CLASS='lingcod.mpa.tests.TestMpa', 
            MPA_FORM='lingcod.mpa.tests.MpaTestForm',
        )
        self.assertEquals(ArrayTestArray, get_array_class())
        password = 'pword'
        user = User.objects.create_user('resttest', 'resttest@marinemap.org', password=password)
        from django.core.urlresolvers import reverse
        url = reverse('kmlapp-user-kml', kwargs={'input_username': user.username, 'session_key': 0})
        assertImplementsRestInterface(self, user, password, url, 
            rest_uid(ArrayTestArray), {'name': 'myname'})


class ArrayCopyTestCase(TestCase):
    fixtures = ['example_data']

    def setUp(self):
        self.settings_manager.set(
            ARRAY_FORM = 'lingcod.array.tests.ArrayTestForm', 
            ARRAY_CLASS = 'lingcod.array.tests.ArrayTestArray', 
            MPA_CLASS='lingcod.mpa.tests.TestMpa', 
            MPA_FORM='lingcod.mpa.tests.MpaTestForm',
        )
        self.client = Client()
        self.password = 'iluvmpas'
        self.user = User.objects.create_user('mpaarraytest', 'test@marinemap.org', password=self.password)
        self.user2 = User.objects.create_user('mpaarraytest2', 'test2@marinemap.org', password=self.password)

        g1 = GEOSGeometry('SRID=4326;POLYGON ((-120.42 34.37, -119.64 34.32, -119.63 34.12, -120.44 34.15, -120.42 34.37))')
        g1.transform(settings.GEOMETRY_DB_SRID)

        smr = MpaDesignation.objects.create(name="Reserve of some sort", acronym="R")
        smr.save()

        self.mpa1 = TestMpa.objects.create( name='Test_MPA_1', designation=smr, user=self.user, geometry_final=g1)
        self.mpa1.save()
        self.mpa1_name = self.mpa1.name

        array1 = ArrayTestArray.objects.create( name='Test_Array_1', user=self.user)
        array1.save()
        array1.add_mpa(self.mpa1)
        self.array1_name = array1.name
        self.array1_pk = array1.pk
        self.url = reverse('array-copy', kwargs={'pk': self.array1_pk })

        # Register the mpas and arrays as shareable content types
        mpa_ct = ContentType.objects.get(app_label='mpa',model='testmpa')
        array_ct = ContentType.objects.get(app_label='array',model='arraytestarray')

        share_mpa = ShareableContent.objects.create(shared_content_type=mpa_ct, 
                                                    container_content_type=array_ct,
                                                    container_set_property='mpa_set')
        share_array = ShareableContent.objects.create(shared_content_type=array_ct)

        # Then make the group with permissions
        self.group1 = Group.objects.create(name="Test Group 1")
        self.group1.save()
        shareables = get_shareables()
        for modelname in shareables.iterkeys():
            self.group1.permissions.add(shareables[modelname][1])

    def test_array_copy(self):
        """ Test that array's copy method works """
        array1 = ArrayTestArray.objects.get(pk=self.array1_pk)
        array2 = array1.copy(self.user)

        self.assertEquals(array2.name, self.array1_name + " (copy)")

        # Make sure MPA got copied over
        self.assertEquals(len(array2.mpa_set), len(array1.mpa_set))
        self.assertEquals(array2.mpa_set[0].name, self.mpa1_name + " (copy)")

        # Make sure the new objects are not shared
        self.assertEquals(len(array2.sharing_groups.all()), 0)
        self.assertEquals(len(array2.mpa_set[0].sharing_groups.all()), 0)

    def test_array_copy_by_get(self):
        """ Array copy web service should not accept GET requests"""
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,400)

    def test_array_copy_by_post(self):
        """Tests a standard copy using the web service"""
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(self.url)
        self.assertEquals(response.status_code,201)
        self.assertTrue(response['Location'])

    def test_array_copy_404(self):
        """Tests copy request for a non-existent array """
        self.client.login(username=self.user.username, password=self.password)
        url = reverse('array-copy', kwargs={'pk': 12345678910 })
        response = self.client.post(url)
        self.assertEquals(response.status_code,404)

    def test_array_copy_shared(self):
        """Tests if another user with proper permissions can make a copy """
        # add both users to group
        self.user.groups.add(self.group1)
        self.user2.groups.add(self.group1)

        # share the array
        the_array = ArrayTestArray.objects.get(pk=self.array1_pk)
        share_object_with_groups(the_array, [self.group1.pk])

        # Test it
        self.client.login(username=self.user2.username, password=self.password)
        response = self.client.post(self.url)
        self.assertEquals(response.status_code,201)
        self.assertTrue(response['Location'])

    def test_array_copy_403(self):
        """Tests if a user without proper permissions can make a copy """
        self.client.login(username=self.user2.username, password=self.password)
        response = self.client.post(self.url)
        self.assertEquals(response.status_code,403)

class MpaArrayServiceTestCase(TestCase):
    fixtures = ['example_data']
    def setUp(self):
        self.client = Client()
        self.password = 'iluvmpas'
        self.user = User.objects.create_user('mpaarraytest', 'test@marinemap.org', password=self.password)

        g1 = GEOSGeometry('SRID=4326;POLYGON ((-120.42 34.37, -119.64 34.32, -119.63 34.12, -120.44 34.15, -120.42 34.37))')
        g1.transform(settings.GEOMETRY_DB_SRID)

        smr = MpaDesignation.objects.create(name="Reserve of some sort", acronym="R")
        smr.save()

        mpa1 = TestMpa.objects.create( name='Test_MPA_1', designation=smr, user=self.user, geometry_final=g1)
        mpa1.save()
        self.test_mpa_id = mpa1.id

        array1 = ArrayTestArray.objects.create( name='Test_Array_1', user=self.user)
        array1.save()
        self.test_array_id = array1.id
        
        array2 = ArrayTestArray.objects.create( name='Test_Array_2', user=self.user)
        array2.save()
        self.test_array2_id = array2.id

        wrong_user = User.objects.create_user('badbad', 'bad@marinemap.org', password=self.password)
        array3 = ArrayTestArray.objects.create( name='Test_Array_3', user=wrong_user)
        array3.save()
        self.test_array3_id = array3.id
        mpa3 = TestMpa.objects.create( name='Test_MPA_3', designation=smr, user=wrong_user, geometry_final=g1)
        mpa3.save()
        self.test_mpa3_id = mpa3.id

    def test_add_mpa(self):
        """
        Make sure MPAs can be added to Arrays
        """
        self.client.login(username=self.user.username, password=self.password)
        url = reverse('array-add-mpa', kwargs={'pk': int(self.test_array_id)})
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        self.assertEquals(response.status_code, 200)

    def test_remove_mpa(self):
        """
        Make sure MPA can be removed from an array 
        """
        self.client.login(username=self.user.username, password=self.password)
        # Add
        url = reverse('array-add-mpa', kwargs={'pk': int(self.test_array_id)})
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        # Remove
        url = reverse('array-remove-mpa', kwargs={'pk': int(self.test_array_id)})
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        self.assertEquals(response.status_code, 200)

    def test_remove_mpa_invalid(self):
        """
        Make sure we get an error if we try to remove an MPA from an array 
        and it is not associated with one
        """
        self.client.login(username=self.user.username, password=self.password)
        url = reverse('array-remove-mpa', kwargs={'pk': int(self.test_array_id)})
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        self.assertEquals(response.status_code, 500)

    def test_remove_mpa_wrong_array(self):
        """
        Make sure we get an error if we try to remove an MPA from an array 
        but that MPA is associated with a different array
        """
        self.client.login(username=self.user.username, password=self.password)
        # Add
        url = reverse('array-add-mpa', kwargs={'pk': int(self.test_array_id)})
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        # Remove from wrong array
        url = reverse('array-remove-mpa', kwargs={'pk': int(self.test_array2_id)})
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        self.assertEquals(response.status_code, 500)

    def test_add_to_other_users_array(self):
        """
        Make sure we get an error if we try to add an MPA to an array that is not ours
        """
        self.client.login(username=self.user.username, password=self.password)
        # Add to other users' array
        url = reverse('array-add-mpa', kwargs={'pk': int(self.test_array3_id)})
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        self.assertEquals(response.status_code, 404)

    def test_add_other_users_mpa(self):
        """
        Make sure we get an error if we try to add someone else's MPA to our array
        """
        self.client.login(username=self.user.username, password=self.password)
        # Add to other users' array
        url = reverse('array-add-mpa', kwargs={'pk': int(self.test_array_id)})
        url += "?mpa_id=%d" % self.test_mpa3_id
        response = self.client.post(url)
        self.assertEquals(response.status_code, 404)

    def test_add_to_phantom_array(self):
        """
        Make sure we get an error if we try to add an MPA to a non-existent array 
        """
        self.client.login(username=self.user.username, password=self.password)
        # Add to other users' array
        url = reverse('array-add-mpa', kwargs={'pk': 1234567 })
        url += "?mpa_id=%d" % self.test_mpa_id
        response = self.client.post(url)
        self.assertEquals(response.status_code, 404)

    def test_add_phantom_mpa(self):
        """
        Make sure we get an error if we try to add a non-existent MPA to our array
        """
        self.client.login(username=self.user.username, password=self.password)
        # Add to other users' array
        url = reverse('array-add-mpa', kwargs={'pk': int(self.test_array_id)})
        url += "?mpa_id=%d" % 1234567
        response = self.client.post(url)
        self.assertEquals(response.status_code, 404)

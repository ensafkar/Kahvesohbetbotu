from transformers import GPT2LMHeadModel, GPT2Tokenizer
import sqlite3
import os

# Önceden eğitilmiş modeli yükleyin
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Eğer varsa veritabanını siler
if os.path.exists('coffee_chatbot.db'):
    os.remove('coffee_chatbot.db')

# Yeni bir veritabanı oluşturur
conn = sqlite3.connect('coffee_chatbot.db')
c = conn.cursor()

def create_tables():
    # Existing CoffeeBeans table
    c.execute("""
        CREATE TABLE CoffeeBeans(
        Name TEXT PRIMARY KEY,
        Country TEXT,
        History TEXT,
        BestBrewMethod TEXT,
        FlavorProfile TEXT,
        RoastType TEXT)
    """)

    # New table for brewing methods
    c.execute("""
        CREATE TABLE Brew_Methods(
        Name TEXT PRIMARY KEY,
        HowToBrew TEXT,
        Tips TEXT)
    """)

    # New table for espresso types
    c.execute('''CREATE TABLE IF NOT EXISTS EspressoTypes
                 (name TEXT, history TEXT, standard TEXT)''')

def insert_data():
    # Existing CoffeeBeans data
    # ...
    # Brazil:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Brazil', 'Brezilya', 'Brezilya, dünyanın en büyük kahve üreticisidir ve kahve, ülkenin ekonomisi için önemli bir unsur olmuştur. Çeşitli bölgelerinde yetişen çok sayıda çeşidi vardır.', 'French Press, Espresso', 'Düşük asidite, dolgun gövde, fındık ve çikolata notaları', 'Medium to Dark Roast')")

    # Ethiopia:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Ethiopia', 'Etiyopya', 'Etiyopya, kahvenin doğduğu yer olarak kabul edilir ve çok çeşitli yerel kahve çeşitlerine ev sahipliği yapar.', 'Pour Over, Drip Coffee Machine', 'Meyvemsi, çiçeksi ve çay gibi notalar, yüksek asidite, orta gövde', 'Light to Medium Roast')")

    # Tanzania:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Tanzania', 'Tanzanya', 'Tanzanya, Afrikanın önemli kahve üreticilerinden biridir. Kahve, ülkenin ekonomisi için önemli bir rol oynar.', 'Pour Over, French Press', 'Yüksek asidite, dolgun gövde, çikolatalı ve meyvemsi notalar', 'Medium Roast')")

    # El Salvador:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('El Salvador', 'El Salvador', 'El Salvador, yüksek kaliteli Arabica çekirdekleri için bilinir. Kahve, ülkenin ekonomisi için önemli bir unsur olmuştur.', 'Pour Over, French Press', 'Tatlı ve dengeli, hafif meyvemsi ve karamelli notalar', 'Medium Roast')")

    # Kenya:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Kenya', 'Kenya', 'Kenya, dünya çapında yüksek kaliteli kahve üretimiyle tanınmıştır. Özellikle çikolata ve meyve notalarıyla bilinen Kenyan Arabica çekirdekleri oldukça popülerdir.', 'Pour Over, Aeropress', 'Yüksek asidite, dolgun gövde, çikolatalı, meyvemsi ve bazen baharatlı notalar', 'Medium Roast')")

    # Burundi:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Burundi', 'Burundi', 'Burundi, özellikle yüksek kaliteli Arabica çekirdekleri yetiştiren küçük bir Doğu Afrika ülkesidir. Kahve, ülkenin ekonomisi için önemli bir unsur olmuştur.', 'Pour Over, French Press', 'Meyvemsi ve çiçeksi notalar, yüksek asidite, dolgun gövde', 'Medium Roast')")

    # Brazil - Bella giana:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Brazil - Bella giana', 'Brezilya', 'Brezilyanın Bella giana bölgesi, düşük asiditeli ve dolgun gövdeli kahveleriyle bilinir.', 'French Press, Espresso', 'Tatlı çikolata ve kavrulmuş fındık notaları', 'Medium to Dark Roast')")

    # Brazil - Jaguar:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Brazil - Jaguar', 'Brezilya', 'Jaguar bölgesi, Brezilyadaki en üst düzey kahve çekirdeklerinden bazılarını üretir.', 'Espresso, French Press', 'Yüksek gövde, düşük asidite, tatlı çikolata notaları', 'Medium to Dark Roast')")

    # Ethiopia - Banko gotiti:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Ethiopia - Banko gotiti', 'Etiyopya', 'Banko gotiti, çeşitli ve zengin lezzet profiline sahip kahveleri ile bilinen bir Etiyopya bölgesidir.', 'Pour Over, Aeropress', 'Karmaşık meyvemsi notalar, yüksek asidite, dolgun gövde', 'Light to Medium Roast')")

    # Ethiopia - Bensa gigesa:
    c.execute(
        "INSERT INTO CoffeeBeans VALUES ('Ethiopia - Bensa gigesa', 'Etiyopya', 'Bensa gigesa, çiçeksi ve meyvemsi notaları ile tanınan kahveleri üretir.', 'Pour Over, French Press', 'Meyvemsi notalar, özellikle de şeftali ve çilek notaları, yüksek asidite, orta gövde', 'Light to Medium Roast')")

    # Insert data into BrewingMethods
    # V60 (pour over)
    # Brew_Methods tablosundaki INSERT ifadelerini güncelle
    c.execute(
        "INSERT INTO Brew_Methods (Name, HowToBrew, Tips) VALUES ('V60', 'Pour Over', '1. V60 konisi üzerine uygun ölçüde kağıt filtre yerleştirin ve filtre kağıdını kaynar su ile ıslatın. 2. Öğütülmüş kahvenizi filtre kağıdına ekleyin. 3. Su ısıtıcınızdan 90-96 derece arası suyu, kahve üzerinde dairesel hareketlerle dökün. 4. 2-4 dakika bekleyin ve kahvenizin demlenmesini bekleyin.')")
    c.execute(
        "INSERT INTO Brew_Methods (Name, HowToBrew, Tips) VALUES ('Chemex', 'Pour Over', '1. Chemexe uygun büyüklükte filtre kağıdını yerleştirin ve filtre kağıdını kaynar su ile ıslatın. 2. Öğütülmüş kahvenizi filtre kağıdına ekleyin. 3. Su ısıtıcınızdan 90-96 derece arası suyu, kahve üzerinde dairesel hareketlerle dökün. 4. 4-5 dakika bekleyin ve kahvenizin demlenmesini bekleyin.')")
    c.execute(
        "INSERT INTO Brew_Methods (Name, HowToBrew, Tips) VALUES ('Kalita', 'Pour Over', '1. Kalitaya uygun büyüklükte filtre kağıdını yerleştirin ve filtre kağıdını kaynar su ile ıslatın. 2. Öğütülmüş kahvenizi filtre kağıdına ekleyin. 3. Su ısıtıcınızdan 90-96 derece arası suyu, kahve üzerinde dairesel hareketlerle dökün. 4. 2-4 dakika bekleyin ve kahvenizin demlenmesini bekleyin.')")
    c.execute(
        "INSERT INTO Brew_Methods (Name, HowToBrew, Tips) VALUES ('AeroPress', 'Press', '1. AeroPressin altına bir filtre yerleştirin ve filtre kağıdını su ile ıslatın. 2. Öğütülmüş kahveyi AeroPressin içine ekleyin. 3. Su ısıtıcınızdan 85-90 derece arası suyu, kahve üzerine dökün. 4. Yaklaşık 1-2 dakika bekleyin ve AeroPressi bir kupa üzerine ters çevirin ve yavaşça bastırın.')")
    c.execute(
        "INSERT INTO Brew_Methods (Name, HowToBrew, Tips) VALUES ('Drip Coffee', 'Drip', '1. Filtre bölümüne kağıt filtre yerleştirin. 2. Öğütülmüş kahveyi filtre kağıdına ekleyin. 3. Makinenin su deposuna soğuk su ekleyin. 4. Makineyi açın ve demlemeyi tamamlamasını bekleyin.')")
    c.execute(
        "INSERT INTO Brew_Methods (Name, HowToBrew, Tips) VALUES ('French Press', 'Press', '1. French Pressinizi ısıtın ve içine öğütülmüş kahveyi ekleyin. 2. Su ısıtıcınızdan 90-96 derece arası suyu, kahve üzerine dökün. 3. Karışımı karıştırın ve French Pressin kapağını kapatın. 4. 4 dakika bekleyin ve sonra pistonu aşağıya bastırın.')")

    # Insert data into EspressoTypes
    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('Espresso', 'Espresso, kahve çekirdeklerinin çok ince öğütülmesi ve ardından sıcak suyun yüksek basınç altında geçirilmesiyle elde edilen bir kahve çeşididir. Standart bir espresso, genellikle bir "shot" olarak adlandırılır ve yaklaşık 30 mililitredir. Kaliteli bir espresso, üzerinde krema denilen altın kahverengi bir köpük tabakası olmalıdır. Tadı, kullanılan kahve çeşidine ve kalitesine bağlı olarak değişebilir, ancak genellikle yoğun ve zengin bir aroması vardır.', 'Standart bir espresso, genellikle bir "shot" olarak adlandırılır ve yaklaşık 30 mililitredir.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('Flat White', 'Flat white, espresso ve buharla işlenmiş sütün birleşiminden oluşan bir kahve türüdür. Standart bir flat white, bir veya iki espresso shotı ve bunların üzerine dökülen az miktarda buharla işlenmiş süt ile yapılır. Bu içecek, sütün köpüğü neredeyse hiç olmadan, sütün kremsi dokusu ve espressonun yoğun tadının dikkate alınmasıyla tanınır.', 'Standart bir flat white, bir veya iki espresso shotı ve bunların üzerine dökülen az miktarda buharla işlenmiş süt ile yapılır.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('White Mocha', 'White mocha, espresso, beyaz çikolata sosu ve buharla işlenmiş sütün karışımından yapılan tatlı bir kahve içeceğidir. Genellikle üstüne süt köpüğü eklenir ve bazen beyaz çikolata sosu ile süslenir. Tatlı, kremsi ve zengin bir içecektir.', 'Standart bir White Mocha, bir ölçü espresso, beyaz çikolata sosu ve buharla işlenmiş süt ile yapılır.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('Latte', 'Latte, bir espresso shotu ve bol miktarda buharla işlenmiş süt içerir. Latte, içerdiği süt miktarı nedeniyle genellikle daha hafif bir tada sahipken, espressonun yoğunluğu hala belirgindir.', 'Standart bir Latte, bir ölçü espresso ve bol miktarda buharla işlenmiş süt içerir.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('Americano', 'Americano, bir espresso shotu ve sıcak suyun birleşiminden oluşur. Bu, espressonun yoğunluğunu sulandırır, ancak aynı zamanda hacmi artırır. Americanonun tadı genellikle bir espressoya kıyasla daha hafif olacaktır.', 'Standart bir Americano, bir ölçü espresso ve sıcak suyun birleşiminden oluşur.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('Ice Flat White', 'Ice Flat White, normal bir flat whiteın soğuk versiyonudur. Buz, bir espresso shotu ve soğuk süt karışımıyla yapılır. Tadı genellikle bir flat white gibidir ancak daha serinletici bir his verir.', 'Standart bir Ice Flat White, bir ölçü buz, bir ölçü espresso ve bir ölçü soğuk süt karışımıyla yapılır.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('Ice Aromalı Latte', 'Ice aromalı latte, soğuk espresso, soğuk süt ve çeşitli tatlar (vanilya, karamel, mocha vb.) ile yapılan bir kahve içeceğidir. Buz eklenerek serinletici hale getirilir.', 'Standart bir Ice Aromalı Latte, bir ölçü soğuk espresso, bir ölçü soğuk süt ve çeşitli tatlar (vanilya, karamel, mocha vb.) içerir.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         ('Ice Americano', 'Ice Americano, bir espresso shotu ve soğuk su ile yapılır. Buz eklenir ve genellikle şeker veya tatlandırıcı ile tatlandırılır.', 'Standart bir Ice Americano, bir ölçü buz, Double espresso ve bir ölçü soğuk su içerir.')''')

    c.execute('''INSERT INTO EspressoTypes VALUES 
                         (' Cold Drip', 'Bu yöntemde, su odası, kahve odası ve bir damlama hızı kontrol mekanizması içeren bir cihaz kullanılır. Soğuk su damla damla kahveye düşer ve yaklaşık 8 saat süren bir süreç boyunca alt tarafta toplanır. Sonuçta elde edilen soğuk demlenmiş kahve, dolgun ve kompleks bir tat profiline sahip olup, özellikle sıcak yaz günlerinde tercih edilir.', 'Standart bir Japanese Cold Drip, bir ölçü su odası, bir ölçü kahve odası ve bir damlama hızı kontrol mekanizması içerir.')''')


def fetch_bean_info(name):
    c.execute('SELECT * FROM CoffeeBeans WHERE Name=?', (name,))



    return c.fetchone()

def fetch_brew_info(name):
    c.execute('SELECT * FROM Brew_Methods WHERE Name=?', (name,))

    return c.fetchone()

def fetch_espresso_info(name):
    c.execute('SELECT * FROM EspressoTypes WHERE name=?', (name,))
    return c.fetchone()

def list_beans():
    c.execute('SELECT name FROM CoffeeBeans')
    beans = c.fetchall()
    print("\nİşte hakkında bilgi sahibi olduğum tüm çekirdekler:")
    for bean in beans:
        print(bean[0])

def add_bean(bean_info):
    # ...
    conn.commit()

def print_all_data():
    c.execute('SELECT * FROM CoffeeBeans')
    rows = c.fetchall()
    for row in rows:
        print(row)

def get_response(input_text):
    inputs = tokenizer.encode(input_text, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response
def main():
    create_tables()
    c.execute('SELECT * FROM CoffeeBeans')
    if c.fetchone() is None:
        insert_data()
        conn.commit()

    print("Kahve Sohbet Botuna hoş geldiniz! Farklı türdeki kahve çekirdekleri hakkında bilgi sağlayabilirim."
          " Bilgi sahibi olabileceğim tüm çekirdekleri görmek için 'liste' yazın, ya da hakkında"
          " daha fazla bilgi öğrenmek istediğiniz çekirdeğin adını girin.")

    # ...

    while True:
        user_input = input("\n> ")
        if user_input.lower() == 'çıkış':
            break
        elif user_input.lower() == 'liste':
            list_beans()
        elif user_input.lower().startswith('ekle'):
            add_bean(user_input.lower().lstrip('ekle ').strip())
        else:
            info = fetch_bean_info(user_input)
            if not info:
                info = fetch_brew_info(user_input)
            if not info:
                info = fetch_espresso_info(user_input)

            if info:
                if len(info) == 6:
                    # This is a bean
                    print(f"\nİşte {user_input} hakkında bulduğum bilgiler:\n"
                          f"Köken: {info[1]}\nTarihçe: {info[2]}\nEn İyi Demleme: {info[3]}\nLezzet Profili: {info[4]}\nKavurma Türü: {info[5]}")
                elif len(info) == 3:
                    # This is an espresso
                    print(f"\nİşte {user_input} hakkında bulduğum bilgiler:\n"
                          f"Tarihçe: {info[1]}\nStandart: {info[2]}")
                else:
                    # This is a brewing method
                    print(f"\nİşte {user_input} hakkında bulduğum bilgiler:\n"
                          f"Tarihçe: {info[1]}\nDemleme Yöntemi: {info[2]}")
            else:
                print(f"Üzgünüm, {user_input} hakkında bilgi bulamadım. Belki GPT-2 modelinden bir yanıt alabilirim.")
                print(get_response(user_input))

    # ...

    print_all_data() # Veritabanındaki tüm verileri yazdır

if __name__ == "__main__":
    main()

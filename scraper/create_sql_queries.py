import pickle
import random as rand

search_words = {}
search_wrods_id = {}

def load_from_file():
    pickle_off = open("products.json", 'rb')
    return pickle.load(pickle_off)

class Product():
    def __init__(self, product_dict):
        self.id = product_dict['id']
        self.id_category = product_dict['category']['id']
        self.ean = product_dict['ean'][:13]
        self.stock = product_dict['stockId']
        self.price_net = product_dict['price']['net']['final_float']
        self.additional_shipping_cost = product_dict['lowest_shipping_cost']['price_float']
        self.weight = product_dict['weight']['weight_float']
        self.name = product_dict['name'][:128]
        self.description = product_dict['description'].replace('\n','').replace('\'','\\\'')
        self.description_short = product_dict['shortDescription'].replace('\n','').replace('\'','\\\'')
        self.main_image = product_dict['main_image']
        self.images = product_dict.get('images', []).remove(self.main_image)
        if self.images is None:
            self.images = []


    def generate_sql_queries(self, f, pos):
        f.write(f"INSERT INTO ps_product (id_product, id_category_default, id_tax_rules_group, ean13, quantity, price,  additional_shipping_cost, weight, date_add, date_upd, reference, redirect_type, indexed,active,visibility) VALUES ({self.id}, {self.id_category}, 1, '{self.ean}',{self.stock},{self.price_net}, {self.additional_shipping_cost}, {self.weight}, '2000-01-01 00:00:00', '2000-01-01 00:00:00','lampy-{self.id}','301-category',1,1, 'both');")
        f.write(f"INSERT INTO ps_product_shop(id_product, id_shop, id_category_default, id_tax_rules_group, price, active, redirect_type, date_add, date_upd, indexed,visibility) VALUES ({self.id},1,{self.id_category},1,{self.price_net}, 1,'301-category', '2000-01-01 00:00:00','2000-01-01 00:00:00', 1, 'both');")
        f.write(f"INSERT INTO ps_stock_available(id_product, id_product_attribute, id_shop, id_shop_group, quantity) VALUES ({self.id},0,1,0,{self.stock});")
        for i in [1,2]:
            f.write(f"INSERT INTO ps_product_lang (id_product, id_lang, description, description_short, name, link_rewrite) VALUES ({self.id},{i}, '{self.description}','{self.description_short}','{self.name}', '{self.id}');")
        f.write(f"INSERT INTO ps_category_product (id_category, id_product, position) VALUES ({self.id_category},{self.id}, {pos});")

        f.write(f"INSERT INTO ps_image (id_image,id_product,position,cover) VALUES ({self.main_image}, {self.id}, 1, 1);")
        f.write(f"INSERT INTO ps_image_shop (id_image,id_product,id_shop,cover) VALUES ({self.main_image}, {self.id}, 1, 1);")
        for idx, image in enumerate(self.images):
            f.write(f"INSERT INTO ps_image (id_image,id_product,position,cover) VALUES ({self.main_image}, {self.id}, {idx+2}, 0);")
            f.write(f"INSERT INTO ps_image_shop (id_image,id_product,id_shop,cover) VALUES ({self.main_image}, {self.id}, 1, 0);")

        for idx, word in enumerate(self.name.split(' ')):
            if idx >= 10:
                print(len(search_words))
                break
            try:
                word_id = search_words[word]
                f.write(f"INSERT INTO ps_search_index (id_word,id_product,weight) VALUES ({word_id}, {self.id}, 1);")
                continue
            except KeyError:
                word_id = rand.randint(0,20000)
                while(search_wrods_id.get(word_id, 0) == 1):
                    print(word_id)
                    word_id = rand.randint(0,20000)

                search_wrods_id[word_id] = 1
                search_words[word] = word_id
            f.write(f"INSERT INTO ps_search_word (id_word,id_shop,id_lang,word) VALUES ({word_id}, 1, 2, '{word}');")
            f.write(f"INSERT INTO ps_search_index (id_word,id_product,weight) VALUES ({word_id}, {self.id}, 1);")





class Category():
    def __init__(self, name, _id):
        self.id = _id
        self.name = name

    def generate_sql_queries(self,f, pos):
        f.write(f"INSERT INTO ps_category (id_category, id_parent, active, is_root_category,date_add,date_upd, level_depth, position) VALUES ({self.id}, 2, 1, 0, '2000-01-01 00:00:00', '2000-01-01 00:00:00', 0, {pos});")
        f.write(f"INSERT INTO ps_category_lang (id_category, id_lang, name, link_rewrite) VALUES ({self.id}, 2, '{self.name}', '{self.name.replace(' ', '-').lower()}');")
        f.write(f"INSERT INTO ps_category_lang (id_category, id_lang, name, link_rewrite) VALUES ({self.id}, 1, '{self.name}', '{self.name.replace(' ', '-').lower()}');")
        f.write(f"INSERT INTO ps_category_shop (id_category, id_shop, position) VALUES ({self.id},1,{pos});")
        for i in range(1,4):
            f.write(f"INSERT INTO ps_category_group (id_category, id_group) VALUES ({self.id},{i});")

    def __hash__(self):
        return hash((self.id, self.name))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.id == other.id and self.name == other.name

    def __repr__(self):
        return f"name: {self.name}, id: {self.id}"


def generate_categories(products_list):
    category_set = set()
    for p in products_list:
        category_set.add(Category(p['category']['name'], p['category']['id']))
    return category_set

def create_root_category(f):
        f.write(f"INSERT INTO ps_category (id_category, id_parent, active, is_root_category,date_add,date_upd) VALUES (2, 0, 1, 1, '2000-01-01 00:00:00', '2000-01-01 00:00:00');")
        f.write(f"INSERT INTO ps_category_lang (id_category, id_lang, name, link_rewrite) VALUES (2, 2, 'lampy', 'lampy');")
        f.write(f"INSERT INTO ps_category_lang (id_category, id_lang, name, link_rewrite) VALUES (2, 1, 'lampy', 'lampy');")
        f.write(f"INSERT INTO ps_category_shop (id_category, id_shop) VALUES (2,1);")
        for i in range(1,4):
            f.write(f"INSERT INTO ps_category_group (id_category, id_group) VALUES (2,{i});")



def generate_category_queries(products_list, f):
    f.write("DELETE FROM ps_category;")
    f.write("DELETE FROM ps_category_lang;")
    f.write("DELETE FROM ps_category_shop;")
    f.write("DELETE FROM ps_category_group;")
    f.write("DELETE FROM ps_search_word;")
    f.write("DELETE FROM ps_search_index;")
    create_root_category(f)
    categories = generate_categories(products_list)
    for idx, category in enumerate(categories):
        category.generate_sql_queries(f, idx+1)

def generate_products(products_list):
    products = []
    for p in products_list:
        products.append(Product(p))
    return products


def generate_products_queries(products_list, f):
    f.write("DELETE FROM ps_product;")
    f.write("DELETE FROM ps_product_shop;")
    f.write("DELETE FROM ps_product_lang;")
    f.write("DELETE FROM ps_stock_available;")
    f.write("DELETE FROM ps_category_product;")
    f.write("DELETE FROM ps_image;")
    f.write("DELETE FROM ps_image_shop;")
    products = generate_products(products_list)
    for idx, p in enumerate(products):
        p.generate_sql_queries(f, idx+1)


def calculate_tax(product):
    return float(product['price']['gross']['final_float'])/\
            float(product['price']['net']['final_float'])

def all_product_tax_is_23_percent(products_list):
    for p in products_list:
        tax = calculate_tax(p)
        if(tax > 1.24 or tax < 1.22):
            return False
    return True


def main():
    products_list = load_from_file()
    print(f"{all_product_tax_is_23_percent(products_list)=}")

    with open('queries.sql', 'w') as f:
        generate_category_queries(products_list, f)
        generate_products_queries(products_list, f)


    # print(cat_set)
    # print(len(cat_set))

    # for p in products_list:
        # if p['category']['id'] == 88:
            # print(p['name'])

if __name__ == "__main__":
    main()


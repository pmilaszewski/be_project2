import shutil
import os

def image_prefix(image_name):
    return image_name[:image_name.find('.')]

def image_sufix(image_name):
    return image_name[image_name.find('.'):]

def create_image_path(image_name):
    prefix = image_prefix(image_name)
    res = ""
    for c in prefix:
        res = f"{res}/{c}"
    return res

def create_directory(path):
    os.makedirs(f'/var/www/prestashop/img/p/{path}', exist_ok = True)

def add_image_to_prestashop(image_name):
    img_path = create_image_path(image_name)
    create_directory(img_path)
    prefix = image_prefix(image_name)
    sufix = image_sufix(image_name)

    for additional_name in ['','-cart_default', '-home_default', '-large_default', '-medium_default', '-small_default']:
        source = f'/var/www/prestashop/scraper/img/{image_name}' 
        dst = f'/var/www/prestashop/img/p/{img_path}/{prefix}{additional_name}{sufix}'
        print(source)
        print(dst)
        shutil.copyfile(source, dst)



def main():
    images_list = []
    for f in os.listdir('/var/www/prestashop/scraper/img/'):
        if f.endswith('.jpg') or f.endswith('.png'):
            images_list.append(f)
    for image in images_list:
        add_image_to_prestashop(image)

if __name__ == "__main__":
    main()

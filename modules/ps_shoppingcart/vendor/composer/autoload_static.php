<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInitce53ee90d1d4585090cc9f575b317ae1
{
    public static $classMap = array (
        'Ps_Shoppingcart' => __DIR__ . '/../..' . '/ps_shoppingcart.php',
        'Ps_ShoppingcartAjaxModuleFrontController' => __DIR__ . '/../..' . '/controllers/front/ajax.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->classMap = ComposerStaticInitce53ee90d1d4585090cc9f575b317ae1::$classMap;

        }, null, ClassLoader::class);
    }
}

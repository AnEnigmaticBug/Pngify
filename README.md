# PNGify
This is a utility script which bulk converts SVGs to PNGs. It is mainly meant for usage with Flutter. It places the PNGs just like Flutter requires(see [this](https://flutter.dev/docs/development/ui/assets-and-images#declaring-resolution-aware-image-assets)).

It requires Inkscape to function. This is because it simply wraps the `inkscape -z -e` command to place images in the Flutter way. It does save quite a lot keystrokes.

## Usage

You specify a base width and a height along with 'variants'. Variants are real numbers and are used to create PNGs having dimensions that are a multiple of the base width and height.

As an example:
```
chmod 777 pngify.py
./pngify --wd 32 --ht 32 --variants 1.0 2.0 3.0 --svgs a.svg b.svg
```

This will create the following directories and files:
```
images/
|
|--a.png //32x32px
|--b.png //32x32px
|
|--2.0x
|  |
|  |--a.png //64x64px
|  |--b.png //64x64px
|
|--3.0x
   |
   |--a.png //96x96px
   |--b.png //96x96px
```
